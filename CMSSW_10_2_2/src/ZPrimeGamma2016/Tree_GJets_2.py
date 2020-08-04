import TreeMaker
from TreeMaker import *
import ROOT
from ROOT import *
import XRootD
from pyxrootd import client

if __name__ == "__main__":
        triggers = ["HLT_Photon165_HE10", "HLT_Photon175"]
        wgt = 126300.0/11850304.0
        outputtree = "HT400to600"
        inputfiles =  "/cms/xaastorage/NanoAOD/2016/DEC18/GJets_2016/GJets_DR-0p4_HT-400To600/"
        newTree = Tree(outputtree,inputfiles,wgt, triggers)


