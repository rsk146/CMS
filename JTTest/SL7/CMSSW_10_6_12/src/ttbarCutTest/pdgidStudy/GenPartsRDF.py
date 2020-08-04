import ROOT
from ROOT import *
import os
import sys

def histDraw(var, out, photon = None, ak8 = None):
    C = ROOT.TCanvas(var, var)
    C.cd()
    if ak8:
        ak8.SetLineColor(kBlue)
        ak8.SetFillColor(kAzure-9)
        ak8.Draw("hist")
        ak8.SetStats(0)

    if photon:
        photon.SetLineColor(kMagenta)
        photon.SetFillColor(kMagenta-9)
        photon.SetStats(0)
        photon.Draw("hist")

    C.Update()
    C.Modified()
    out.cd()
    C.Write()

out = ROOT.TFile("GenParts.root", "RECREATE")
ROOT.ROOT.EnableImplicitMT()
RDF = ROOT.ROOT.RDataFrame

ttbar = RDF("tree", sys.argv[1])
photonpdgID = ttbar.Histo1D(("Matched Photon pdgID", "Photon PDGID", 50, 0, 30), "photon_pdgId", "weight")
ak8pdgID = ttbar.Histo1D(("Matched AK8 pdgID", "AK8 PDGID", 50, 0, 700), "ak8_pdgId", "weight")
photonStatus = ttbar.Histo1D(("Matched Photon Status Code", "Photon Status Codes", 50, 0, 25), "PhotonStatus", "weight")
ak8Status = ttbar.Histo1D(("Matched ak8 Status Code", "AK8 Status Codes", 50, 0, 80), "AK8Status", "weight")

histDraw("Photon PDGID", out, photon = photonpdgID)
histDraw("AK8 PDGID", out, ak8 = ak8pdgID)
histDraw("Photon Status Codes", out, photon = photonStatus)
histDraw("AK8 Status Codes", out, ak8 = ak8Status)