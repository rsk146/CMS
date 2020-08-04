import ROOT
from ROOT import *
import os
import sys
from histDraw import histDraw
from CutoffEfficient import Cutoffs

'''def getBinVals(self, pt, rho):
    xbin = cutoff_hist.GetXaxis().FindBin(rho)
    ybin = cutoff_hist.GetYaxis().FindBin(pt)
    return xbin, ybin

def getCutoffVal(self, pt, rho):
    xbin, ybin = getBinVals(pt, rho)
    return cutoff_hist.GetBinContent(xbin, ybin)

def ddt(self, pt, rho, n2):
    return n2 - getCutoffVal(pt, rho)
#ddt = lambda pt, rho, n2: n2 - getCutoffVal(pt, rho) '''

if __name__ == "__main__":
    out = ROOT.TFile("N2DDTtest.root", "RECREATE")
    ROOT.ROOT.EnableImplicitMT()
    RDF = ROOT.ROOT.RDataFrame

    #hists = [[TH1F(str(i) + ", " + str(j), "N2 with Cuts; N2; Events", 50, 0., .5) for j in range(16)] for i in range(16)]
    #utoff = Cutoffs("N210ttbar", sys.argv[1], hists)

    cutoff_hist = TH2F()
    print type(cutoff_hist)
    ROOT.TFile(sys.argv[2]).GetObject("Cutoffs", cutoff_hist)
    ttbar = RDF("tree", sys.argv[1]) 
    ROOT.gInterpreter.ProcessLine("auto  cutoff = Cutoffs;")
    fancy_code =    '''
                    float ddt(float pt, float rho, float n2)
                    {
                        int xbin = cutoff->GetXaxis()->FindBin(rho);
                        int ybin = cutoff->GetYaxis()->FindBin(pt);
                        return n2 - cutoff->GetBinContent(xbin, ybin);
                    }
                    '''
    ROOT.gInterpreter.Declare(fancy_code)
    n2ddt = ttbar.Define("N2DDT", "ddt(AK8_pt, AK8_rho, AK8_n2)")
    ddt = n2ddt.Histo1D(("n2ddt", "N2DDT; N2 DDT;", 50, -1.0, 1.0), "N2DDT", "weight")
    C = ROOT.TCanvas("N2DDT", "N2DDT")
    C.cd()
    C.SetLogy()
    ddt.SetLineColor(kGreen)
    ddt.SetFillColor(kGreen)
    ddt.SetFillStyle(3001)
    ddt.SetLineWidth(2)
    ddt.Draw("hist")
    C.Update()
    C.Modified()
    out.cd()
    C.Write()
