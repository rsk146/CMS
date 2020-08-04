import ROOT
from ROOT import *
import os
from RDF import histDraw

out = ROOT.TFile("tau32.root", "RECREATE")
ROOT.ROOT.EnableImplicitMT()
RDF = ROOT.ROOT.RDataFrame

signal = RDF("tree", "signalM10PreselectionTreeAK4Photon.root")
ttbar = RDF("tree", "ttbar2018PreselectionTreeAK4Photon.root")
gjets = RDF("tree", "100toInfPreselectionTreeAK4Photon.root")

sigtau32 = signal.Histo1D(("sigtau32", "#tau_{3}/#tau_{2}; #tau_{3}/#tau_{2}", 50, 0, 1), "AK8_tau32", "weight")
ttbartau32 = ttbar.Histo1D(("ttbartau32", "#tau_{3}/#tau_{2}; #tau_{3}/#tau_{2}", 50, 0, 1), "AK8_tau32", "weight")
gjetstau32 = gjets.Histo1D(("gjetstau32", "#tau_{3}/#tau_{2}; #tau_{3}/#tau_{2}", 50, 0, 1), "AK8_tau32", "weight")

histDraw(sigtau32, ttbartau32, gjetstau32, "tau32", out)
