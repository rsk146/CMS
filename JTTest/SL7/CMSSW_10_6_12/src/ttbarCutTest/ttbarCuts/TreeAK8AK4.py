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
        
        self.Photon_pt = array('f', [0.0])
        self.addBranch('Photon_pt', self.Photon_pt, self.weight)
        self.Photon_eta = array('f', [100.0])
        self.addBranch('Photon_eta', self.Photon_eta, self.weight)
        self.Photon_phi = array('f', [0.0])
        self.addBranch('Photon_phi', self.Photon_phi, self.weight)
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
        self.AK8_rho = array('f', [0.0])
        self.addBranch('AK8_rho', self.AK8_rho, self.weight)
        self.AK8_tau21 = array('f', [0.0])
        self.addBranch('AK8_tau21', self.AK8_tau21, self.weight)
        self.AK8_tau32 = array('f', [0.0])
        self.addBranch('AK8_tau32', self.AK8_tau32, self.weight)
        self.AK8_n2 = array('f', [0.0])
        self.addBranch('AK8_n2', self.AK8_n2, self.weight)
        self.AK8_n3 = array('f', [0.0])
        self.addBranch('AK8_n3', self.AK8_n3, self.weight)

        self.AK4_Photon_deltaR = array('f', [0.0])
        self.addBranch('AK4_Photon_deltaR', self.AK4_Photon_deltaR, self.weight)
        self.AK4_Photon_deltaEta = array('f', [0.0])
        self.addBranch('AK4_Photon_deltaEta', self.AK4_Photon_deltaEta, self.weight)
        self.AK4_csv = array('f', [0.0])
        self.addBranch('AK4_csv', self.AK4_csv, self.weight)
        self.AK4_AK8_deltaR = array('f', [0.0])
        self.addBranch('AK4_AK8_deltaR', self.AK4_AK8_deltaR, self.weight)
        self.AK4_AK8_deltaEta = array('f', [0.0])
        self.addBranch('AK4_AK8_deltaEta', self.AK4_AK8_deltaEta, self.weight)
        self.AK4_mass = array('f', [0.0])
        self.addBranch('AK4_mass', self.AK4_mass, self.weight)

        self.MET = array('f', [0.0])
        self.addBranch('MET', self.MET, self.weight)
        self.photon_pdgId = array('f', [0.0])
        self.addBranch('photon_pdgId', self.photon_pdgId, self.weight)
        self.ak8_pdgId = array('f', [0.0])
        self.addBranch('ak8_pdgId', self.ak8_pdgId, self.weight)
        self.PhotonStatus = array('f', [0.0])
        self.addBranch('PhotonStatus', self.PhotonStatus, self.weight)
        self.AK8Status = array('f', [0.0])
        self.addBranch('AK8Status', self.AK8Status, self.weight)

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
            if not self.T.nPhoton > 0: continue
            if not self.T.nselectedPatJetsAK8PFPuppi > 0: continue
            tau21 = self.T.selectedPatJetsAK8PFPuppi_NjettinessAK8Puppi_tau2[jetsIndeces[0]] / self.T.selectedPatJetsAK8PFPuppi_NjettinessAK8Puppi_tau1[jetsIndeces[0]]
            tau32 = self.T.selectedPatJetsAK8PFPuppi_NjettinessAK8Puppi_tau3[jetsIndeces[0]] / self.T.selectedPatJetsAK8PFPuppi_NjettinessAK8Puppi_tau2[jetsIndeces[0]]                       
            #closest jet to AK8 specification
            if not self.T.nJet > 0: continue
            jet = TLorentzVector()
            photonJetdeltaR = 0
            AK8AK4deltaR = 0
            goodJetIndex = -1
            for i in range(len(self.T.Jet_pt)):
                if not self.T.Jet_jetId[i] > 2: continue
                jet.SetPtEtaPhiM(self.T.Jet_pt[i], self.T.Jet_eta[i], self.T.Jet_phi[i], self.T.Jet_mass[i])
                if AK8AK4deltaR == 0:
                    if jet.DeltaR(fatjet) > .3:
                        photonJetdeltaR = jet.DeltaR(photon)
                        AK8AK4deltaR = jet.DeltaR(fatjet)
                        goodJetIndex = i
                elif (jet.DeltaR(fatjet) < AK8AK4deltaR and jet.DeltaR(fatjet) > .3): 
                    photonJetdeltaR = jet.DeltaR(photon)
                    AK8AK4deltaR = jet.DeltaR(fatjet)
                    goodJetIndex = i
            if goodJetIndex == -1: continue
            photonJetdeltaEta = abs(self.T.Jet_eta[goodJetIndex] - goodPhotonsEta[0])
            AK8AK4deltaEta = abs(self.T.Jet_eta[goodJetIndex] - goodJetsEta[0])
            #genparts
            genpart = TLorentzVector()
            genpart.SetPtEtaPhiM(self.T.GenPart_pt[0], self.T.GenPart_eta[0], self.T.GenPart_phi[0], self.T.GenPart_mass[0])
            dR_photon = photon.DeltaR(genpart)
            dR_ak8 = fatjet.DeltaR(genpart)
            photon_match_index = 0
            ak8_match_index = 0
            for gp in range(self.T.nGenPart):
                genpart.SetPtEtaPhiM(self.T.GenPart_pt[gp], self.T.GenPart_eta[gp], self.T.GenPart_phi[gp], self.T.GenPart_mass[gp])
                if photon.DeltaR(genpart) < dR_photon: 
                    dR_photon = photon.DeltaR(genpart)
                    photon_match_index = gp
                if fatjet.DeltaR(genpart) < dR_ak8:
                    dR_ak8 = fatjet.DeltaR(genpart)
                    ak8_match_index = gp
            #FILL
            self.Photon_pt[0] = goodPhotonsPt[0]
            self.Photon_eta[0] = goodPhotonsEta[0]
            self.Photon_phi[0] = self.T.Photon_phi[photonIndeces[0]]
            self.Photon_mvaID_WP80[0] = self.T.Photon_mvaID_WP80[photonIndeces[0]]
            self.Photon_mvaID_WP90[0] = self.T.Photon_mvaID_WP90[photonIndeces[0]]
            self.Photon_pfRelIso03_all[0] = self.T.Photon_pfRelIso03_all[photonIndeces[0]]
            
            self.AK8_phi[0] = self.T.selectedPatJetsAK8PFPuppi_phi[jetsIndeces[0]]
            self.AK8_pt[0] = goodJetsPt[0]
            self.AK8_eta[0] = goodJetsEta[0]
            self.AK8_mass[0] = self.T.selectedPatJetsAK8PFPuppi_mass[jetsIndeces[0]]
            self.AK8_msoftdrop[0] = goodJetsSDM[0]
            self.AK8_rho[0] = FatRho
            self.AK8_tau21[0] = tau21
            self.AK8_tau32[0] = tau32
            self.AK8_n2[0] = self.T.selectedPatJetsAK8PFPuppi_ak8PFJetsPuppiSoftDropValueMap_nb1AK8PuppiSoftDropN2[jetsIndeces[0]]
            self.AK8_n3[0] = self.T.selectedPatJetsAK8PFPuppi_ak8PFJetsPuppiSoftDropValueMap_nb1AK8PuppiSoftDropN3[jetsIndeces[0]]

            self.AK4_Photon_deltaR[0] = photonJetdeltaR
            self.AK4_Photon_deltaEta[0] = photonJetdeltaEta
            self.AK4_csv[0] = self.T.Jet_btagCSVV2[goodJetIndex]
            self.AK4_mass[0] = self.T.Jet_mass[goodJetIndex]
            self.AK4_AK8_deltaR[0] = AK8AK4deltaR
            self.AK4_AK8_deltaEta[0] = AK8AK4deltaEta
            self.MET[0] = self.T.MET_pt

            self.photon_pdgId[0] = self.T.GenPart_pdgId[photon_match_index]
            self.ak8_pdgId[0] = self.T.GenPart_pdgId[ak8_match_index]
            self.PhotonStatus[0] = self.T.GenPart_status[photon_match_index]
            self.AK8Status[0] = self.T.GenPart_status[ak8_match_index]
            self.tree.Fill()
            
        File.Close()
    def addBranch(self, name, obj, T):
        self.tree.Branch(name, obj, name + "/F")

