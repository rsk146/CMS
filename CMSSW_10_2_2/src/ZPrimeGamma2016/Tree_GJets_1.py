import TreeMaker
from TreeMaker import *
import ROOT
from ROOT import *
import XRootD
from pyxrootd import client

if __name__ == "__main__":
        triggers = ["HLT_Photon165_HE10", "HLT_Photon175"]
        wgt = 1092000.0/50836550.0
        outputtree = "HT200to400"
        inputfiles =  "/cms/xaastorage/NanoAOD/2016/DEC18/GJets_2016/GJets_DR-0p4_HT-200To400/"
        newTree = Tree(outputtree,inputfiles,wgt, triggers)
