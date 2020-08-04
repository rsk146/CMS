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
        self.deltaRFatJetPhoton = array('f', [0.0])
        self.addBranch('deltaRFatJetPhoton', self.deltaRFatJetPhoton, self.weight)
        self.deltaRJetPhoton = array('f', [0.0])
        self.addBranch('deltaRJetPhoton', self.deltaRJetPhoton, self.weight)

        self.Photon_pt = array('f', [0.0])
        self.addBranch('Photon_pt', self.Photon_pt, self.weight)
        self.Photon_eta = array('f', [100.0])
        self.addBranch('Photon_eta', self.Photon_eta, self.weight)
        self.Photon_phi = array('f', [0.0])
        self.addBranch('Photon_phi', self.Photon_phi, self.weight)
        self.Photon_mass = array('f', [100.0])
        self.addBranch('Photon_mass', self.Photon_mass, self.weight)
        self.Photon_mvaID_WP80 = array('f', [100.0])
        self.addBranch('Photon_mvaID_WP80', self.Photon_mvaID_WP80, self.weight)
        self.Photon_mvaID_WP90 = array('f', [100.0])
        self.addBranch('Photon_mvaID_WP90', self.Photon_mvaID_WP90, self.weight)
        self.Photon_pfRelIso03_all = array('f', [0.0])
        self.addBranch('Photon_pfRelIso03_all', self.Photon_pfRelIso03_all, self.weight)
        
        self.AK8_pt = array('f', [0.0])
        self.addBranch('AK8_pt', self.AK8_pt, self.weight)
        self.AK8_eta = array('f', [100.0])
        self.addBranch('AK8_eta', self.AK8_eta, self.weight)
        self.AK8_mass = array('f', [-1.0])
        self.addBranch('AK8_mass', self.AK8_mass, self.weight)
        self.AK8_phi = array('f', [0.0])
        self.addBranch('AK8_phi', self.AK8_phi, self.weight)
        self.AK8_msoftdrop = array('f', [0.0])
        self.addBranch('AK8_msoftdrop', self.AK8_msoftdrop, self.weight)
        self.AK8_jetId = array('f', [100.0])
        self.addBranch('AK8_jetId', self.AK8_jetId, self.weight)
        self.AK8_rho = array('f', [0.0])
        self.addBranch('AK8_rho', self.AK8_rho, self.weight)
        self.AK8_tau1 = array('f', [100.0])
        self.addBranch('AK8_tau1', self.AK8_tau1, self.weight)
        self.AK8_tau2 = array('f', [100.0])
        self.addBranch('AK8_tau2', self.AK8_tau2, self.weight)
        self.AK8_tau3 = array('f', [100.0])
        self.addBranch('AK8_tau3', self.AK8_tau3, self.weight)
        self.AK8_tau4 = array('f', [100.0])
        self.addBranch('AK8_tau4', self.AK8_tau4, self.weight)
        self.AK8_tau21 = array('f', [0.0])
        self.addBranch('AK8_tau21', self.AK8_tau21, self.weight)
        self.AK8_n2 = array('f', [0.0])
        self.addBranch('AK8_n2', self.AK8_n2, self.weight)

        self.Jet_pt = array('f', [0.0])
        self.addBranch('Jet_pt', self.Jet_pt, self.weight)
        self.Jet_eta = array('f', [100.0])
        self.addBranch('Jet_eta', self.Jet_eta, self.weight)
        self.Jet_phi = array('f', [0.0])
        self.addBranch('Jet_phi', self.Jet_phi, self.weight)
        self.Jet_mass = array('f', [0.0])
        self.addBranch('Jet_mass', self.Jet_mass, self.weight)
        self.Jet_rho = array('f', [0.0])
        self.addBranch('Jet_rho', self.Jet_rho, self.weight)
        self.Jet_btagCSVV2 = array('f', [0.0])
        self.addBranch('Jet_btagCSVV2', self.Jet_btagCSVV2, self.weight)

        self.MET_pt = array('f', [0.0])
        self.addBranch('MET_pt', self.MET_pt, self.weight)
    
    def FillTree(self, file, trigger):
        File = TFile(file)
        self.T = File.Get("Events")        
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
                    if FatRho > -7 and FatRho < -2:
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
            tau21 = self.T.selectedPatJetsAK8PFPuppi_NjettinessAK8Puppi_tau2[jetsIndeces[0]] / self.T.selectedPatJetsAK8PFPuppi_NjettinessAK8Puppi_tau1[jetsIndeces[0]]
            #FILL
            self.Photon_pt[0] = goodPhotonsPt[0]
            self.Photon_eta[0] = goodPhotonsEta[0]
            self.Photon_phi[0] = self.T.Photon_phi[photonIndeces[0]]
            self.Photon_mass[0] = self.T.Photon_mass[photonIndeces[0]]
            self.Photon_mvaID_WP80[0] = self.T.Photon_mvaID_WP80[photonIndeces[0]]
            self.Photon_mvaID_WP90[0] = self.T.Photon_mvaID_WP90[photonIndeces[0]]
            self.Photon_pfRelIso03_all[0] = self.T.Photon_pfRelIso03_all[photonIndeces[0]]
            
            self.AK8_phi[0] = self.T.selectedPatJetsAK8PFPuppi_phi[jetsIndeces[0]]
            self.AK8_pt[0] = goodJetsPt[0]
            self.AK8_eta[0] = goodJetsEta[0]
            self.AK8_mass[0] = self.T.selectedPatJetsAK8PFPuppi_mass[jetsIndeces[0]]
            self.AK8_msoftdrop[0] = goodJetsSDM[0]
            #if FatRho > -7.5 and FatRho < -2:
            self.AK8_rho[0] = goodJetsRho[0]
            self.AK8_tau21[0] = tau21
            self.AK8_n2[0] = self.T.selectedPatJetsAK8PFPuppi_ak8PFJetsPuppiSoftDropValueMap_nb1AK8PuppiSoftDropN2[0]
            self.tree.Fill()
            
        File.Close()
    def addBranch(self, name, obj, T):
        self.tree.Branch(name, obj, name + "/F")


#newTree = Tree("TestTreeLoops", "/cms/evah/workspace/CMSSW_9_4_9/src/old_runs/VectorDiJet1Gamma_75_13TeV-madgraph/MultiN/", 99824.0/290.0, ["HLT_Photon175", "HLT_Photon165_HE10"]) 
#newTree = Tree("TestGJets","/cms/xaastorage/NanoAOD/2018/DEC18/2018_GJets_HT/GJets_HT-100To200/", 10125438.0/9238000.0, ["HLT_Photon175", "HLT_Photon110EB_TightID_TightIso"])
