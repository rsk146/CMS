#include "histDraw.h"

void histoDraw(){
  // drawHist((char*)"BGFatJetTau21", (char*) "FatJetTau21", (char*) "c7"); 
  drawHist((char*)"BGPhotonPt", (char*) "PhotonPt", (char*) "c1");
  drawHist((char*)"BGPhotonEta", (char*) "PhotonEta", (char*) "c2");
  drawHist((char*)"BGFatJetRho", (char*) "FatJetRho", (char*) "c3");
  drawHist((char*)"BGFatJetPt", (char*) "FatJetPt", (char*) "c4");
  drawHist((char*)"BGFatJetEta", (char*) "FatJetEta", (char*) "c5");
  drawHist((char*)"BGFatJetSDM", (char*) "FatJetSDM", (char*) "c6");
  drawHist((char*)"BGFatJetTau21", (char*) "FatJetTau21", (char*) "c8");
}
