import ROOT
import os
from ROOT import *
from array import array
import math
from math import *
import sys
import glob
import csv
import ctypes
from ctypes import*

class histDraw:
    def __init__(self, hist, eff, filename, dim, log, c):
        out = TFile("ttbarPreselectionHists.root", "UPDATE")
        f1 = TFile(filename)
        c1 = TCanvas(c, c, 10, 10, 700, 500)
        if not dim-1:
            input1 = TH1F()
            f1.GetObject(hist, input1)
            c1.cd()
            if log:
                c1.SetLogy()
            #input1.GetYAxis().SetRangeUser(0, ran)
            input1.SetLineColor(kBlack)
            input1.SetFillColor(kAzure-9)
            input1.SetLineWidth(2)
            input1.SetStats(0)
            input1.Draw("hist")
            c1.Update()
            c1.Modified()
            out.cd()
            c1.Write()
        else:
            input1 = TH2F()
            one = TH1F()
            two = TH1F()
            three = TH1F()
            four = TH1F()
            five = TH1F()
            six = TH1F()
            seven = TH1F()
            eight = TH1F()
            nine = TH1F()
            effic = [one, two, three, four, five, six, seven, eight, nine]
            f1.Print()
            f1.GetObject("tree", input1)
            c1.cd()
            input1.SetStats(0)
            input1.Draw("colz")
            for his in effic:
                i = 1
                name = eff + str(i)
                f1.GetObject(name, his)
                his.SetLineColor(kRed)
                his.SetLineWidth(2)
                his.Draw("same hist")


histDraw("PhotonPt", "", "ttbarPreselection1D.root", 1, 1, "Photon Pt")
histDraw("PhotonEta", "", "ttbarPreselection1D.root", 1, 1, "Photon Eta")
#histDraw("AK8Rho", "", "ttbar1D.root", 1, 1, "Jet Rho")
histDraw("AK8Pt", "", "ttbarPreselection1D.root", 1, 1, "FatJet Pt")
histDraw("AK8Eta", "", "ttbarPreselection1D.root", 1, 1, "FatJet Eta")
histDraw("AK8SDM", "", "ttbarPreselection1D.root", 1, 1, "FatJet SDM")
histDraw("AK8N2", "", "ttbarPreselection1D.root", 1, 1, "FatJet N2")
