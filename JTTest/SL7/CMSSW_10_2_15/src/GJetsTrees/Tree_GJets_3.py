import Tree
from Tree import *
import ROOT
from ROOT import *
import XRootD
from pyxrootd import client

if __name__ == "__main__":
        triggers = ["HLT_Photon110EB_TightID_TightIso", "HLT_Photon175"]
        wgt = 36*93460.0/5044493.0
        outputtree = "GJetsHT600toInf"
        inputfiles =  "/users/h2/rsk146/JTTest/SL7/CMSSW_10_2_15/src/miniAODJobs600toInf/"
        newTree = Tree(outputtree,inputfiles,wgt, triggers)
