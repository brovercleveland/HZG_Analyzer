#!/usr/bin/env python
import sys,os
sys.argv.append('-b')
from PlottingClasses import *
from ROOT import *
import numpy as np

gROOT.ProcessLine('.L ./tdrstyle.C')
setTDRStyle()

def GenericPlotter(folder):
  if os.environ.get('AT_NWU') == None:
    FileMu= TFile("/uscms_data/d2/bpollack/CMSSW_5_3_8_patch1/src/HZG_Analyzer/HiggsZGAnalyzer/batchHistos/higgsHistograms_MuMu2012ABCD_10-17-13.root")
  else:
    FileMu= TFile("/tthome/bpollack/CMSSW_5_3_11_patch6/src/HZG_Analyzer/HiggsZGAnalyzer/batchHistos/higgsHistograms_MuMu2012ABCD_10-23-13.root")

  plotter = Plotter(FileMu, folder, folder, '2012','mu','Signal2012ggM125p8')
  for key in plotter.folderDict.keys():
    plotter.DataBGComp(plotter.folderDict[key])
    plotter.DataBGComp2DProj(plotter.folderDict[key])
    #splotter.DataBGComp2DProj(plotter.folderDict[key],125)

def ROCPlotter():
  if os.environ.get('AT_NWU') == None:
    FileMu= TFile("/uscms_data/d2/bpollack/CMSSW_5_3_8_patch1/src/HZG_Analyzer/HiggsZGAnalyzer/batchHistos/higgsHistograms_MuMu2012ABCD_10-17-13.root")
  else:
    FileMu= TFile("/tthome/bpollack/CMSSW_5_3_11_patch6/src/HZG_Analyzer/HiggsZGAnalyzer/batchHistos/higgsHistograms_MuMu2012ABCD_10-23-13.root")

  plotter = Plotter(FileMu, 'MEPlots', 'ROC', '2012','mu','Signal2012ggM125p8')
  for key in plotter.folderDict.keys():
    plotter.ROCcurves(plotter.folderDict[key])
    plotter.ROCcurves(plotter.folderDict[key],125)

def RatioPlotter():
  if os.environ.get('AT_NWU') == None:
    FileMu= TFile("/uscms_data/d2/bpollack/CMSSW_5_3_8_patch1/src/HZG_Analyzer/HiggsZGAnalyzer/batchHistos/higgsHistograms_MuMu2012ABCD_10-17-13.root")
  else:
    FileMu= TFile("/tthome/bpollack/CMSSW_5_3_11_patch6/src/HZG_Analyzer/HiggsZGAnalyzer/batchHistos/higgsHistograms_MuMu2012ABCD_10-23-13.root")

  plotter = Plotter(FileMu, 'PreGen', 'Ratio', '2012','mu','Signal2012ggM125p8')
  for key in plotter.folderDict.keys():
    plotter.RatioPlots(plotter.folderDict[key],'Signal2012ggM125p6','Signal2012ggM125p8')


if __name__=="__main__":
  print 'executing', sys.argv[1]
  if 'plot' == sys.argv[1]:
    GenericPlotter(sys.argv[2])
  elif 'ROC' == sys.argv[1]:
    ROCPlotter()
  elif 'Ratio' == sys.argv[1]:
