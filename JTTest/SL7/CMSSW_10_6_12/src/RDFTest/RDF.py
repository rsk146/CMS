import ROOT
from ROOT import *
import os

class histDraw:
    def __init__(self, sig, ttbar, gjet, var, out):
        C = ROOT.TCanvas(var, var)
        C.cd()
        C.SetLogy()

        gjet.SetLineColor(kBlue)
        gjet.SetFillColor(kAzure-9)
        gjet.SetFillStyle(3001)
        gjet.SetLineWidth(2)
        gjet.SetStats(0)
        gjet.GetYaxis().SetRangeUser(1, 1000000)
        gjet.Draw("hist")

        ttbar.SetLineColor(kGreen)
        ttbar.SetFillColor(kGreen)
        ttbar.SetFillStyle(3001)
        ttbar.SetLineWidth(2)
        ttbar.Draw("histsame")

        sig.SetLineColor(kRed)
        sig.SetLineWidth(3)
        sig.Draw("histsame")

        legend = TLegend(.7, .8, .9, .9)
        legend.AddEntry(gjet.GetValue(), "#gamma+jetsMC", "f")
        legend.AddEntry(ttbar.GetValue(), "ttbar", "f")
        legend.AddEntry(sig.GetValue(), "Z'_{10GeV}", "l")

        legend.Draw()

        C.Update()
        C.Modified()
        out.cd()
        C.Write()

out = ROOT.TFile("Preselections.root", "RECREATE")
ROOT.ROOT.EnableImplicitMT()
RDF = ROOT.ROOT.RDataFrame

signal = RDF("tree", "/users/h2/rsk146/JTTest/SL7/CMSSW_10_2_15/src/signalM_10MC/M10signal.root")
ttbar = RDF("tree", "/users/h2/rsk146/JTTest/SL7/CMSSW_10_2_15/src/ttbarnanoAOD/ttbar2018PreselectionTree.root")
GJets = RDF("tree", "/users/h2/rsk146/JTTest/SL7/CMSSW_10_2_15/src/GJetsTrees/GJetsHT100toInf.root")

sigAK8Pt = signal.Histo1D(("sigAK8Pt", ";p_{T} (GeV)", 50, 0, 1600.0), "AK8_pt", "weight")
ttbarAK8Pt = ttbar.Histo1D(("ttbarAK8Pt", ";p_{T} (GeV)", 50, 0, 1600.0), "AK8_pt", "weight")
GJetsAK8Pt = GJets.Histo1D(("GJetsAK8PtHist", "AK8 p_{T};p_{T} (GeV)", 50, 0, 1600.0 ), "AK8_pt", "weight")

sigAK8eta = signal.Histo1D(("sigAK8eta", ";#eta", 60, -3.0, 3.0), "AK8_eta", "weight")
ttbarAK8eta = ttbar.Histo1D(("ttbarAK8eta", ";#eta", 60, -3.0, 3.0), "AK8_eta", "weight")
GJetsAK8eta = GJets.Histo1D(("GJetsAK8eta", "AK8 #eta;AK8 #eta", 60, -3.0, 3.0), "AK8_eta", "weight")

sigAK8SDM = signal.Histo1D(("sigAK8SDM", ";Soft DropMass (GeV)", 50, 0, 200.0), "AK8_msoftdrop", "weight")
ttbarAK8SDM = ttbar.Histo1D(("ttbarAK8SDM", ";Soft Drop Mass (GeV)", 50, 0.0, 200.0), "AK8_msoftdrop", "weight")
GJetsAK8SDM = GJets.Histo1D(("GJetsAK8SDM", "AK8 Soft Drop Mass ;Soft Drop Mass (GeV)", 50, 0.0, 200.0), "AK8_msoftdrop", "weight")

sigAK8N2 = signal.Histo1D(("sigAK8N2", ";N2", 50, 0.0, .5), "AK8_n2", "weight")
ttbarAK8N2 = ttbar.Histo1D(("ttbarAK8N2", ";N2", 50, 0.0, .5), "AK8_n2", "weight")
GJetsAK8N2 = GJets.Histo1D(("GJetsAK8N2", "N2;N2", 50, 0.0, .5), "AK8_n2", "weight")

sigPt = signal.Histo1D(("sigPt", ";Photon p_{T} (GeV)", 50, 0.0, 1600.), "Photon_pt", "weight")
ttbarPt = ttbar.Histo1D(("ttbarPt", ";Photon p_{T} (GeV)", 50, 0.0, 1600.), "Photon_pt", "weight")
GJetsPt = GJets.Histo1D(("GJetsPt", "Photon p_{T}; Photon p_{T} (GeV)", 50, 0.0, 1600.), "Photon_pt", "weight")

sigEta = signal.Histo1D(("sigEta", ";Photon #eta", 60, -3.0, 3.0), "Photon_eta", "weight")
ttbarEta = ttbar.Histo1D(("ttbarEta", ";Photon #eta", 60, -3.0, 3.0), "Photon_eta", "weight")
GJetsEta = GJets.Histo1D(("GJetsEta", "Photon #eta; Photon #eta", 60, -3.0, 3.0), "Photon_eta", "weight")

histDraw(sigAK8Pt, ttbarAK8Pt, GJetsAK8Pt, "AK8 p_{T}", out)
histDraw(sigAK8eta, ttbarAK8eta, GJetsAK8eta, "AK8 Eta", out)
histDraw(sigAK8SDM, ttbarAK8SDM, GJetsAK8SDM, "AK8 SDM", out)
histDraw(sigAK8N2, ttbarAK8N2, GJetsAK8N2, "AK8 N2", out)
histDraw(sigPt, ttbarPt, GJetsPt, "Photon p_{T}", out)
histDraw(sigEta, ttbarEta, GJetsEta, "Photon Eta", out)


