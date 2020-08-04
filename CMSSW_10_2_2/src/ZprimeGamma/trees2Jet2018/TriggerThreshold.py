import ROOT
import os
from ROOT import *
from array import array
import math
from math import *
import sys
import glob
import csv

class TriggerThreshold:
    def __init__(self, name, File1, File2):
        self.name = name
        self.File1 = File1
        self.File2 = File2
        self.__book__(name)
        #self.File3 = ROOT.TFile(self.name + ".root", "RECREATE")
        #self.File3.cd()
        h1 = TH1F("Photon110LeadingJets", "Photon110LeadingJets", 50, 0, 1000)
        h2 = TH1F("NoTriggerLeadingJets", "NoTriggerLeadingJets", 50, 0, 1000)
        h3 = TH1F("Photon110LeadingJetsTurnOn", "Photon110LeadingJetsTurnOn", 50, 0, 1000)
        self.FillHist(File1, h1)
        self.FillHist(File2, h2)
        self.FillHist(File1, h3)
        h3.Divide(h2)
        self.File3.Write()
        
        #self.File3.Close()
        

    def FillHist(self, File, hist):
        F = TFile(File)
        self.T = F.Get("tree")
        for e in self.T:
          #  if(abs(self.T.Photon_eta) < 1.44):
                hist.Fill(self.T.HadronicHT, self.T.weight)
        F.Close()
        
    def __book__(self, name):
        self.File3 = ROOT.TFile(self.name + ".root", "RECREATE")
        self.File3.cd()
        



    
newDivision = TriggerThreshold("NewTrigger2JetNo100BinAnalysis", "/users/h2/rsk146/CMSSW_10_2_2/src/ZprimeGamma/trees2Jet2018/GJets_HT100toInf_added.root", "/users/h2/rsk146/CMSSW_10_2_2/src/ZprimeGamma/treesNoCut2Jet2018/GJets_HT200toInf_NoCut_added.root")

