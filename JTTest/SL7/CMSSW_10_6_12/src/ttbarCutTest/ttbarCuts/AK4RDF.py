import ROOT
from ROOT import *
import os
import sys

class histDraw:
    def __init__(self, ttbar, signal, gjet, out, canvas):
        C = ROOT.TCanvas(canvas, canvas)
        C.cd()

        ttbar.SetLineColor(kGreen)
        ttbar.SetFillColor(kGreen)
        ttbar.SetFillStyle(3001)
        ttbar.SetLineWidth(2)
        ttbar.Scale(1.0/ttbar.Integral())
        ttbar.SetStats(0)
        ttbar.Draw("hist")
        
        gjet.SetLineColor(kBlue)
        gjet.SetFillColor(kAzure-9)
        gjet.SetFillStyle(3001)
        gjet.SetLineWidth(2)
        gjet.Scale(1.0/gjet.Integral())
        gjet.SetStats(0)
        gjet.Draw("hist same")

        signal.SetLineColor(kRed)
        signal.SetLineWidth(3)
        signal.Scale(1.0/signal.Integral())
        signal.SetStats(0)
        signal.Draw("hist same")

        legend = TLegend(.7, .8, .9, .9)
        legend.AddEntry(gjet.GetValue(), "#gamma+jetsMC", "f")
        legend.AddEntry(ttbar.GetValue(), "ttbar", "f")
        legend.AddEntry(signal.GetValue(), "Z'_{10GeV}", "l")
        legend.Draw()

        C.Update()
        C.Modified()
        out.cd()
        C.Write()

if __name__ == "__main__":
    if "AK8" in sys.argv[1]:
        out = ROOT.TFile("AK4AK8.root", "RECREATE")
    else:
        out = ROOT.TFile("AK4Photon.root", "RECREATE")
    ROOT.ROOT.EnableImplicitMT()
    RDF = ROOT.ROOT.RDataFrame

    ttbar = RDF("tree", sys.argv[1])
    signal = RDF("tree", sys.argv[2])
    gjets = RDF("tree", sys.argv[3])

    deltaR = ttbar.Histo1D(("deltaR Photon and AK4", "deltaR Photon and Closest AK4; #Deltar #gamma AK4", 50, 0.0, 4.0), "AK4_Photon_deltaR", "weight")
    deltaEta = ttbar.Histo1D(("deltaEta Photon and AK4", "delta Eta Photon and Closest AK4; #Delta#eta #gamma AK4", 50, 0.0, 4.0), "AK4_Photon_deltaEta", "weight")
    csv = ttbar.Histo1D(("CSV", "CSV", 50, 0.0, 2.0), "AK4_csv", "weight")
    DR = ttbar.Histo1D(("deltaR AK8 and AK4", "deltaR AK8 and AK4; #Deltar AK8 AK4", 50, 0.0, 4.0), "AK4_AK8_deltaR", "weight")
    DE = ttbar.Histo1D(("deltaEta AK8 and AK4", "delta Eta AK8 and AK4; #Delta#eta AK8 AK4", 50, 0.0, 4.0), "AK4_AK8_deltaEta", "weight")
    mass = ttbar.Histo1D(("mass", "AK4 Mass; AK4 Mass (GeV)", 50, 0.0, 100.0), "AK4_mass", "weight")
    MET = ttbar.Histo1D(("MET", "MET; MET (GeV)", 50, 0.0, 500.0), "MET", "weight")

    sigdeltaR = signal.Histo1D(("deltaR Photon and AK4", "deltaR Photon and Closest AK4; #Deltar #gamma AK4", 50, 0.0, 4.0), "AK4_Photon_deltaR", "weight")
    sigdeltaEta = signal.Histo1D(("deltaEta Photon and AK4", "delta Eta Photon and Closest AK4; #Delta#eta #gamma AK4", 50, 0.0, 4.0), "AK4_Photon_deltaEta", "weight")
    sigcsv = signal.Histo1D(("CSV", "CSV", 50, 0.0, 2.0), "AK4_csv", "weight")
    sigDR = signal.Histo1D(("deltaR AK8 and AK4", "deltaR AK8 and AK4; #Deltar AK8 AK4", 50, 0.0, 4.0), "AK4_AK8_deltaR", "weight")
    sigDE = signal.Histo1D(("deltaEta AK8 and AK4", "delta Eta AK8 and AK4; #Delta#eta AK8 AK4", 50, 0.0, 4.0), "AK4_AK8_deltaEta", "weight")
    sigmass = signal.Histo1D(("mass", "AK4 Mass; AK4 Mass (GeV)", 50, 0.0, 100.0), "AK4_mass", "weight")
    sigMET = signal.Histo1D(("MET", "MET; MET (GeV)", 50, 0.0, 500.0), "MET", "weight")

    gjetsdeltaR = gjets.Histo1D(("deltaR Photon and AK4", "deltaR Photon and Closest AK4; #Deltar #gamma AK4", 50, 0.0, 4.0), "AK4_Photon_deltaR", "weight")
    gjetsdeltaEta = gjets.Histo1D(("deltaEta Photon and AK4", "delta Eta Photon and Closest AK4; #Delta#eta #gamma AK4", 50, 0.0, 4.0), "AK4_Photon_deltaEta", "weight")
    gjetscsv = gjets.Histo1D(("CSV", "CSV", 50, 0.0, 2.0), "AK4_csv", "weight")
    gjetsDR = gjets.Histo1D(("deltaR AK8 and AK4", "deltaR AK8 and AK4; #Deltar AK8 AK4", 50, 0.0, 4.0), "AK4_AK8_deltaR", "weight")
    gjetsDE = gjets.Histo1D(("deltaEta AK8 and AK4", "delta Eta AK8 and AK4; #Delta#eta AK8 AK4", 50, 0.0, 4.0), "AK4_AK8_deltaEta", "weight")
    gjetsmass = gjets.Histo1D(("mass", "AK4 Mass; AK4 Mass (GeV)", 50, 0.0, 100.0), "AK4_mass", "weight")
    gjetsMET = gjets.Histo1D(("MET", "MET; MET (GeV)", 50, 0.0, 500.0), "MET", "weight")

    histDraw(deltaR, sigdeltaR, gjetsdeltaR, out, "deltaR Photon and AK4")
    histDraw(deltaEta, sigdeltaEta, gjetsdeltaEta, out, "deltaEta Photon and AK4")
    histDraw(csv, sigcsv, gjetscsv, out, "csv")
    histDraw(DR, sigDR, gjetsDR, out, "deltaR AK8 and AK4")
    histDraw(DE, sigDE, gjetsDE, out, "deltaEta AK8 and AK4")
    histDraw(mass, sigmass, gjetsmass, out, "AK4 mass")
    histDraw(MET, sigMET, gjetsMET, out, "MET")

