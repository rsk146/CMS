#include <iostream>
#include <fstream>
#include <TFile.h>
#include "TH1.h"
#include <TF1.h>
#include "TCanvas.h"
#include "TLegend.h"
#include "TGraph.h"
#include "TGraphAsymmErrors.h"
#include "TLine.h"
#include "TMath.h"
#include <TROOT.h>
#include <string>
#include "TTree.h"


void BothCuts(char* outputFileName, char* inputfile, char* histFile)
{
  TFile* f1 = new TFile(outputFileName, "recreate");
  TFile* f2 = new TFile(inputfile);
  TFile* f3 = new TFile(histFile);
  f1->cd();
  TTree* T;
  f2->GetObject("tree", T);
  TH1F* h1 = new TH1F("Tau21Effic", "Tau21 Efficiency; #tau_{2}/#tau_{1}; Efficiency", 50, 0., 1.);
  double finalArray[16][16];
  double ptMax = 237.5;
  double rhoMax = -6.6875;
  Long64_t nentries = T->GetEntries();
  for(int ptCounter = 0; ptCounter < 16; ptCounter++){
    for(int rhoCounter = 0; rhoCounter < 16; rhoCounter++){
      for(Long64_t entry =0; entry < nentries; entry++){
	T->GetEntry(entry);
	finalArray[ptCounter][rhoCounter] = FatJet_pt[0];
      }
    }
  }
  for(int i =0; i < 16; i ++){
    for(int j = 0; j < 16; j ++){
      std::cout <<finalArray[i][j] << ' ';
    }
    std::cout <<std::endl;
  }
}
