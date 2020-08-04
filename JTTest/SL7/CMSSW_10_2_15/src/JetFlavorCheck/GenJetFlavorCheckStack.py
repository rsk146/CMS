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
    def __init__(self, name, File1):
        self.name = name
        self.File1 = File1
        self.__book__(name)
        hist = TH1F("NConst", "nCons; nCons; Events", 50, 0, 100)
        h1 = TH1F("One", "One; nCons; Events", 50, 0, 100)
        h2 = TH1F("Two", "Two; nCons; Events", 50, 0, 100)
        h3 = TH1F("Three", "Three Four and Five; nCons; Events", 50, 0, 100)
        h4 = TH1F("Four", "Four; nCons; Events", 50, 0, 100)
        h5 = TH1F("Five", "Five; nCons; Events", 50, 0, 100)
        h6 = TH1F("TwentyOne", "TwentyOne; nCons; Events", 50, 0, 100)
        h7 = TH1F("Zero", "Zero; nCons; Events", 50, 0, 100)
        h8 = TH1F("None", "none; nCons; Events", 50, 0, 100)
        h12 = TH1F("211","", 50, 0, 100)
        h21 = TH1F("Twenty1One","",50,0,100)
        self.FillNoCut(File1, hist)
        self.FillHist(File1, h1, 1)
        self.FillHist(File1, h2, 2)
        self.FillHist(File1, h3, 3)
        self.FillHist(File1, h4, 4)
        self.FillHist(File1, h5, 5)
        self.FillHist(File1, h6, 21)
        self.FillHist(File1, h7, 0)
        self.FillHist(File1, h12, 21)
        self.FillHist(File1, h21, 21)
        h21.Add(h1)
        h12.Add(h1)
        self.File3.Write()
        self.File3.cd()
        h12.Add(h2)
        h12.Write("21,1,2")
        h12.Add(h3)
        h12.Write("21,1,2,3")
        h12.Add(h4)
        h12.Write("21,1,2,3,4")
        h12.Add(h5)
        h12.Write("21,1,2,3,4,5")

    def FillHist(self, File, hist, flavor):
        F = TFile(File)
        self.T = F.Get("tree")
        for e in self.T:
            if abs(self.T.AK8_JetFlavor) == flavor:
                hist.Fill(self.T.AK8_msoftdrop, self.T.weight)
        F.Close()
    
    def FillNoCut(self, File, hist):
        F = TFile(File)
        self.T = F.Get("tree")
        for e in self.T:
            hist.Fill(self.T.AK8_msoftdrop, self.T.weight)
        F.Close()
        
    def __book__(self, name):
        self.File3 = ROOT.TFile(self.name + ".root", "RECREATE")
        self.File3.cd()
        



    
newDivision = TriggerThreshold("ttbarFlavorCuts", "ttbar2018FlavorTreeCuts.root")
