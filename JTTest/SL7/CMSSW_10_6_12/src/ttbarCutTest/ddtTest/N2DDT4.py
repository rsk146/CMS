import ROOT
from ROOT import *
import os
import sys
import math
from vetos import histDraw
from histDraw import Hist_Setup
from CutoffEfficient import Cutoffs

def kinematics_draw(passs, fail, out):
    gjetsAK8pt = passs.Histo1D(("GJetsAK8PtHist", "AK8 p_{T};p_{T} (GeV)", 50, 0, 800.0 ), "AK8_pt", "weight")
    gjetsAK8eta = passs.Histo1D(("GJetsAK8eta", "AK8 #eta;AK8 #eta", 60, -3.0, 3.0), "AK8_eta", "weight")
    gjetsAK8SDM = passs.Histo1D(("GJetsAK8SDM", "AK8 Soft Drop Mass;Soft Drop Mass (GeV)", 50, 0.0, 200.0), "AK8_msoftdrop", "weight")
    gjetsAK8rho = passs.Histo1D(("GJetsAK8Rho", "Rho ;Rho", 50, -7, -2), "AK8_rho", "weight")
    gjetspt = passs.Histo1D(("GJetsPt", "Photon p_{T}; Photon p_{T} (GeV)", 50, 0.0, 1600.), "Photon_pt", "weight")
    gjetseta = passs.Histo1D(("GJetsEta", "Photon #eta; Photon #eta", 60, -3.0, 3.0), "Photon_eta", "weight")

    gjetsAK8ptfail = fail.Histo1D(("GJetsAK8PtHist", "AK8 p_{T};p_{T} (GeV)", 50, 0, 800.0 ), "AK8_pt", "newWeight")
    gjetsAK8etafail = fail.Histo1D(("GJetsAK8eta", "AK8 #eta;AK8 #eta", 60, -3.0, 3.0), "AK8_eta", "newWeight")
    gjetsAK8SDMfail = fail.Histo1D(("GJetsAK8SDM", "AK8 Soft Drop Mass;Soft Drop Mass (GeV)", 50, 0.0, 200.0), "AK8_msoftdrop", "newWeight")
    gjetsAK8rhofail = fail.Histo1D(("GJetsAK8Rho", "Rho ;Rho", 50, -7, -2), "AK8_rho", "newWeight")
    gjetsptfail = fail.Histo1D(("GJetsPt", "Photon p_{T}; Photon p_{T} (GeV)", 50, 0.0, 1600.), "Photon_pt", "newWeight")
    gjetsetafail = fail.Histo1D(("GJetsEta", "Photon #eta; Photon #eta", 60, -3.0, 3.0), "Photon_eta", "newWeight")

    hist_draw(gjetsAK8pt, gjetsAK8ptfail, "jet pt", out)
    hist_draw(gjetsAK8eta, gjetsAK8etafail, "jet eta", out)
    hist_draw(gjetsAK8SDM, gjetsAK8SDMfail, "sdm", out)
    hist_draw(gjetsAK8rho, gjetsAK8rhofail, "rho", out)
    hist_draw(gjetspt, gjetsptfail, "photon pt", out)
    hist_draw(gjetseta, gjetsetafail, "photon eta", out)

