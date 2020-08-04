import Tree
from Tree import *
import ROOT
from ROOT import *
import XRootD
from pyxrootd import client

if __name__ == "__main__":
        triggers = ["HLT_Photon110EB_TightID_TightIso", "HLT_Photon175"]
        wgt = 36*2305000.0/19258533.0
        outputtree = "GJetsHT200to400"
        inputfiles =  "/users/h2/rsk146/JTTest/CMSSW_10_2_15/src/miniAODJobs200to400/"
        newTree = Tree(outputtree,inputfiles,wgt, triggers)
