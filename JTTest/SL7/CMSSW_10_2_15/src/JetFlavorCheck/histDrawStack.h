 #ifndef HISTDRAW_H
#define HISTDRAW_H
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
#include "TPaveText.h"
#include <TROOT.h>
#include <string>

void drawHist(char* AllHists, char* five, char* four, char* three, char* two, char* twentyone, char* c)
{
  TFile* f1 = new TFile("ttbarFlavorCuts.root");
  TCanvas* c1 = new TCanvas(c, c, 10, 10, 700, 500);
  TH1F* input1;
  const char* histname = AllHists;
  f1->GetObject(histname,input1);
  TH1F* input2;
  const char* histname2 = five;
  f1->GetObject(histname2,input2);
  TH1F* input3;
  const char* histname3 = four;
  f1->GetObject(histname3, input3);
  TH1F* input4;
  const char* histname4 = three;
  f1->GetObject(histname4, input4);
  TH1F* input5;
  const char* histname5 = two;
  f1->GetObject(histname5, input5);
  TH1F* input6;
  const char* histname6 = twentyone;
  f1->GetObject(histname6, input6);
  
  
  c1->cd();
  gPad->SetLogy();
  input1->SetTitle("Parton Stack");
  input1->SetLineColor(kBlack);
  input1->SetLineWidth(2);
  input1->SetStats(0);
  input1->GetXaxis()->SetTitle("SDM [GeV]");
  input1->SetMinimum(10);
  //input1->GetYaxis()->SetMinimum(.001);
  //c1->SetLogy();
  //input1->GetXaxis()->SetRangeUser(0, 200);
  //input1->Scale(1/(input1->Integral()));
  input1->Draw("hist");
  input2->SetLineColor(kGreen +2);
  input2->SetLineWidth(2);
  //input4->Scale(1/(input4->Integral()));
  input2->Draw("hist same");
  input3->SetLineColor(kViolet+1);
  input3->SetLineWidth(2);
  //input5->Scale(1/(input5->Integral()));
  input3->Draw("hist same");
  //input3->SetFillColor(kGray);
  //input2->Scale(1/(input2->Integral()));
  //input3->Draw("hist same");
  input4->SetLineColor(kMagenta);
  input4->SetLineWidth(2);
  //input3->Scale(1/(input3->Integral()));
  input4->Draw("hist same");
  input5->SetLineColor(kRed);
  input5->SetLineWidth(2);
  input5->Draw("hist same");
  input6->SetLineColor(kAzure);
  input6->SetLineWidth(2);
  input6->Draw("hist same");
  TLegend* legend = new TLegend(.7, .6, .87, .87);
  legend->SetLineColor(0);
  legend->AddEntry(input1, "All Partons", "f");
  legend->AddEntry(input2, "21,1,2,3,4", "f");
  legend->AddEntry(input3, "21,1,2,3", "f");
  legend->AddEntry(input4, "21,1,2", "f"); 
  legend->AddEntry(input5, "21,1", "f");
  legend->AddEntry(input6, "21", "f");
  legend->Draw();
  
}

#endif
