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
    def __init__(self, name, File, weight, triggers):
        self.name = name
        self.triggeredCounter = 0
        self.total = 0
        #self.tree = ROOT.TTree("tree", "tree")
        self.File = File
        self.__book__(name, weight)
        self.triggers = triggers
        for file in glob.glob(self.File + "*.root"):
            self.FillMicroTree(file, self.triggers)
        #self.triggers = triggers
        self.f.cd()
        self.f.Write()
        self.f.Close()


    def __book__(self, name, weight):
        self.f = ROOT.TFile(self.name + ".root", "RECREATE")
        self.f.cd()
        self.tree = ROOT.TTree("tree", "tree")

        #define gen vars
        self.weight = array('f', [0.0])
        self.addBranch('weight', self.weight, self.tree)
        self.weight[0] = weight

        #define photon vars
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

        #define jets vars
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
        self.FatJet_tau1 = array('f', [100.0])
        self.addBranch('FatJet_tau1', self.FatJet_tau1, self.weight)
        self.FatJet_tau2 = array('f', [100.0])
        self.addBranch('FatJet_tau2', self.FatJet_tau2, self.weight)
        self.FatJet_tau3 = array('f', [100.0])
        self.addBranch('FatJet_tau3', self.FatJet_tau3, self.weight)
        self.FatJet_tau4 = array('f', [100.0])
        self.addBranch('FatJet_tau4', self.FatJet_tau4, self.weight)
        self.HadronicHT = array('f', [0.0])
        self.addBranch('HadronicHT', self.HadronicHT, self.weight)

    def FillMicroTree(self, g, triggs):
        print "Working on " + g;
        F = TFile(g)
        self.T = F.Get("Events")
        for e in self.T: 
            #print "%s" %(w)
            #w+=1
           #for t in triggs:
            #if GET(e, triggs) >0:
                    #self.triggeredCounter+=1
            #       continue
         HadronicHT = 0
         t = triggs[0]
         x = triggs[1]
         if GET(e,t) > 0 or GET(e,x) > 0:
             self.triggeredCounter+=1
             if not self.T.nPhoton>0: continue
             if not abs(self.T.Photon_eta[0]) < 1.44: continue
             if not self.T.Photon_cutBasedBitmap[0] >= 4: continue
             if not (self.T.Photon_pfRelIso03_all[0]/self.T.Photon_pt[0]) < 0.2: continue
                #for s in range(2):
                   # if not (self.T.Jet_pt[s] >= 50): continue
                   # if not (abs(self.T.Jet_eta[s]) < 2.4): continue
                   # HadronicHT += self.T.Jet_pt[s]
            # self.HadronicHT[0] = self.T.Jet_pt[0]
             self.Photon_pt[0] = self.T.Photon_pt[0]
             self.Photon_eta[0] = self.T.Photon_eta[0]
             self.Photon_phi[0] = self.T.Photon_phi[0]
             self.Photon_mass[0] = self.T.Photon_mass[0]
             self.Photon_mvaID_WP80[0] = self.T.Photon_mvaID_WP80[0]
             self.Photon_mvaID_WP90[0] = self.T.Photon_mvaID_WP90[0]
             self.Photon_electronVeto[0] = self.T.Photon_electronVeto[0]
             self.Photon_pfRelIso03_all[0] = self.T.Photon_pfRelIso03_all[0]
#                    self.FatJet_phi[0] = self.T.FatJet_phi[0]
 #                   self.FatJet_pt[0] = self.T.FatJet_pt[0]
  #                  self.FatJet_eta[0] = self.T.FatJet_eta[0]
   #                 self.FatJet_mass[0] = self.T.FatJet_mass[0]
    #                self.FatJet_msoftdrop[0] = self.T.FatJet_msoftdrop[0]
     #               self.FatJet_jetId[0] = self.T.FatJet_jetId[0]
      #              self.FatJet_tau1[0] = self.T.FatJet_tau1[0]
       #             self.FatJet_tau2[0] = self.T.FatJet_tau2[0]
        #            self.FatJet_tau3[0] = self.T.FatJet_tau3[0]
         #           self.FatJet_tau4[0] = self.T.FatJet_tau4[0]
             self.tree.Fill()
                #self.tree.Print()

        self.total += self.T.GetEntries() 
        print "Percent Passed: %f%%" %(float(self.triggeredCounter)/float(self.total)*100)
        #F.cd()
        #F.Write()
        F.Close()
    
    def addBranch(self, name, obj, T):
        self.tree.Branch(name, obj, name +"/F")
    
#newTree = Tree("trees2018/TestCode100to200", "/cms/xaastorage/NanoAOD/2018/DEC18/2018_GJets_HT/GJets_HT-100To200/14CE32BF-31E1-9C4D-BAD9-1C31B1A0AF00.root/", 10125438.0/9238000.0, ["HLT_Photon110EB_TightID_TightIso"])

