#!/usr/bin/env python
import sys
sys.argv.append('-b')
from ROOT import *

gROOT.ProcessLine('.L ./tdrstyle.C')
setTDRStyle()
TH1.SetDefaultSumw2(kTRUE)
TH2.SetDefaultSumw2(kTRUE)
TProfile.SetDefaultSumw2(kTRUE)

PlotList = ['h2_MassVsME_']
catList = ['','CAT1','CAT2','CAT3','CAT4']

myFileData= TFile('../HiggsZGAnalyzer/batchHistos/higgsHistograms_MuMu2012ABCD_ME_plots.root','r')
myFileSignal= TFile('../HiggsZGAnalyzer/localHistos/higgsHistograms_ggM125_8TeV_pythia8_175_v2_mumuGamma_local.root','r')
can= TCanvas('can','canvas',800,600)
can.SetRightMargin(0.1)
can.cd()

for cat in catList:
  h2HistData = myFileData.Get(PlotList[0]+cat+'_DATA')
  h2HistData.Draw('colz')
  can.SaveAs('MEPlots/MassVsME_2D_Data'+cat+'.pdf')

  h2HistSignal = myFileSignal.Get(PlotList[0]+cat+'_Signal2012ggM125')
  h2HistSignal.Draw('colz')
  can.SaveAs('MEPlots/MassVsME_2D_Signal'+cat+'.pdf')

h2HistData = myFileData.Get(PlotList[1]+'DATA')
h2HistData.Draw('colz')
can.SaveAs('MEPlots/MassVsME_2D_Data.pdf')
f_data = open('MEPlots/MassVsME_2D_Data.txt','w')
f_data.write('2D data, Muon channel, low edge of bin values given for x and y axes\n')
f_data.write('Mass (GeV), Disc, nEvent\n')

for i in range(1,h2HistData.GetNbinsX()+1):
  for j in range(1,h2HistData.GetNbinsY()+1):
    print h2HistData.GetXaxis().GetBinLowEdge(i), h2HistData.GetYaxis().GetBinLowEdge(j), h2HistData.GetBinContent(i,j)
    f_data.write('{0:}, {1:.3}, {2}\n'.format(h2HistData.GetXaxis().GetBinLowEdge(i), h2HistData.GetYaxis().GetBinLowEdge(j), h2HistData.GetBinContent(i,j)))

f_data.close()


h2HistSignal = myFileSignal.Get(PlotList[1]+'Signal2012ggM125')
h2HistSignal.Draw('colz')
can.SaveAs('MEPlots/MassVsME_2D_Signal.pdf')
f_signal = open('MEPlots/MassVsME_2D_Signal.txt','w')
f_signal.write('2D signal (scaled to L and XS), Muon channel, low edge of bin values given for x and y axes\n')
f_signal.write('Mass (GeV), Disc, nEvent\n')

for i in range(1,h2HistSignal.GetNbinsX()+1):
  for j in range(1,h2HistSignal.GetNbinsY()+1):
    print h2HistSignal.GetXaxis().GetBinLowEdge(i), h2HistSignal.GetYaxis().GetBinLowEdge(j), h2HistSignal.GetBinContent(i,j)*0.00059555
    f_signal.write('{0:}, {1:.3}, {2}\n'.format(h2HistSignal.GetXaxis().GetBinLowEdge(i), h2HistSignal.GetYaxis().GetBinLowEdge(j), h2HistSignal.GetBinContent(i,j)*0.00059555))

f_signal.close()
