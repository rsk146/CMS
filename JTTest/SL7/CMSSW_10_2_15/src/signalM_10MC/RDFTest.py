import ROOT
from ROOT import *
import os

out = ROOT.TFile("Preselections.root", "UPDATE")

ROOT.ROOT.EnableImplicitMT()
RDF = ROOT.ROOT.RDataFrame

signal = RDF("tree", "M10signal.root")
ttbar = RDF("tree", "../ttbarnanoAOD/ttbar2018TreeTest.root")
GJets1 = RDF("tree", "../GJetsTrees/GJetsHT100to200.root")
GJets2 = RDF("tree", "../GJetsTrees/GJetsHT200to400.root")
GJets3 = RDF("tree", "../GJetsTrees/GJetsHT400to600.root")
GJets4 = RDF("tree", "../GJetsTrees/GJetsHT600toInf.root")

sigAK8Pt = signal.Histo1D(("sigAK8Pt", ";p_{T} (GeV)", 50, 0.0, 1600.0), "AK8_pt", "weight")
ttbarAK8Pt = ttbar.Histo1D(("ttbarAK8Pt", ";p_{T} (GeV)", 50, 0.0, 1600.0), "AK8_pt", "weight")
GJets1AK8Pt = GJets1.Histo1D(("GJets1AK8Pt", ";p_{T} (GeV)", 50, 0.0, 1600.0), "AK8_pt", "weight")
GJets2AK8Pt = GJets2.Histo1D(("GJets2AK8Pt", ";p_{T} (GeV)", 50, 0.0, 1600.0), "AK8_pt", "weight")
GJets3AK8Pt = GJets3.Histo1D(("GJets3AK8Pt", ";p_{T} (GeV)", 50, 0.0, 1600.0), "AK8_pt", "weight")
GJets4AK8Pt = GJets4.Histo1D(("GJets4AK8Pt", ";p_{T} (GeV)", 50, 0.0, 1600.0), "AK8_pt", "weight")
GJetsAK8PtHist = ROOT.TH1F("GJetsAK8Pt", ";p_{T} (GeV)", 50, 0.0, 1600.0)
GJetsAK8PtHist.Add(GJets1AK8Pt)
GJetsAK8PtHist.Add(GJets2AK8Pt)
GJetsAK8PtHist.Add(GJets3AK8Pt)
GJetsAK8PtHist.Add(GJets4AK8Pt)

C = ROOT.TCanvas()
C.cd()
sigAK8Pt.Draw("hist")
ttbarAK8Pt.Draw("hist same")
GJetsAK8PtHist.Draw("hist same")
C.Update()
C.Modified()
out.cd()
C.Write()

