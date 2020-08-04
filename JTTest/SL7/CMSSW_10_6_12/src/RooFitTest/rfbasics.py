import ROOT

x = ROOT.RooRealVar("x", "x", -10, 10)
mean = ROOT.RooRealVar("mean", "mean of gaussian",1, -10, 10)
sigma = ROOT.RooRealVar("sigma", "width of gaussian", 1, .1, 10)

gauss = ROOT.RooGaussian("gauss", "gaussian pdf", x, mean, sigma)

xframe = x.frame(ROOT.RooFit.Title("Gaussian pdf"))

gauss.plotOn(xframe)
sigma.setVal(3)
gauss.plotOn(xframe, ROOT.RooFit.LineColor(ROOT.kRed))


data = gauss.generate(ROOT.RooArgSet(x), 10000)

xframe2 = x.frame(ROOT.RooFit.Title("Gaussian pdf with data"))
data.plotOn(xframe2)
gauss.plotOn(xframe2)

gauss.fitTo(data)

mean.Print()
sigma.Print()

c = ROOT.TCanvas("rf basic", "rf basic", 800, 400)
c.Divide(2)
c.cd(1)
ROOT.gPad.SetLeftMargin(0.15)
xframe.GetYaxis().SetTitleOffset(1.6)
xframe.Draw()
c.cd(2)
ROOT.gPad.SetLeftMargin(.15)
xframe2.GetYaxis().SetTitleOffset(1.6)
xframe2.Draw()

c.SaveAs("rf101.png")