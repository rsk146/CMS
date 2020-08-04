import ROOT
from ROOT import *
import os
import sys

class histDraw:
    def __init__(self, sample, out, canvas):
        C = ROOT.TCanvas(canvas, canvas)
        C.cd()
        gStyle.SetPalette(1)
        sample.SetStats(0)
        sample.Draw("colx")
        C.Update()
        C.Modified()
        out.cd()
        C.Write()

out = ROOT.TFile("JetPtDeltaR.root", "RECREATE")
ROOT.ROOT.EnableImplicitMT()
RDF = ROOT.ROOT.RDataFrame

ttbar = RDF("tree", sys.argv[1])
signal10 = RDF("tree", sys.argv[2])
signal25 = RDF("tree", sys.argv[3])

test = ttbar.Histo2D(("ttbar", "ttbar;Jet p_{T} (GeV);#DeltaR_{j #gamma}", 40, 0, 800.0, 15, 0, 3.0), "AK4_pt", "AK4_Photon_deltaR", "weight")
test2 = signal10.Histo2D(("sig10", "sig10;Jet p_{T} (GeV);#DeltaR_{j #gamma}", 40, 0, 800.0, 15, 0, 3.0), "AK4_pt", "AK4_Photon_deltaR", "weight")
test3 = signal25.Histo2D(("sig25", "sig25;Jet p_{T} (GeV);#DeltaR_{j #gamma}", 40, 0, 800.0, 15, 0, 3.0), "AK4_pt", "AK4_Photon_deltaR", "weight")

histDraw(test, out, "ttbar")
histDraw(test2, out, "signal10")
histDraw(test3, out, "signal25")