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

void drawHist(char* BigHistname, char* SmallHistname, char* c)
{
  TFile* f1 = new TFile("BGHist.root");
  TFile* f2 = new TFile("Zp75Hist.root");
  TCanvas* c1 = new TCanvas(c, c, 10, 10, 700, 500);
  TH1F* input1;
  const char* histname = BigHistname;
  // input1 = (TH1F*) f1->Get(histname.c_str());
  f1->GetObject(histname,input1);
  TH1F* input2;
  const char* histname2 = SmallHistname;
  // input2 = (TH1F*) f2->Get(histname2);
  f2->GetObject(histname2,input2);

  c1->cd();
  c1->SetLogy();
  input1->GetYaxis()->SetRangeUser(1, 100000);
  input1->SetLineColor(kBlack);
  input1->SetFillColor(kAzure - 9);
  input1->SetLineWidth(3);
  input1->SetStats(0);
  input1->Draw("hist");
  input2->SetLineColor(kRed);
  input2->SetLineWidth(2);
  input2->Draw("hist same");
  TLegend* legend = new TLegend(.8, .7, .95, .9);
  legend->AddEntry(input1, "#gamma+jets MC", "f");
  legend->AddEntry(input2, "Z'_{75GeV}", "l");
  legend->SetBorderSize(0);
  legend->Draw();
  
}

#endif
