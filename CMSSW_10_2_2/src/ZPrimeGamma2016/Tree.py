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
	self.ntot = 0
	self.nTrig = 0
	self.nGT1phojet = 0
	self.nPhotonCuts = 0

        self.nPhotonpt = 0
        self.nJetpteta = 0 
        self.nPhotoneta = 0
        self.nWp90 = 0
        self.nRho = 0
        self.nDR = 0
        self.nJetid = 0
        self.nbveto = 0
        self.nDRjet = 0

	self.nElectronCuts = 0
	self.nRhoCuts = 0
	self.nDeltaRCuts = 0
	self.nJetCuts = 0
	self.nSignalCuts = 0
        for file in glob.glob(self.F + "*.root"):
            print file
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
        self.Photon_electronVeto = array('f', [100.0])
        self.addBranch('Photon_electronVeto', self.Photon_electronVeto, self.weight)
        self.Photon_pfRelIso03_all = array('f', [0.0])
        self.addBranch('Photon_pfRelIso03_all', self.Photon_pfRelIso03_all, self.weight)
        
        self.Electron_convVeto = array('f', [100.0])
        self.addBranch('Electron_convVeto', self.Electron_convVeto, self.weight)
        self.Electron_pt = array('f', [0.0])
        self.addBranch('Electron_pt', self.Electron_pt, self.weight)
        self.Electron_eta = array('f', [0.0])
        self.addBranch('Electron_eta', self.Electron_eta, self.weight)
        self.Electron_cutBased = array('f', [100.0])
        self.addBranch('Electron_cutBased', self.Electron_cutBased, self.weight)
        
        self.FatJet_pt = array('f', [0.0])
        self.addBranch('FatJet_pt', self.FatJet_pt, self.weight)
        self.FatJet_eta = array('f', [100.0])
        self.addBranch('FatJet_eta', self.FatJet_eta, self.weight)
        self.FatJet_mass = array('f', [-1.0])
        self.addBranch('FatJet_mass', self.FatJet_mass, self.weight)
        self.FatJet_phi = array('f', [0.0])
        self.addBranch('FatJet_phi', self.FatJet_phi, self.weight)
        self.FatJet_msoftdrop = array('f', [0.0])
        self.addBranch('FatJet_msoftdrop', self.FatJet_msoftdrop, self.weight)
        self.FatJet_jetId = array('f', [100.0])
        self.addBranch('FatJet_jetId', self.FatJet_jetId, self.weight)
        self.FatJet_rho = array('f', [0.0])
        self.addBranch('FatJet_rho', self.FatJet_rho, self.weight)
        self.FatJet_tau1 = array('f', [100.0])
        self.addBranch('FatJet_tau1', self.FatJet_tau1, self.weight)
        self.FatJet_tau2 = array('f', [100.0])
        self.addBranch('FatJet_tau2', self.FatJet_tau2, self.weight)
        self.FatJet_tau3 = array('f', [100.0])
        self.addBranch('FatJet_tau3', self.FatJet_tau3, self.weight)
        self.FatJet_tau4 = array('f', [100.0])
        self.addBranch('FatJet_tau4', self.FatJet_tau4, self.weight)
        #self.HadronicHT = array('f', [0.0])
        #self.addBranch('HadronicHT', self.HadronicHT, self.weight)
        self.FatJet_tau21 = array('f', [0.0])
        self.addBranch('FatJet_tau21', self.FatJet_tau21, self.weight)
        self.FatJet_n2b1 = array('f', [0.0])
        self.addBranch('FatJet_n2b1', self.FatJet_n2b1, self.weight)

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
	    self.ntot+=1
            if not((GET(e, trigger[0]) or GET(e, trigger[1]))): continue
	    self.nTrig+=1
            if not self.T.nPhoton > 0: continue
            if not self.T.nFatJet > 0: continue
            #control Cuts
            #photon cuts
            goodPhotonsPt = []
            goodPhotonsEta = []
            photonIndeces = []
            for i in range(len(self.T.Photon_pt)):
                if self.T.Photon_pt[i] > 200 and abs(self.T.Photon_eta[i])< 2.1 and self.T.Photon_mvaID_WP90[i] > 0 and self.T.Photon_electronVeto[i] > 0:   
                    goodPhotonsPt.append(self.T.Photon_pt[i])
                    goodPhotonsEta.append(self.T.Photon_eta[i])
                    photonIndeces.append(i)
            ptCounter = 0
            for s in goodPhotonsPt:
                if s > 14:
                    ptCounter+=1
            if ptCounter > 1: continue
            #jet cuts
            goodJetsPt = []
            goodJetsEta = []
            goodJetsSDM = []
            goodJetsRho = []
            jetsIndeces= []
            for i in range(len(self.T.FatJet_pt)):
                
                if self.T.FatJet_pt[i] > 200 and abs(self.T.FatJet_eta[i]) < 2.1 and self.T.FatJet_msoftdrop[i] > 0 and self.T.FatJet_jetId[i] > 2: 
                    FatRho = math.log((self.T.FatJet_msoftdrop[i]*self.T.FatJet_msoftdrop[i])/(self.T.FatJet_pt[i]*self.T.FatJet_pt[i]))
                    if FatRho > -7.5 and FatRho < -2:
                        goodJetsPt.append(self.T.FatJet_pt[i])
                        goodJetsEta.append(self.T.FatJet_eta[i])
                        goodJetsSDM.append(self.T.FatJet_msoftdrop[i])
                        goodJetsRho.append(FatRho)
                        jetsIndeces.append(i)
            
            #electron cuts
            ElectronBool = False
            for i in range(len(self.T.Electron_pt)):
                if self.T.Electron_pt[i] > 10 and abs(self.T.Electron_eta[i]) < 2.5 and self.T.Electron_cutBased[i] < 3:
                    ElectronBool = True
                    break
            if ElectronBool: continue
            if len(goodPhotonsPt) == 0 or len(goodJetsPt) == 0: continue
            #deltaR cuts
            photon = TLorentzVector()
            fatjet = TLorentzVector()
            photon.SetPtEtaPhiM(goodPhotonsPt[0], goodPhotonsEta[0], self.T.Photon_phi[photonIndeces[0]], self.T.Photon_mass[photonIndeces[0]])
            fatjet.SetPtEtaPhiM(goodJetsPt[0], goodJetsEta[0], self.T.FatJet_phi[jetsIndeces[0]], self.T.FatJet_mass[jetsIndeces[0]])
            deltaR = photon.DeltaR(fatjet) 
            if not deltaR > 2.2: continue
            #signal
            #if self.T.Jet_btagCSVV2[] >= .5426 and deltaRJet < 1.5: continue
            #if self.T.Jet_pt[0] > 30 and deltaRJet < .8: continue
            #self.nDRjet +=1 
            #if self.T.MET_pt > 75: continue
            tau21 = self.T.FatJet_tau2[jetsIndeces[0]] / self.T.FatJet_tau1[jetsIndeces[0]]
            #FILL
            self.Photon_pt[0] = goodPhotonsPt[0]
            self.Photon_eta[0] = goodPhotonsEta[0]
            self.Photon_phi[0] = self.T.Photon_phi[photonIndeces[0]]
            self.Photon_mass[0] = self.T.Photon_mass[photonIndeces[0]]
            self.Photon_mvaID_WP80[0] = self.T.Photon_mvaID_WP80[photonIndeces[0]]
            self.Photon_mvaID_WP90[0] = self.T.Photon_mvaID_WP90[photonIndeces[0]]
            self.Photon_electronVeto[0] = self.T.Photon_electronVeto[photonIndeces[0]]
            self.Photon_pfRelIso03_all[0] = self.T.Photon_pfRelIso03_all[photonIndeces[0]]
            
            self.FatJet_phi[0] = self.T.FatJet_phi[jetsIndeces[0]]
            self.FatJet_pt[0] = goodJetsPt[0]
            self.FatJet_eta[0] = goodJetsEta[0]
            self.FatJet_mass[0] = self.T.FatJet_mass[jetsIndeces[0]]
            self.FatJet_msoftdrop[0] = goodJetsSDM[0]
            if FatRho > -7.5 and FatRho < -2:
                self.FatJet_rho[0] = FatRho
            self.FatJet_tau21[0] = tau21

            self.tree.Fill()
            
        File.Close()
    def addBranch(self, name, obj, T):
        self.tree.Branch(name, obj, name + "/F")


newTree = Tree("TestTreeLoops", "/cms/evah/workspace/CMSSW_9_4_9/src/old_runs/VectorDiJet1Gamma_75_13TeV-madgraph/MultiN/", 99824.0/290.0, ["HLT_Photon175", "HLT_Photon165_HE10"]) 
#newTree = Tree("TestGJets","/cms/xaastorage/NanoAOD/2018/DEC18/2018_GJets_HT/GJets_HT-100To200/", 10125438.0/9238000.0, ["HLT_Photon175", "HLT_Photon110EB_TightID_TightIso"])