#ttbar
newTree = Tree("/users/h2/rsk146/JTTest/SL7/CMSSW_10_6_12/src/ttbarCutTest/ttbar2018PreselectionTreeAK8AK4TestPDGID", "/users/h2/rsk146/JTTest/SL7/CMSSW_10_2_15/src/ttbarminiAOD/", 36*831760.0/10345333.0, ["HLT_Photon175", "HLT_Photon110EB_TightID_TightIso"])
#signal
#signalTree = Tree("/users/h2/rsk146/JTTest/SL7/CMSSW_10_6_12/src/ttbarCutTest/signal2018PreselectionTreeAK8AK4", "/users/h2/rsk146/JTTest/SL7/CMSSW_10_2_15/src/signalM_10MCNano/", 36*690.0/453231.0, ["HLT_Photon175", "HLT_Photon110EB_TightID_TightIso"])
#gjets
#bin1 = Tree("/users/h2/rsk146/JTTest/SL7/CMSSW_10_6_12/src/ttbarCutTest/100to200PreselectionTreeAK8AK4", "/users/h2/rsk146/JTTest/CMSSW_10_2_15/src/miniAODJobs100to200/", 36*9238000.0/10125438.0, ["HLT_Photon175", "HLT_Photon110EB_TightID_TightIso"])
#bin2 = Tree("/users/h2/rsk146/JTTest/SL7/CMSSW_10_6_12/src/ttbarCutTest/200to400PreselectionTreeAK8AK4", "/users/h2/rsk146/JTTest/CMSSW_10_2_15/src/miniAODJobs200to400/", 36*2305000.0/19258533.0, ["HLT_Photon175", "HLT_Photon110EB_TightID_TightIso"])
#bin3 = Tree("/users/h2/rsk146/JTTest/SL7/CMSSW_10_6_12/src/ttbarCutTest/400to600PreselectionTreeAK8AK4", "/users/h2/rsk146/JTTest/SL7/CMSSW_10_2_15/src/miniAODJobs400to600/", 36*274400.0/4795233.0, ["HLT_Photon175", "HLT_Photon110EB_TightID_TightIso"])
#bin4 = Tree("/users/h2/rsk146/JTTest/SL7/CMSSW_10_6_12/src/ttbarCutTest/600toInfPreselectionTreeAK8AK4", "/users/h2/rsk146/JTTest/SL7/CMSSW_10_2_15/src/miniAODJobs600toInf/", 36*93460.0/5044493.0, ["HLT_Photon175", "HLT_Photon110EB_TightID_TightIso"])
