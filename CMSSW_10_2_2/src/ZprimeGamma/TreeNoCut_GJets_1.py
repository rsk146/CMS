import TreeNoCut
from TreeNoCut import *
import ROOT
from ROOT import *
import XRootD
from pyxrootd import client

if __name__ == "__main__":
	#triggers = ["HLT_Photon110EB_TightID_TightIso"]
	wgt = 19258533.0/2305000.0
	outputtree = "treesNoCutPhotonCut2018/HT200to400"
	inputfiles =  "/cms/xaastorage/NanoAOD/2018/DEC18/2018_GJets_HT/GJets_HT-200To400/"
	newTree = TreeNoCut(outputtree,inputfiles,wgt)	
