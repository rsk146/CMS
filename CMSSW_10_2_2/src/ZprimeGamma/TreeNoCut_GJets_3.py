import TreeNoCut
from TreeNoCut import *
import ROOT
from ROOT import *
import XRootD
from pyxrootd import client

if __name__ == "__main__":
	#triggers = ["HLT_Photon110EB_TightID_TightIso"]
	wgt = 5044493.0/93460.0
	outputtree = "treesNoCutPhotonCut2018/HT600toInf"
	inputfiles =  "/cms/xaastorage/NanoAOD/2018/DEC18/2018_GJets_HT/GJets_HT-600ToInf/"
	newTree = TreeNoCut(outputtree,inputfiles,wgt)
		
