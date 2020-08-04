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
            h5 = TH2F("N2EffPtRho", "N2EffPtRho", 16, -7., -2., 16, 120., 720.)
            pTCounter = 157.5
            while(pTCounter <= 720.):
                rhoCounter = -6.6875
                while(rhoCounter <= -2.):
                    h3 = TH1F("N2Effic", "N2 with Cuts; N2; Events", 50, 0., .5)
                    self.FillHist(File1, h3, pTCounter, rhoCounter)
                    self.File.cd()
                    #h3.Write()
                    total = h3.Integral()
                    bin = 1
                    while(bin < 50):
                        num = h3.Integral(0, bin)
                        if num / total > .1:
                            binRight = bin
                            break
                        bin+=1
                    h5.Fill(rhoCounter - .3125, pTCounter - 37.5, binRight/100.)
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
                  if self.T.AK8_pt < maxpt  and self.T.AK8_pt > maxpt - 37.5:
                      if self.T.AK8_rho < maxrho and self.T.AK8_rho > maxrho -.3125:
                            h1.Fill(self.T.AK8_n2, self.T.weight*36)
            F.Close()


newDiv = EfficiencyTester("N210%", "/users/h2/rsk146/JTTest/CMSSW_10_2_15/src/N2DDT/GJetsHT100toInf.root")
