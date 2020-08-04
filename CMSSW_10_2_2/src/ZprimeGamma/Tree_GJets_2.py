import Tree
from Tree import *
import ROOT
from ROOT import *
import XRootD
from pyxrootd import client

if __name__ == "__main__":
	triggers = ["HLT_Photon110EB_TightID_TightIso", "HLT_Photon175"]
	wgt = 4795233.0/274400.0
	outputtree = "treesOrCut2018/HT400to600"
	inputfiles =  "/cms/xaastorage/NanoAOD/2018/DEC18/2018_GJets_HT/GJets_HT-400To600/"
	newTree = Tree(outputtree,inputfiles,wgt, triggers)
		
