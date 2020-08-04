import ROOT
from ROOT import *
import os
import sys
from vetos import histDraw
from histDraw import Hist_Setup
from CutoffEfficient import Cutoffs

if __name__ == "__main__":
    out = ROOT.TFile("N2DDTPreselections.root", "RECREATE")
    ROOT.ROOT.EnableImplicitMT()
    RDF = ROOT.ROOT.RDataFrame
    ttbar = RDF("tree", sys.argv[1])
    signal = RDF("tree", sys.argv[2])
    gjets = RDF("tree", sys.argv[3])
    
    #ttbar
    hists = [[TH1F(str(i) + ", " + str(j), "N2 with Cuts; N2; Events", 50, 0., .5) for j in range(16)] for i in range(16)]
    test = Cutoffs("N210ttbar", sys.argv[1], hists, "ttbar")
    cutoff_hist = TH2F(test.cutoffHist)
    ROOT.gInterpreter.ProcessLine("auto cutoff = Cutoffsttbar;")
    fancy_code =     '''
                        float ddt(float pt, float rho, float n2)
                        {   
                            int xbin = cutoff->GetXaxis()->FindBin(rho);
                            int ybin = cutoff->GetYaxis()->FindBin(pt);
                            return n2 - cutoff->GetBinContent(xbin, ybin);
                        }
                        '''
    ROOT.gInterpreter.Declare(fancy_code)
    ttbarC = ttbar.Filter("AK8_rho >= -7. && AK8_rho <= -2.")
    n2ttbar = ttbarC.Define("N2DDT", "ddt(AK8_pt, AK8_rho, AK8_n2)")
    #n2cutttbar = n2ttbar.Filter("MET < 75 && AK4_csv < .55 && AK8_tau32 > .5 && N2DDT < 0 && AK4_pt < 50")
    
    #signal
    hists2 = [[TH1F(str(i) + ", " + str(j), "N2 with Cuts; N2; Events", 50, 0., .5) for j in range(16)] for i in range(16)]
    test2 = Cutoffs("N210signal", sys.argv[2], hists2, "signal")
    cutoff_hist2 = TH2F(test2.cutoffHist)
    ROOT.gInterpreter.ProcessLine("auto cutoff2 = Cutoffssignal;")
    fancy_code2 = '''
                        float ddt2(float pt, float rho, float n2)
                        {   
                            int xbin = cutoff2->GetXaxis()->FindBin(rho);
                            int ybin = cutoff2->GetYaxis()->FindBin(pt);
                            return n2 - cutoff2->GetBinContent(xbin, ybin);
                        }
                        '''
    ROOT.gInterpreter.Declare(fancy_code2)
    signalC = signal.Filter("AK8_rho >= -7. && AK8_rho <= -2.")
    n2signal = signalC.Define("N2DDT", "ddt2(AK8_pt, AK8_rho, AK8_n2)")
    #n2cutsignal = n2signal.Filter("MET < 75 && AK4_csv < .55 && AK8_tau32 > .5 && N2DDT < 0 && AK4_pt < 50")

    #gjets
    hists3 = [[TH1F(str(i) + ", " + str(j), "N2 with Cuts; N2; Events", 50, 0., .5) for j in range(16)] for i in range(16)]
    test3 = Cutoffs("N210gjets", sys.argv[3], hists3, "gjets")
    cutoff_hist3 = TH2F(test3.cutoffHist)
    ROOT.gInterpreter.ProcessLine("auto cutoff3 = Cutoffsgjets;")
    fancy_code3 = '''
                        float ddt3(float pt, float rho, float n2)
                        {   
                            int xbin = cutoff3->GetXaxis()->FindBin(rho);
                            int ybin = cutoff3->GetYaxis()->FindBin(pt);
                            return n2 - cutoff3->GetBinContent(xbin, ybin);
                        }
                        '''
    ROOT.gInterpreter.Declare(fancy_code3)
    gjetsC = gjets.Filter("AK8_rho >= -7. && AK8_rho <= -2.")
    n2gjets = gjetsC.Define("N2DDT", "ddt3(AK8_pt, AK8_rho, AK8_n2)")

    sign2ddt = n2signal.Histo1D(("sign2ddt", "N2DDT", 50, -.2, .25), "N2DDT", "weight")
    ttbarn2ddt = n2ttbar.Histo1D(("ttbarn2ddt", "N2DDT", 50, -.2, .25), "N2DDT", "weight")
    gjetsn2ddt = n2gjets.Histo1D(("gjetsn2ddt", "N2DDT", 50, -.2, .25), "N2DDT", "weight")

    histDraw(sign2ddt, ttbarn2ddt, gjetsn2ddt, "N2DDT", out)

    #sign2cut = n2signal.Filter("N2DDT < 0")
    #ttbarn2cut = n2ttbar.Filter("N2DDT < 0")
    #gjetsn2cut = n2gjets.Filter("N2DDT < 0")
    
   # Hist_Setup(sign2cut, ttbarn2cut, gjetsn2cut, " N2DDT < 0", out)
    #sign2ddtpt = sign2cut.Histo2D(("sigptn2ddt", ";p_{T};N2DDT", 16, 100, 800, 40, -.25, .2), "AK8_pt", "N2DDT", "weight")
    #ttbarn2ddtpt = ttbarn2cut.Histo2D(("ttbarptn2ddt", ";p_{T};N2DDT", 16, 100, 800, 40, -.25, .2), "AK8_pt", "N2DDT", "weight")
    #gjetsn2ddtpt = gjetsn2cut.Histo2D(("gjestptn2ddt", ";p_{T};N2DDT", 16, 100, 800, 40, -.25, .2), "AK8_pt", "N2DDT", "weight")
    