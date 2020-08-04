import Tree
from Tree import *
import ROOT
from ROOT import *
import XRootD
from pyxrootd import client

if __name__ == "__main__":
	triggers = ["HLT_Photon175"]
	wgt = 10125438.0/9238000.0
	outputtree = "treesOldCutLeadJet2018/HT100to200"
	inputfiles =  "/cms/xaastorage/NanoAOD/2018/DEC18/2018_GJets_HT/GJets_HT-100To200/"
	newTree = Tree(outputtree,inputfiles,wgt, triggers)
		
