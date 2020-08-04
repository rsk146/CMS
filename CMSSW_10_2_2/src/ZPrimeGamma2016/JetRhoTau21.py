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
            h4 = TH2F("Tau_{21}10%", "Tau21; Jet #rho; Jet p_{T}", 16, -7., -2., 16, 200., 800.) 
            G = TFile(File2)
            h2 = TH1F()
            G.GetObject("BGFatJetTau21", h2)
            self.File.cd()
            ptCounter = 200.
            rhoCounter =  -6.6875
            while(ptCounter <= 800.):
                  while(rhoCounter < -2):
                        h3 = TH1F("Tau21Effic", "Tau21 with Cuts; #tau_{2}/#tau_{1}; Events", 50, 0., 1.)
                        self.FillHist(File1, h3, rhoCounter, ptCounter)
                        h3.Divide(h2)
                        diff = abs(h3.GetBinContent(0) - .1)
                        binRight = 0
                        for i in range(45):
                              currDiff = abs(h3.GetBinContent(i) - .1)
                              if currDiff <= .01 and currDiff <= diff:
                                    diff = currDiff
                                    binRight = i
                        h4.Fill(rhoCounter, ptCounter, binRight*50.)
                        rhoCounter += .3125
                  ptCounter +=37.5
            self.File.cd()
            h4.Write()
      def __book__(self,name):
            self.File = ROOT.TFile(self.name + ".root", "RECREATE")
            self.File.cd()
      def FillHist(self, File, h1, maxRho, maxPt):
            F = TFile(File)
            self.T = F.Get("tree")
            for e in self.T:
                  if self.T.FatJet_rho <maxRho  and self.T.FatJet_rho > maxRho - .3125:
                        if self.T.FatJet_pt > maxPt - 37.5 and self.T.FatJet_pt < maxPt:
                              h1.Fill(self.T.FatJet_tau21, self.T.weight*36)
            F.Close()      


newDiv = EfficiencyTester("Tau212dArrayTest", "/users/h2/rsk146/CMSSW_10_2_2/src/ZPrimeGamma2016/HT100toInf.root", "/users/h2/rsk146/CMSSW_10_2_2/src/ZPrimeGamma2016/BGHist.root")