def hist_draw(passs, fail, var, out):
    print var + " Integral:" + str(passs.Integral())
    C = ROOT.TCanvas(var, var)
    C.cd()
    p1 = ROOT.TPad("pad1", "tall", 0, 0.35, 1, 1)
    p2 = ROOT.TPad("pad2", "short", 0, 0.0, 1.0, 0.325)
    p2.SetBottomMargin(0.35)
    p1.Draw()
    p2.Draw()

    #top
    p1.cd()
    passs.SetMarkerStyle(kFullCircle)
    passs.SetLineColor(kBlack)
    passs.SetStats(0)
    passs.Draw()

    fail.SetLineColor(kBlue)
    fail.SetLineWidth(2)
    fail.Draw("samehist")

    p1.RedrawAxis()

    legend = TLegend(.7, .7, .9, .9)
    legend.AddEntry(passs.GetValue(), "Events Passing N_{2}DDT", "lep")
    legend.AddEntry(fail.GetValue(), "#frac{1}{9} #times Events Failing N_{2}DDT", "l")
    legend.Draw()

    #bottom
    p2.cd()
    rp = passs.Clone("Ratio")
    rp.Reset()
    rp.SetStats(0)
    for bin in range(passs.GetNbinsX()):
        err = passs.GetBinError(bin+1)
        if err == 0: continue
        val = (passs.GetBinContent(bin+1) - fail.GetBinContent(bin+1)) / err
        rp.SetBinContent(bin+1, val)
        rp.SetBinError(bin+1, math.sqrt(abs(rp.GetBinContent(bin+1))))
    rp.SetTitleSize(.07, "x")
    rp.GetXaxis().SetLabelSize(.07)
    rp.GetYaxis().SetLabelSize(.07)
    rp.SetMarkerStyle(kFullCircle)
    rp.SetLineColor(kBlack)
    rp.Draw("")
    p2.RedrawAxis()

    #save
    C.Update()
    C.Modified()
    out.cd()
    C.Write()

    
    #bottom
    '''p2.cd()
    comparison = passs.Clone("Comp")
    comparison.Reset()
    comparison.SetStats(0)
    for bin in range(passs.GetNbinsX()):
        if passs.GetBinContent(bin+1) == 0: continue
        val = (passs.GetBinContent(bin+1) - fail.GetBinContent(bin+1))/passs.GetBinContent(bin+1)
        comparison.SetBinContent(bin+1, val)
    comparison.SetTitleSize(.07, "x")
    comparison.GetXaxis().SetLabelSize(0.07)
    comparison.GetYaxis().SetLabelSize(.07)
    comparison.SetMarkerStyle(kFullCircle)
    comparison.SetLineColor(kBlack)
    comparison.Draw()
    p2.RedrawAxis()'''

    #save
    '''ROOT.gStyle.SetOptStat(0)
    passs.SetStats(0)
    passs.SetLineColor(kBlack)
    fail.SetLineColor(kBlue)
    fail.SetLineWidth(2)

    rp = TRatioPlot(passs.GetValue(), fail.GetValue(), "diffsigerrasym")
    rp.SetH1DrawOpt("")
    rp.SetH2DrawOpt("hist")
    rp.Draw()
    legend = TLegend(.7, .7, .9, .9)
    legend.AddEntry(passs.GetValue(), "Events Passing N_{2}DDT", "lep")
    legend.AddEntry(fail.GetValue(), "#frac{1}{9} #times Events Failing N_{2}DDT", "l")
    rp.GetUpperPad().cd()
    legend.Draw()'''
    '''p1.cd()
    passs.SetMarkerStyle(kFullCircle)
    passs.SetStats(0)
    passs.Draw()

    fail.SetLineColor(kBlue)
    fail.SetLineWidth(2)
    fail.Draw("samehist")

    
    p1.RedrawAxis()'''
    #rp.Draw()

    


if __name__ == "__main__":
    out = ROOT.TFile("PassFailNew.root", "RECREATE")
    ROOT.ROOT.EnableImplicitMT()
    RDF = ROOT.ROOT.RDataFrame
    gjets = RDF("tree", sys.argv[1])
    hists3 = [[TH1F(str(i) + ", " + str(j), "N2 with Cuts; N2; Events", 50, 0., .5) for j in range(16)] for i in range(16)]
    test3 = Cutoffs("N210gjets", sys.argv[1], hists3, "gjets")
    cutoff_hist3 = TH2F(test3.cutoffHist)
    ROOT.gInterpreter.ProcessLine("auto cutoff3 = Cutoffsgjets;")
    fancy_code3 = '''
                        float ddt3(float pt, float rho, float n2)
                        {   
                            int xbin = cutoff3->GetXaxis()->FindBin(rho);
                            int ybin = cutoff3->GetYaxis()->FindBin(pt);
                            return n2 - cutoff3->GetBinContent(xbin, ybin);
                        }
                        '''
    ROOT.gInterpreter.Declare(fancy_code3)
    gjetsC = gjets.Filter("AK8_rho >= -7. && AK8_rho <= -2.")
    n2gjets = gjetsC.Define("N2DDT", "ddt3(AK8_pt, AK8_rho, AK8_n2)")
    gjetsfail = n2gjets.Filter("N2DDT > 0 && AK8_pt > 200")
    gjetspass = n2gjets.Filter("N2DDT < 0 && AK8_pt > 200")
    gjetsfailweight = n2gjets.Define("newWeight", "1.0/9.0*weight")

    kinematics_draw(gjetspass, gjetsfailweight, out)

    #p/f Factor creation
    basemap_Pass = gjetspass.Histo2D(("Base_Map_Pass", "Base Map; rho; pt", 16, -7, -2, 16, 200, 800), "AK8_rho", "AK8_pt", "weight")
    basemap_Fail = gjetsfail.Histo2D(("Base_Map_Fail", "Base Map; rho; pt", 16, -7, -2, 16, 200, 800), "AK8_rho", "AK8_pt", "weight")


    R_Factor = TH2F("R_Factor", "R_Factor; Rho; p_{T} (GeV)", 16, -7, -2, 10, 200, 1600)
    for i in range(1,17):
        for j in range(1, 17):
            passVal = basemap_Pass.GetBinContent(i, j)
            failVal = basemap_Fail.GetBinContent(i, j)
            if failVal == 0: continue
            #print float(passVal)/float(failVal)
            R_Factor.SetBinContent(i,j, float(passVal)/float(failVal))
    C = ROOT.TCanvas("R Factor", "R Factor")
    C.cd()
    R_Factor.SetStats(0)
    R_Factor.GetYaxis().SetTitleOffset(2)
    R_Factor.GetXaxis().SetTitleOffset(2)
    R_Factor.Draw("SURF1")
    out.cd()
    C.Write()
    out.Close()