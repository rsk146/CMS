import ROOT
from ROOT import *
import os
import sys
import math

if __name__ == "__main__":
    f = TFile("/home/akobert/CMSSW_10_2_9/src/N2DDT.root")
    passhist = f.Get("pass_rho_pt")  
    failhist = f.Get("fail_rho_pt")
    #rho: 14 bins: 3 to 12
    #pt: 40 bins: 3 to 30
    print "Pass X: " + str(passhist.GetNbinsX())
    print "Pass Y: " + str(passhist.GetNbinsY())
    print "Fail X: " + str(failhist.GetNbinsX())
    print "Fail Y: " + str(failhist.GetNbinsY())

    