#ifndef TWODHISTDRAW_H
#define TWODHISTDRAW_H
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

void drawHist(char* BigHistname, char*c)
{
  TFile* f1 = new TFile("BGHist.root");
  TCanvas* c1 = new TCanvas(c, c, 10, 10, 700, 500);
  TH2F* input1;
  const char* histname = BigHistname;
  f1->GetObject(histname,input1);
  c1->cd();
  input1->Draw("colz");
  input1->SetStats(0);
}
#endif
