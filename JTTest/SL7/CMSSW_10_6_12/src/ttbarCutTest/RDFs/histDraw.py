import ROOT
from ROOT import *
import os
import sys

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

def Hist_Setup(signal_metCut, ttbar_metCut, GJets_metCut, cut, out):
    sigAK8Pt = signal_metCut.Histo1D(("sigAK8Pt", ";p_{T} (GeV)", 50, 0, 1600.0), "AK8_pt", "weight")
    ttbarAK8Pt = ttbar_metCut.Histo1D(("ttbarAK8Pt", ";p_{T} (GeV)", 50, 0, 1600.0), "AK8_pt", "weight")
    GJetsAK8Pt = GJets_metCut.Histo1D(("GJetsAK8PtHist", "AK8 p_{T};p_{T} (GeV)", 50, 0, 1600.0 ), "AK8_pt", "weight")

    sigAK8eta = signal_metCut.Histo1D(("sigAK8eta", ";#eta", 60, -3.0, 3.0), "AK8_eta", "weight")
    ttbarAK8eta = ttbar_metCut.Histo1D(("ttbarAK8eta", ";#eta", 60, -3.0, 3.0), "AK8_eta", "weight")
    GJetsAK8eta = GJets_metCut.Histo1D(("GJetsAK8eta", "AK8 #eta;AK8 #eta", 60, -3.0, 3.0), "AK8_eta", "weight")

    sigAK8SDM = signal_metCut.Histo1D(("sigAK8SDM", ";Soft DropMass (GeV)", 50, 0, 200.0), "AK8_msoftdrop", "weight")
    ttbarAK8SDM = ttbar_metCut.Histo1D(("ttbarAK8SDM", ";Soft Drop Mass (GeV)", 50, 0.0, 200.0), "AK8_msoftdrop", "weight")
    GJetsAK8SDM = GJets_metCut.Histo1D(("GJetsAK8SDM", "AK8 Soft Drop Mass;Soft Drop Mass (GeV)", 50, 0.0, 200.0), "AK8_msoftdrop", "weight")

    sigAK8N2 = signal_metCut.Histo1D(("sigAK8N2", ";N2", 50, 0.0, .5), "AK8_n2", "weight")
    ttbarAK8N2 = ttbar_metCut.Histo1D(("ttbarAK8N2", ";N2", 50, 0.0, .5), "AK8_n2", "weight")
    GJetsAK8N2 = GJets_metCut.Histo1D(("GJetsAK8N2", "N2 ;N2", 50, 0.0, .5), "AK8_n2", "weight")

    sigPt = signal_metCut.Histo1D(("sigPt", ";Photon p_{T} (GeV)", 50, 0.0, 1600.), "Photon_pt", "weight")
    ttbarPt = ttbar_metCut.Histo1D(("ttbarPt", ";Photon p_{T} (GeV)", 50, 0.0, 1600.), "Photon_pt", "weight")
    GJetsPt = GJets_metCut.Histo1D(("GJetsPt", "Photon p_{T}; Photon p_{T} (GeV)", 50, 0.0, 1600.), "Photon_pt", "weight")

    sigEta = signal_metCut.Histo1D(("sigEta", ";Photon #eta", 60, -3.0, 3.0), "Photon_eta", "weight")
    ttbarEta = ttbar_metCut.Histo1D(("ttbarEta", ";Photon #eta", 60, -3.0, 3.0), "Photon_eta", "weight")
    GJetsEta = GJets_metCut.Histo1D(("GJetsEta", "Photon #eta; Photon #eta", 60, -3.0, 3.0), "Photon_eta", "weight")

    histDraw(sigAK8Pt, ttbarAK8Pt, GJetsAK8Pt, "AK8 pT" + cut, out)
    histDraw(sigAK8eta, ttbarAK8eta, GJetsAK8eta, "AK8 Eta" + cut, out)
    histDraw(sigAK8SDM, ttbarAK8SDM, GJetsAK8SDM, "AK8 SDM" + cut, out)
    histDraw(sigAK8N2, ttbarAK8N2, GJetsAK8N2, "AK8 N2" + cut, out)
    histDraw(sigPt, ttbarPt, GJetsPt, "Photon pT" + cut, out)
    histDraw(sigEta, ttbarEta, GJetsEta, "Photon Eta" + cut, out)

