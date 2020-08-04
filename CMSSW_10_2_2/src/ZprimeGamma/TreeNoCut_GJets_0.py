import TreeNoCut
from TreeNoCut import *
import ROOT
from ROOT import *
import XRootD
from pyxrootd import client

if __name__ == "__main__":
	#triggers = ["HLT_Photon110EB_TightID_TightIso"]
	wgt = 10125438.0/9238000
	outputtree = "treesNoCutPhotonCut2018/HT100to200"
	inputfiles =  "/cms/xaastorage/NanoAOD/2018/DEC18/2018_GJets_HT/GJets_HT-100To200/"
	newTree = TreeNoCut(outputtree,inputfiles,wgt)
		
