import Tree
from Tree import *
import ROOT
from ROOT import *
import XRootD
from pyxrootd import client

if __name__ == "__main__":
        triggers = ["HLT_Photon110EB_TightID_TightIso", "HLT_Photon175"]
        wgt = 36*274400.0/4795233.0
        outputtree = "GJetsHT400to600"
        inputfiles =  "/users/h2/rsk146/JTTest/SL7/CMSSW_10_2_15/src/miniAODJobs400to600/"
        newTree = Tree(outputtree,inputfiles,wgt, triggers)
