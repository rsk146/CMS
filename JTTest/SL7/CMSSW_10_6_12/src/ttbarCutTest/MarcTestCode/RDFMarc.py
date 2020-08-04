####### RDataFrame Examples:
#######
import ROOT # Duh...
import os # Not really sure if you need this, the example I started from had it, so here it is.

ROOT.ROOT.EnableImplicitMT() # This allows root to multi-thread when applicable (i.e. when processing events)
RDF = ROOT.ROOT.RDataFrame # Just to make things more redable

# Here I'm loading a ttree from a file. This is the equivalent of T = TFile.Get(TTree)
QCD = RDF("tree_nominal", "/home/rek81/userArea/CMSSW_10_2_2/src/nano_to_tree/2016_QCD/2016_QCD_PFHT800.root")
# Just like with TTree.Draw() we can define our cuts as strings. Note however that this is no longer a ROOT expression, but a C++ evaluatable:
cut = "evt_HT>900. && J2pt>300."
# Basically this is something that C++ would return true or false for.
cut_QCD = QCD.Filter(cut) # It really is that simple, SR_QCD is now a new RDF that has had the cut applied to it
QCDcount = QCD.Count() #  I can count how many events are in each set
QCDcutcount = cut_QCD.Count()
print str(QCDcutcount.GetValue()) + " events left after applying the cut"
print "compared to " + str(QCDcount.GetValue()) + " original events"
# you can plot stuff really intuitively and simply:
QCDplot = cut_QCD.Histo2D(("QCD_Dist", ";#Delta#eta;Jet Double-b Tag;Events", 50, 0., 4., 50, -1., 1.), "evt_Deta","J2dbtag", "weight")
# here evt_Deta, J2dbtag and weight are all branches of the TTree.
C = ROOT.TCanvas()
C.SetRightMargin(0.125) # keeps the Z-title on the canvas
C.cd()
QCDplot.Draw("colz")
# Ok, now for the good stuff:
# The tree I'm using stores two masses: the J1SDM and J2SDM
# Let's say I want to plot the maximum mass? (This was not possible in TTree.Draw())
# Here's how you do it:
code = 	''' float GetMaxSDM(float J1, float J2)
			{
				return max(J1, J2);
			}
		'''
# Notice that this is C++. I can use it to "define" a new column (variable)
ROOT.gInterpreter.Declare(code) #now ROOT knows how to do that!
NewRDF = cut_QCD.Define("MaxSDM", "GetMaxSDM(J1SDM, J2SDM)") #make the variable (careful, you have to add it to a new object, it doesn't get added to cut_QCD)
# Make some plots to check that it worked:
M1 = NewRDF.Histo1D(("M1", ";masses (GeV)", 100, 0., 500.), "J1SDM", "weight")
M2 = NewRDF.Histo1D(("M2", ";masses (GeV)", 100, 0., 500.), "J2SDM", "weight")
M2.SetLineColor(ROOT.kRed)
Mm = NewRDF.Histo1D(("Mmax", ";masses (GeV)", 100, 0., 500.), "MaxSDM", "weight")
Mm.SetLineColor(ROOT.kGreen)
C2 = ROOT.TCanvas()
C2.cd()
M1.Draw("hist")
M2.Draw("histsame")
Mm.Draw("histsame")
# But wait, there's more: You can use ROOT objects in your "code" that you feed into the RDF
# I'll define a random TF1:
fit = ROOT.TF1("fit_square", "x*x", 0., 500.)
# now I add it to ROOT so I can use it in a function:
ROOT.gInterpreter.ProcessLine("auto  myFit = fit_square;")
fancy_code = 	'''
				float EvalSquare(float x)
				{
					return myFit->Eval(x);
				}
				'''
ROOT.gInterpreter.Declare(fancy_code)
NewNewRDF = NewRDF.Define("squareofMaxSDM", "EvalSquare(MaxSDM)") # this function should make a new branch which is just the square of the MaxSDM
Plot2 = NewNewRDF.Histo2D(("name", ";MaxSDM;MaxSDM^{2}", 100, 0., 500., 100, 0., 250000.), "MaxSDM", "squareofMaxSDM", "weight")
C3 = ROOT.TCanvas()
C3.SetRightMargin(0.125)
C3.cd()
Plot2.Draw("colz")