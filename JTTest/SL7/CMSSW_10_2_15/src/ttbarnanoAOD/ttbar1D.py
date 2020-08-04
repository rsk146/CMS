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
        #h1 = TH2F("MassVsRho","Jet Mass vs Rho; FatJet #rho; FatJet mass", 20, -8., -1., 50, 0., 250.)
        h2 = TH1F("PhotonPt", "Photon P_{t}; Photon P_{t} [GeV]; Events per 50 GeV Bin", 50, 0., 1600.)
        h3 = TH1F("PhotonEta", "Photon Eta; Photon #eta; Events per 60 Bin", 60, -3., 3.)
        #h4 = TH1F("AK8Rho", " AK8 Rho; Leading AK8 #rho; Events per 65 Bin", 65, -8, -1.5)
        h5 = TH1F("AK8Pt", " Ak8 P_{t}; Leading AK8 P_{t} [GeV]; Events per 50 GeV Bin", 50, 0., 1600.)
        h6 = TH1F("AK8Eta", " AK8 Eta; Leading AK8 #eta; Events per 60 Bin", 60, -3., 3.)
        h7 = TH1F("AK8SDM", "AK8 Soft Drop Mass; Leading AK8 Soft Drop Mass [GeV]; Events per 50 Bin", 50, 0., 200.)
        h8 = TH1F("AK8N2", "AK8 N2; Leading AK8 N_{2}; Events", 50, 0., .5)
        #h9 = TH2F("N2Rho", "Jet Rho vs N2; Jet #rho; N2", 25, -8.,-1., 25, 0., .5)
        #h10 = TH2F("N2Pt", "Jet pt vs N2; Jet p_{t}; N2", 16, 200., 800., 30, 0., .5) 
        #h11 = TH2F("N2SDM", "Jet SDM vs N2; Jet mass soft drop; N2", 16, 0., 250., 30, 0., .5)
        self.FillHist(File1, h2, h3, h5, h6, h7, h8)
        self.File.Write()
    def __book__(self, name):
        self.File = ROOT.TFile(self.name + ".root", "RECREATE")
        self.File.cd()
    def FillHist(self, File, h2, h3, h5, h6, h7, h8):
        F = TFile(File)
        self.T = F.Get("tree")
        for e in self.T:
           #h1.Fill(self.T.AK8_rho, self.T.AK8_mass, self.T.weight*36. )
           h2.Fill(self.T.Photon_pt, self.T.weight*36.)
           h3.Fill(self.T.Photon_eta, self.T.weight*36.)
           #h4.Fill(self.T.AK8_rho, self.T.weight*36.)
           h5.Fill(self.T.AK8_pt, self.T.weight*36.)
           h6.Fill(self.T.AK8_eta, self.T.weight*36.)
           h7.Fill(self.T.AK8_msoftdrop, self.T.weight*36.)
           h8.Fill(self.T.AK8_n2, self.T.weight*36.)
           #h9.Fill(self.T.AK8_rho, self.T.AK8_tau21, self.T.weight*36.)
           #h10.Fill(self.T.AK8_pt, self.T.AK8_tau21, self.T.weight*36.)
           #h11.Fill(self.T.AK8_msoftdrop, self.T.AK8_tau21, self.T.weight*36)
        F.Close()

#Hist = HistGen("Zp75Hist", "/users/h2/rsk146/CMSSW_10_2_2/src/ZPrimeGamma2016/TestTreeMaker.root")
Hist2 = HistGen("ttbarPreselection1D", "/users/h2/rsk146/JTTest/SL7/CMSSW_10_2_15/src/ttbarnanoAOD/ttbar2018PreselectionTree.root")
