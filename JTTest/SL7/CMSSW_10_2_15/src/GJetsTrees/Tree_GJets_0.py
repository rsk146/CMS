import Tree
from Tree import *
import ROOT
from ROOT import *
import XRootD
from pyxrootd import client

if __name__ == "__main__":
        triggers = ["HLT_Photon110EB_TightID_TightIso", "HLT_Photon175"]
        wgt = 36*9238000.0/10125438.0
        outputtree = "GJetsHT100to200"
        inputfiles =  "/users/h2/rsk146/JTTest/CMSSW_10_2_15/src/miniAODJobs100to200/"
        newTree = Tree(outputtree,inputfiles,wgt, triggers)
