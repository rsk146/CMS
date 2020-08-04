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
            percent = .1
            h1 = TH2F("JetRhoN2", "JetRho to N2; Jet Rho; N2", 16, -7., -2.0, 16, 0., .5)
            self.FillTwoD(File1, h1) 
            self.File.cd()
            h1.Write()
            while(percent <=.9):
                h5 = TH1F("N2EffRho", "N2EffRho", 16, -7., -2.0)
                sdmCounter = -6.6875
                while(sdmCounter <= 2.):
                    h3 = TH1F("N2Effic", "N2 with Cuts; N2; Events", 50, 0., .5)
                    self.FillHist(File1, h3, sdmCounter)
                    total = h3.Integral()
                    print total
                    bin = 1
                    while(bin < 50):
                        num = h3.Integral(1, bin)
                        print num
                        if num / total > percent:
                            binRight = bin
                            break
                        bin+=1
                    print binRight
                    print sdmCounter
                    h5.Fill(sdmCounter - .3125, binRight/100.)
                    sdmCounter+=.3125
                percent += .1
                self.File.cd()
                h5.Write()
      def __book__(self,name):
            self.File = ROOT.TFile(self.name + ".root", "RECREATE")
            self.File.cd()
      def FillHist(self, File, h1, maxsdm):
            F = TFile(File)
            self.T = F.Get("tree")
            for e in self.T:
                  if self.T.AK8_rho < maxsdm  and self.T.AK8_rho > maxsdm - .3125:
                        h1.Fill(self.T.AK8_n2, self.T.weight*36)
      def FillTwoD(self, File, h1):
            F = TFile(File)
            self.T = F.Get("tree")
            for e in self.T:
                  if self.T.AK8_rho >-7. and self.T.AK8_rho <-2.:
                        h1.Fill(self.T.AK8_rho, self.T.AK8_n2, self.T.weight*36)
            F.Close()
newDiv = EfficiencyTester("N2Rho", "/users/h2/rsk146/JTTest/CMSSW_10_2_15/src/N2DDT/GJetsHT100toInf.root")
