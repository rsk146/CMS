import ROOT
from ROOT import *
import os
import sys
import math

class histDraw:
    def __init__(self, sig, ttbar, gjet, var, out):
        C = ROOT.TCanvas(var, var)
        C.cd()
        p1 = ROOT.TPad("pad1", "tall", 0, 0.325, 1, 1)
        p2 = ROOT.TPad("pad2", "short", 0, 0.0, 1.0, 0.35)
        p2.SetBottomMargin(0.35)
        p1.Draw()
        p2.Draw()
        p1.SetLogy()

        #top
        p1.cd() 
        ROOT.gPad.SetTicks(1,1)

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
        p1.RedrawAxis()


        #bottom
        p2.cd() 
        ROOT.gPad.SetTicks(1,1)
        s_over_rootb = ttbar.Clone("s/rootb")
        s_over_rootb.Reset()
        s_over_rootb.SetStats(0)
        s_over_rootb.SetLineColor(kBlack)
        s_over_rootb.SetFillColor(kWhite)
        for bin in range(ttbar.GetNbinsX()):
            if ttbar.GetBinContent(bin+1) == 0 and gjet.GetBinContent(bin+1) == 0: continue
            print("Signal Val: " + str(sig.GetBinContent(bin+1)) + " ttbar Val: " + str(ttbar.GetBinContent(bin+1)) + " gjets Val: " + str(gjet.GetBinContent(bin+1)))
            s_over_rootb_val = sig.GetBinContent(bin+1)/math.sqrt(ttbar.GetBinContent(bin+1) + gjet.GetBinContent(bin+1))
            print "S/sqrtB: " + str(s_over_rootb_val)
            s_over_rootb.SetBinContent(bin+1, s_over_rootb_val)
        s_over_rootb.GetYaxis().SetTitle("s/rootb")
        s_over_rootb.SetTitleSize(.07, "y")
        s_over_rootb.GetXaxis().SetTitle("")
        s_over_rootb.GetXaxis().SetTitleSize(0.1925)
        s_over_rootb.GetXaxis().SetLabelSize(0.16)
        s_over_rootb.GetXaxis().SetTitleOffset(0.84)
        s_over_rootb.GetYaxis().SetLabelSize(.05)
        s_over_rootb.GetXaxis().SetLabelSize(.07)
        s_over_rootb.Draw("hist")
        p2.RedrawAxis()

        #save
        C.Update()
        C.Modified()
        out.cd()
        C.Write()
    
def Hist_Setup(signal_metCut, ttbar_metCut, GJets_metCut, cut):
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

if __name__ == "__main__":

    out = ROOT.TFile("Preselections_sOverRootb.root", "RECREATE")
    ROOT.ROOT.EnableImplicitMT()
    RDF = ROOT.ROOT.RDataFrame

    ttbar = RDF("tree", sys.argv[1])
    signal = RDF("tree", sys.argv[2])
    gjets = RDF("tree", sys.argv[3])

    ttbar_nopt = ttbar.Filter("MET < 75 && AK4_csv < .55 && AK8_tau32 > .5")
    signal_nopt = signal.Filter("MET < 75 && AK4_csv < .55 && AK8_tau32 > .5")
    gjets_nopt = gjets.Filter("MET < 75 && AK4_csv < .55 && AK8_tau32 > .5")
    ttbar_n = ttbar_nopt.Histo1D(("ttbar", "", 50, 0., 800.0), "AK4_pt", "weight")
    signal_n = signal_nopt.Histo1D(("signal", "", 50, 0., 800.0), "AK4_pt", "weight")
    gjets_n = gjets_nopt.Histo1D(("gjets", "AK4 p_{T}; AK4 p_{T} (GeV)", 50, 0., 800.0), "AK4_pt", "weight")
    histDraw(signal_n, ttbar_n, gjets_n, "N-1: AK4 pT", out)
    Hist_Setup(signal_nopt, ttbar_nopt, gjets_nopt, " No pT Cut")
    
    ttbar_nomet = ttbar.Filter("AK4_csv < .55 && AK8_tau32 > .5 && AK4_pt < 50")
    signal_nomet = signal.Filter("AK4_csv < .55 && AK8_tau32 > .5 && AK4_pt < 50")
    gjets_nomet = gjets.Filter("AK4_csv < .55 && AK8_tau32 > .5 && AK4_pt < 50")
    ttbar_n = ttbar_nomet.Histo1D(("ttbar", "", 50, 0., 500.0), "MET", "weight")
    signal_n = signal_nomet.Histo1D(("signal", "", 50, 0., 500.0), "MET", "weight")
    gjets_n = gjets_nomet.Histo1D(("gjets", "MET; MET (GeV)", 50, 0., 500.0), "MET", "weight")
    histDraw(signal_n, ttbar_n, gjets_n, "N-1: MET", out)
    Hist_Setup(signal_nomet, ttbar_nomet, gjets_nomet, " No MET Cut")
    
    ttbar_nocsv = ttbar.Filter("MET < 75 && AK8_tau32 > .5 && AK4_pt < 50")
    signal_nocsv = signal.Filter("MET < 75 && AK8_tau32 > .5 && AK4_pt < 50")
    gjets_nocsv = gjets.Filter("MET < 75 && AK8_tau32 > .5 && AK4_pt < 50")
    ttbar_n = ttbar_nocsv.Histo1D(("ttbar", "", 50, 0., 1), "AK4_csv", "weight")
    signal_n = signal_nocsv.Histo1D(("signal", "", 50, 0., 1.0), "AK4_csv", "weight")
    gjets_n = gjets_nocsv.Histo1D(("gjets", "AK4 bTag; AK4 bTag", 50, 0., 1.0), "AK4_csv", "weight")
    histDraw(signal_n, ttbar_n, gjets_n, "N-1: bTag", out)
    Hist_Setup(signal_nocsv, ttbar_nocsv, gjets_nocsv, " No btag Cut")

    ttbar_notau = ttbar.Filter("MET < 75 && AK4_csv < .55 && AK4_pt < 50")
    signal_notau = signal.Filter("MET < 75 && AK4_csv < .55 && AK4_pt < 50")
    gjets_notau = gjets.Filter("MET < 75 && AK4_csv < .55 && AK4_pt < 50")
    ttbar_n = ttbar_notau.Histo1D(("ttbar", "", 50, 0., 1), "AK8_tau32", "weight")
    signal_n = signal_notau.Histo1D(("signal", "", 50, 0., 1.0), "AK8_tau32", "weight")
    gjets_n = gjets_notau.Histo1D(("gjets", "AK8 tau32; AK8 tau32", 50, 0., 1.0), "AK8_tau32", "weight")
    histDraw(signal_n, ttbar_n, gjets_n, "N-1: tau32", out)
    Hist_Setup(signal_notau, ttbar_notau, gjets_notau, " No tau32 Cut")
    
    ttbar_all = ttbar.Filter("MET < 75 && AK4_csv < .55 && AK4_pt < 50 && AK8_tau32 > .5")
    signal_all = signal.Filter("MET < 75 && AK4_csv < .55 && AK4_pt < 50 && AK8_tau32 > .5")
    gjets_all = gjets.Filter("MET < 75 && AK4_csv < .55 && AK4_pt < 50 && AK8_tau32 > .5")

    Hist_Setup(signal_all, ttbar_all, gjets_all, " All Cuts")