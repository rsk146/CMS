import ROOT
import os
from ROOT import *
from array import array
import math
from math import *
import sys
import glob
import csv
def GET(E,B):
    return getattr(E,B)

class Tree:
    def __init__(self, name, F, weight, triggers):
        self.name = name
        self.F = F
        self.__book__(name, weight)
        self.triggers = triggers
        for file in glob.glob(self.F + "*.root"):
            self.FillTree(file, self.triggers)
        self.f.cd()
        self.f.Write()
        self.f.Close()

    def __book__(self, name, weight):
        self.f = ROOT.TFile(self.name + ".root", "RECREATE")
        self.f.cd()
        self.tree = ROOT.TTree("tree", "tree")
        
        self.weight = array('f', [0.0])
        self.addBranch('weight', self.weight, self.tree)
        self.weight[0] = weight
        
        self.AK8_pt = array('f', [0.0])
        self.addBranch('AK8_pt', self.AK8_pt, self.weight)
        self.AK8_eta = array('f', [100.0])
        self.addBranch('AK8_eta', self.AK8_eta, self.weight)
        self.AK8_msoftdrop = array('f', [0.0])
        self.addBranch('AK8_msoftdrop', self.AK8_msoftdrop, self.weight)
        self.AK8_jetId = array('f', [100.0])
        self.addBranch('AK8_jetId', self.AK8_jetId, self.weight)
        self.AK8_n2 = array('f', [-100.0])
        self.addBranch('AK8_n2', self.AK8_n2, self.weight)
        self.AK8_nCons = array('f', [0.0])
        self.addBranch('AK8_nCons', self.AK8_nCons, self.weight)
        self.AK8_JetFlavor = array('f', [100.0])
        self.addBranch('AK8_JetFlavor', self.AK8_JetFlavor, self.weight)
    
    def FillTree(self, file, trigger):
        File = TFile(file)
        self.T = File.Get("Events")   
        print str(file)
        for e in self.T:
            #CUTS
            if not((GET(e, trigger[0]) or GET(e, trigger[1]))): continue
            if not self.T.nPhoton > 0: continue
            if not self.T.nselectedPatJetsAK8PFPuppi > 0: continue
            #control Cuts
            #photon cuts
            goodPhotonsPt = []
            goodPhotonsEta = []
            photonIndeces = []
            for i in range(len(self.T.Photon_pt)):
                if self.T.Photon_pt[i] > 110 and abs(self.T.Photon_eta[i])< 2.1 and self.T.Photon_mvaID_WP90[i] > 0:   
                    goodPhotonsPt.append(self.T.Photon_pt[i])
                    goodPhotonsEta.append(self.T.Photon_eta[i])
                    photonIndeces.append(i)
            #jet cuts
            goodJetsPt = []
            goodJetsEta = []
            goodJetsSDM = []
            goodJetsRho = []
            jetsIndeces= []
            for i in range(len(self.T.selectedPatJetsAK8PFPuppi_pt)):
                
                if self.T.selectedPatJetsAK8PFPuppi_pt[i] > 110 and abs(self.T.selectedPatJetsAK8PFPuppi_eta[i]) < 2.1 and self.T.selectedPatJetsAK8PFPuppi_softdropMass[i] > 0 and self.T.selectedPatJetsAK8PFPuppi_jetId[i] > 2: 
                    FatRho = math.log((self.T.selectedPatJetsAK8PFPuppi_softdropMass[i]*self.T.selectedPatJetsAK8PFPuppi_softdropMass[i])/(self.T.selectedPatJetsAK8PFPuppi_pt[i]*self.T.selectedPatJetsAK8PFPuppi_pt[i]))
                    if FatRho > -7.5 and FatRho < -2:
                        goodJetsPt.append(self.T.selectedPatJetsAK8PFPuppi_pt[i])
                        goodJetsEta.append(self.T.selectedPatJetsAK8PFPuppi_eta[i])
                        goodJetsSDM.append(self.T.selectedPatJetsAK8PFPuppi_softdropMass[i])
                        goodJetsRho.append(FatRho)
                        jetsIndeces.append(i)
            #deltaR cuts
            photon = TLorentzVector()
            fatjet = TLorentzVector()
            if len(jetsIndeces) == 0 or len(photonIndeces) == 0: continue
            photon.SetPtEtaPhiM(goodPhotonsPt[0], goodPhotonsEta[0], self.T.Photon_phi[photonIndeces[0]], self.T.Photon_mass[photonIndeces[0]])
            fatjet.SetPtEtaPhiM(goodJetsPt[0], goodJetsEta[0], self.T.selectedPatJetsAK8PFPuppi_phi[jetsIndeces[0]], self.T.selectedPatJetsAK8PFPuppi_mass[jetsIndeces[0]])
            deltaR = photon.DeltaR(fatjet) 
            if not deltaR > 2.2: continue
                #FILL
            self.AK8_pt[0] = self.T.selectedPatJetsAK8PFPuppi_pt[0]
            self.AK8_eta[0] = self.T.selectedPatJetsAK8PFPuppi_eta[0]
            self.AK8_msoftdrop[0] = self.T.selectedPatJetsAK8PFPuppi_softdropMass[0]
            self.AK8_n2[0] = self.T.selectedPatJetsAK8PFPuppi_ak8PFJetsPuppiSoftDropValueMap_nb1AK8PuppiSoftDropN2[0]
            self.AK8_jetId[0] = self.T.selectedPatJetsAK8PFPuppi_jetId[0]
            self.AK8_nCons[0] = self.T.selectedPatJetsAK8PFPuppi_nConstituents[0]
            self.AK8_JetFlavor[0] = self.T.selectedPatJetsAK8PFPuppi_partonFlavor[0]
            self.tree.Fill()
            
        File.Close()
    def addBranch(self, name, obj, T):
        self.tree.Branch(name, obj, name + "/F")


#newTree = Tree("TestTreeLoops", "/cms/evah/workspace/CMSSW_9_4_9/src/old_runs/VectorDiJet1Gamma_75_13TeV-madgraph/MultiN/", 99824.0/290.0, ["HLT_Photon175", "HLT_Photon165_HE10"]) 
#newTree = Tree("TestGJets","/cms/xaastorage/NanoAOD/2018/DEC18/2018_GJets_HT/GJets_HT-100To200/", 10125438.0/9238000.0, ["HLT_Photon175", "HLT_Photon110EB_TightID_TightIso"])
newTree = Tree("/users/h2/rsk146/JTTest/SL7/CMSSW_10_2_15/src/JetFlavorCheck/ttbar2018FlavorTreeCuts", "/users/h2/rsk146/JTTest/SL7/CMSSW_10_2_15/src/ttbarminiAOD/",  10345333.0/831760.0, ["HLT_Photon175", "HLT_Photon110EB_TightID_TightIso"])
