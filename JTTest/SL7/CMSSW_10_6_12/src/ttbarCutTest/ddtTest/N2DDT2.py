import ROOT
from ROOT import *
import os
import sys
from vetos import histDraw
from histDraw import Hist_Setup
from CutoffEfficient import Cutoffs

if __name__ == "__main__":
    out = ROOT.TFile("N2DDTtest.root", "RECREATE")
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
    fancy_code =    '''
                        float ddt(float pt, float rho, float n2)
                        {   
                            int xbin = cutoff->GetXaxis()->FindBin(rho);
                            int ybin = cutoff->GetYaxis()->FindBin(pt);
                            return n2 - cutoff->GetBinContent(xbin, ybin);
                        }
                        '''
    ROOT.gInterpreter.Declare(fancy_code)
    n2ttbar = ttbar.Define("N2DDT", "ddt(AK8_pt, AK8_rho, AK8_n2)")
    n2cutttbar = n2ttbar.Filter("MET < 75 && AK4_csv < .55 && AK8_tau32 > .5 && N2DDT < 0 && AK4_pt < 50")
    
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
    n2signal = signal.Define("N2DDT", "ddt2(AK8_pt, AK8_rho, AK8_n2)")
    n2cutsignal = n2signal.Filter("MET < 75 && AK4_csv < .55 && AK8_tau32 > .5 && N2DDT < 0 && AK4_pt < 50")

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
    n2gjets = gjets.Define("N2DDT", "ddt3(AK8_pt, AK8_rho, AK8_n2)")
    n2cutgjets = n2gjets.Filter("MET < 75 && AK4_csv < .55 && AK8_tau32 > .5 && N2DDT < 0 && AK4_pt < 50")
    
    Hist_Setup(n2cutsignal, n2cutttbar, n2cutgjets, " All Cuts and N2DDT", out)    

    ttbar_nopt = n2ttbar.Filter("MET < 75 && AK4_csv < .55 && AK8_tau32 > .5 && N2DDT < 0")
    signal_nopt = n2signal.Filter("MET < 75 && AK4_csv < .55 && AK8_tau32 > .5 && N2DDT < 0")
    gjets_nopt = n2gjets.Filter("MET < 75 && AK4_csv < .55 && AK8_tau32 > .5 && N2DDT < 0")
    ttbar_n = ttbar_nopt.Histo1D(("ttbar", "", 50, 0., 800.0), "AK4_pt", "weight")
    signal_n = signal_nopt.Histo1D(("signal", "", 50, 0., 800.0), "AK4_pt", "weight")
    gjets_n = gjets_nopt.Histo1D(("gjets", "AK4 p_{T}; AK4 p_{T} (GeV)", 50, 0., 800.0), "AK4_pt", "weight")
    histDraw(signal_n, ttbar_n, gjets_n, "N-1: AK4 pT", out)

    ttbar_nomet = n2ttbar.Filter("AK4_csv < .55 && AK8_tau32 > .5 && AK4_pt < 50 && N2DDT < 0")
    signal_nomet = n2signal.Filter("AK4_csv < .55 && AK8_tau32 > .5 && AK4_pt < 50 && N2DDT < 0")
    gjets_nomet = n2gjets.Filter("AK4_csv < .55 && AK8_tau32 > .5 && AK4_pt < 50 && N2DDT < 0")
    ttbar_n = ttbar_nomet.Histo1D(("ttbar", "", 50, 0., 500.0), "MET", "weight")
    signal_n = signal_nomet.Histo1D(("signal", "", 50, 0., 500.0), "MET", "weight")
    gjets_n = gjets_nomet.Histo1D(("gjets", "MET; MET (GeV)", 50, 0., 500.0), "MET", "weight")
    histDraw(signal_n, ttbar_n, gjets_n, "N-1: MET", out)

    ttbar_nocsv = n2ttbar.Filter("MET < 75 && AK8_tau32 > .5 && AK4_pt < 50 && N2DDT < 0")
    signal_nocsv = n2signal.Filter("MET < 75 && AK8_tau32 > .5 && AK4_pt < 50 && N2DDT < 0")
    gjets_nocsv = n2gjets.Filter("MET < 75 && AK8_tau32 > .5 && AK4_pt < 50 && N2DDT < 0")
    ttbar_n = ttbar_nocsv.Histo1D(("ttbar", "", 50, 0., 1), "AK4_csv", "weight")
    signal_n = signal_nocsv.Histo1D(("signal", "", 50, 0., 1.0), "AK4_csv", "weight")
    gjets_n = gjets_nocsv.Histo1D(("gjets", "AK4 bTag; AK4 bTag", 50, 0., 1.0), "AK4_csv", "weight")
    histDraw(signal_n, ttbar_n, gjets_n, "N-1: bTag", out)

    ttbar_notau = n2ttbar.Filter("MET < 75 && AK4_csv < .55 && AK4_pt < 50 && N2DDT < 0")
    signal_notau = n2signal.Filter("MET < 75 && AK4_csv < .55 && AK4_pt < 50 && N2DDT < 0")
    gjets_notau = n2gjets.Filter("MET < 75 && AK4_csv < .55 && AK4_pt < 50 && N2DDT < 0")
    ttbar_n = ttbar_notau.Histo1D(("ttbar", "", 50, 0., 1), "AK8_tau32", "weight")
    signal_n = signal_notau.Histo1D(("signal", "", 50, 0., 1.0), "AK8_tau32", "weight")
    gjets_n = gjets_notau.Histo1D(("gjets", "AK8 tau32; AK8 tau32", 50, 0., 1.0), "AK8_tau32", "weight")
    histDraw(signal_n, ttbar_n, gjets_n, "N-1: tau32", out)

    ttbar_noN2 = n2ttbar.Filter("MET < 75 && AK4_csv < .55 && AK4_pt < 50 && AK8_tau32 > .5")
    signal_noN2 = n2signal.Filter("MET < 75 && AK4_csv < .55 && AK4_pt < 50 && AK8_tau32 > .5")
    gjets_noN2 = n2gjets.Filter("MET < 75 && AK4_csv < .55 && AK4_pt < 50 && AK8_tau32 > .5")
    ttbar_n = ttbar_noN2.Histo1D(("ttbar", "", 50, -1., 1), "N2DDT", "weight")
    signal_n = signal_noN2.Histo1D(("signal", "", 50, -1, 1), "N2DDT", "weight")
    gjets_n = gjets_noN2.Histo1D(("gjets", "", 50, -1, 1), "N2DDT", "weight")
    histDraw(signal_n, ttbar_n, gjets_n, "N-1: N2DDT", out)