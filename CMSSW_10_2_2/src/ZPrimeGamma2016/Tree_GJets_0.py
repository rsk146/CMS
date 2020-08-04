import TreeMaker
from TreeMaker import *
import ROOT
from ROOT import *
import XRootD
from pyxrootd import client

if __name__ == "__main__":
        triggers = ["HLT_Photon165_HE10", "HLT_Photon175"]
        wgt = 4881000.0/15007836.0
        outputtree = "HT100to200"
        inputfiles =  "/cms/xaastorage/NanoAOD/2016/DEC18/GJets_2016/GJets_DR-0p4_HT-100To200/"
        newTree = Tree(outputtree,inputfiles,wgt, triggers)
