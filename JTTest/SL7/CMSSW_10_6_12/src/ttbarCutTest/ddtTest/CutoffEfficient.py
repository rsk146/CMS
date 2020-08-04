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
import numpy as np

class Cutoffs:
    def __init__(self, name, File1, hists, plot):
        self.binRight = -1
        self.name = name
        self.F = File1
        self.__book__(name)
        self.cutoffHist = TH2F("Cutoffs" + plot, "N2EffPtRho", 16, -7., -2., 16, 100., 1600.)
        compareHist = TH2F("N2", "N2", 16, -7, -2, 16, 100, 1600)
        self.FillHist(File1, compareHist)
        self.FillHists(File1, hists)
        self.File.cd()
        compareHist.Write()
        for i in range(16):
            for j in range(16):
                currHist = hists[i][j]
                total = currHist.Integral()
                if total == 0:
                    #print ("(%d, %d) Total =  %d" % (i, j, total))
                    continue
                for bin in range(1, 50):
                    num = currHist.Integral(0, bin)
                    if num/total > .1:
                        self.binRight = bin
                        break
                currBin = self.cutoffHist.GetBin(i, j)
                self.cutoffHist.SetBinContent(i+1, j+1, self.binRight/100.)
        self.File.cd()
        self.cutoffHist.Write()
        for i in hists:
            for hist in i:
                hist.Write()
    def __book__(self, name):
        self.File= ROOT.TFile(self.name + ".root", "RECREATE")
        self.File.cd()

    def FillHists(self, File, hists):
        F = TFile(File)
        self.T = F.Get("tree")
        for e in self.T:
            x = int(floor((self.T.AK8_rho + 7) / .3125))
            y = int(floor((self.T.AK8_pt - 100)/ 93.75))
            if x in range(16) and y in range(16):
                (hists[x][y]).Fill(self.T.AK8_n2, self.T.weight)
        F.Close()
    def FillHist(self, File, hist):
        F = TFile(File)
        self.T = F.Get("tree")
        for e in self.T:
            hist.Fill(self.T.AK8_rho, self.T.AK8_pt, self.T.AK8_n2)
        F.Close()
    def getHist(self):
        return self.cutoffHist


if __name__ == "__main__":
    hists = [[TH1F(str(i) + ", " + str(j), "N2 with Cuts; N2; Events", 50, 0., .5) for j in range(16)] for i in range(16)]
    #Cutoffs("N210ttbar", sys.argv[1], hists)