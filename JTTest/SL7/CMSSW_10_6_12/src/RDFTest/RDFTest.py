import ROOT
from ROOT import *
import os

out = ROOT.TFile("Preselections.root", "RECREATE")

ROOT.ROOT.EnableImplicitMT()
RDF = ROOT.ROOT.RDataFrame

signal = RDF("tree", "/users/h2/rsk146/JTTest/SL7/CMSSW_10_2_15/src/signalM_10MC/M10signal.root")
ttbar = RDF("tree", "/users/h2/rsk146/JTTest/SL7/CMSSW_10_2_15/src/ttbarnanoAOD/ttbar2018PreselectionTree.root")
GJets = RDF("tree", "/users/h2/rsk146/JTTest/SL7/CMSSW_10_2_15/src/GJetsTrees/GJetsHT100toInf.root")
sigAK8Pt = signal.Histo1D(("sigAK8Pt", ";p_{T} (GeV)", 50, 0.0, 1600.0), "AK8_pt", "weight")
ttbarAK8Pt = ttbar.Histo1D(("ttbarAK8Pt", ";p_{T} (GeV)", 50, 0.0, 1600.0), "AK8_pt", "weight")
GJetsAK8PtHist = GJets.Histo1D(("GJetsAK8PtHist", "AK8 p_{T};p_{T} (GeV)", 50, 0.0, 1600.), "AK8_pt", "weight")


C = ROOT.TCanvas()
C.cd()
C.SetLogy()

GJetsAK8PtHist.SetLineColor(kBlue)
GJetsAK8PtHist.SetFillColor(kAzure - 9)
GJetsAK8PtHist.SetFillStyle(3001)
GJetsAK8PtHist.SetLineWidth(2)
GJetsAK8PtHist.SetStats(0)
GJetsAK8PtHist.Draw("hist")

ttbarAK8Pt.SetLineColor(kGreen)
ttbarAK8Pt.SetFillColor(kGreen)
ttbarAK8Pt.SetFillStyle(3001)
ttbarAK8Pt.SetLineWidth(2)
ttbarAK8Pt.Draw("histsame")

sigAK8Pt.SetLineColor(kRed)
sigAK8Pt.SetLineWidth(3)
sigAK8Pt.SetStats(0)
sigAK8Pt.Draw("histsame")

legend = TLegend(.8, .7, .9, .9)
legend.AddEntry(GJetsAK8PtHist.GetValue(), "#gamma+jetsMC", "f")
legend.AddEntry(ttbarAK8Pt.GetValue(), "ttbar", "f")
legend.AddEntry(sigAK8Pt.GetValue(), "Z'_{10GeV}", "l")

legend.Draw()

C.Update()
C.Modified()
out.cd()
C.Write()


