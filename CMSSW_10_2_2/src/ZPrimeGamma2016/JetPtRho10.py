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
      def __init__(self, name, File1):
            self.name = name
            self.F = File1
            self.__book__(name)
            h5 = TH2F("Tau21EffPtRho", "Tau21EffPtRho", 16, -7., -2., 16, 200., 800.)
            pTCounter = 237.5
            while(pTCounter <= 800.):
                rhoCounter = -6.6875
                while(rhoCounter <= -2.):
                    h3 = TH1F("Tau21Effic", "Tau21 with Cuts; #tau_{2}/#tau_{1}; Events", 50, 0., 1.)
                    self.FillHist(File1, h3, pTCounter, rhoCounter)
                    self.File.cd()
                    h3.Write()
                    total = h3.Integral()
                    bin = 1
                    while(bin < 50):
                        num = h3.Integral(0, bin)
                        if num / total > .1:
                            binRight = bin
                            break
                        bin+=1
                    h5.Fill(rhoCounter - .3125, pTCounter - 37.5, binRight/50.)
                    rhoCounter+=.3125
                pTCounter+=37.5
            self.File.cd()
            h5.Write()
      def __book__(self,name):
            self.File = ROOT.TFile(self.name + ".root", "RECREATE")
            self.File.cd()
      def FillHist(self, File, h1, maxpt, maxrho):
            F = TFile(File)
            self.T = F.Get("tree")
            for e in self.T:
                  if self.T.FatJet_pt < maxpt  and self.T.FatJet_pt > maxpt - 37.5:
                      if self.T.FatJet_rho < maxrho and self.T.FatJet_rho > maxrho -.3125:
                            h1.Fill(self.T.FatJet_tau21, self.T.weight*36)
            F.Close()


newDiv = EfficiencyTester("Tau21TwoD", "/users/h2/rsk146/CMSSW_10_2_2/src/ZPrimeGamma2016/HT100toInf.root")
