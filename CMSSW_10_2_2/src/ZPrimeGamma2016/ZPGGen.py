import ROOT
import os
from ROOT import *
from array import array
import math
from math import *
import sys
import glob
import csv

class HistGen:
    def __init__(self, name, File1): 
        self.name = name
        self.F = File1
        self.__book__(name)
        h1 = TH2F("MassvsRho","Jet Mass vs Rho; FatJet #rho; FatJet mass", 20, -8., -1., 50, 0., 250.)
        h2 = TH1F("PhotonPt", "Photon Pt; Photon P_t; Events", 50, 0., 1000.)
        h3 = TH1F("PhotonEta", "Photon Eta; Photon #eta; Events", 60, -3., 3.)
        h4 = TH1F("FatJetRho", "Leading AK8 Rho; Leading AK8 #rho; Events", 65, -8., -1.5)
        h5 = TH1F("FatJetPt", "Leading AK8 Pt; Leading AK8 P_t; Events", 50, 0., 1400.)
        h6 = TH1F("FatJetEta", "Leading AK8 Eta; Leading AK8 #eta; Events", 60, -3., 3.)
        h7 = TH1F("FatJetSDM", "Leading AK8 Soft Drop Mass; Leading AK8 Soft Drop Mass [GeV]; Events", 50, 0., 200.)
        h8 = TH1F("FatJetTau21", "Leading AK8 Tau21; Leading AK8 #tau_2/#tau_1; Events", 50, 0., 1.)
        self.FillHist(File1, h1, h2, h3, h4, h5, h6, h7, h8)
        self.File.Write()
    def __book__(self, name):
        self.File = ROOT.TFile(self.name + ".root", "RECREATE")
        self.File.cd()
    def FillHist(self, File, h1, h2, h3, h4, h5, h6, h7, h8):
        F = TFile(File)
        self.T = F.Get("tree")
        for e in self.T:
           h1.Fill(self.T.FatJet_rho, self.T.FatJet_mass, self.T.weight*36.)
           h2.Fill(self.T.Photon_pt, self.T.weight*36.)
           h3.Fill(self.T.Photon_eta, self.T.weight*36.)
           h4.Fill(self.T.FatJet_rho, self.T.weight*36.)
           h5.Fill(self.T.FatJet_pt, self.T.weight*36.)
           h6.Fill(self.T.FatJet_eta, self.T.weight*36.)
           h7.Fill(self.T.FatJet_msoftdrop, self.T.weight*36.)
           h8.Fill(self.T.FatJet_tau21, self.T.weight*36.)
        F.Close()

Hist = HistGen("Zp75Hist", "/users/h2/rsk146/CMSSW_10_2_2/src/ZPrimeGamma2016/TestTreeLoops.root")

