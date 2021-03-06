import ROOT
import os
from ROOT import *
from array import array
import math
from math import*
import sys
import glob
import csv
import ctypes
from ctypes import*

class EfficiencyTester:
      def __init__(self, name, File1, File2):
            self.name = name
            self.F = File1
            self.__book__(name)
            h5 = TH1F("Tau21EffPt", "Tau21EffPt", 16, 200., 800.)
            G = TFile(File2)
            h2 = TH1F()
            G.GetObject("BGFatJetTau21", h2)
            pTCounter = 237.5
            while(pTCounter <= 800.):
                h3 = TH1F("Tau21Effic", "Tau21 with Cuts; #tau_{2}/#tau_{1}; Events", 50, 0., 1.)
                self.FillHist(File1, h3, pTCounter)
                h3.Divide(h2)
                self.File.cd()
                h3.Write()
                diff = abs(h3.GetBinContent(0) - .1)
                binRight = 0
                for i in range(30):
                      currDiff = abs(h3.GetBinContent(i) - .1)
                      if currDiff <= .08 and currDiff <= diff:
                            diff = currDiff
                            binRight = i
                            if binRight < 25 and binRight > 5:
                                break
                print binRight/50.
                print pTCounter
                h5.Fill(pTCounter - 37.5, binRight/50.)
                pTCounter += 37.5
            self.File.cd()
            h5.Write()
      def __book__(self,name):
            self.File = ROOT.TFile(self.name + ".root", "RECREATE")
            self.File.cd()
      def FillHist(self, File, h1, maxpt):
            F = TFile(File)
            self.T = F.Get("tree")
            for e in self.T:
                  if self.T.FatJet_pt < maxpt  and self.T.FatJet_pt > maxpt - 37.5:
                        h1.Fill(self.T.FatJet_tau21, self.T.weight*36)
            F.Close()


newDiv = EfficiencyTester("Tau21PtHistoTest", "/users/h2/rsk146/CMSSW_10_2_2/src/ZPrimeGamma2016/HT100toInf.root", "/users/h2/rsk146/CMSSW_10_2_2/src/ZPrimeGamma2016/BGHist.root")
