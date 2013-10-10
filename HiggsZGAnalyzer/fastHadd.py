#!/usr/bin/env python
import sys, os, glob

#useage:
# ./fastHadd.py tag

def fastHadd():
  if len(sys.argv) != 2:
    print 'usage: ./fastHadd.py tag'

  if not os.path.isfile('.checkfile.txt'):
    print 'where is the .checkfile.txt?! you fucked something up, I aint hadding shit. fuck you, do it yourself.'
    return

  year = '2012ABCD'
  infile = open('.checkfile.txt','r')
  for line in infile:
    selectionList = line.split()
    if selectionList[0] == 'mumuGamma':
      leptonA = 'MuMu'
      leptonB = 'mumuGamma'
    elif selectionList[0] == 'eeGamma_Combined':
      leptonA = 'EE'
      leptonB = 'eeGamma'
    tag = sys.argv[1]

    os.system('./hadd.py ForStoyan/higgsHistograms_'+leptonA+year+'_Limits_'+tag+'.root '+leptonB+' File {0}'.format(' '.join(selectionList[1:])))
    os.system('./hadd.py ~/afsHome/public/m_llgFile_'+leptonA+year+'_'+tag+'.root '+leptonB+' m_llgFile {0}'.format(' '.join(selectionList[1:])))
    os.system('./hadd.py batchHistos/higgsHistograms_'+leptonA+year+'_'+tag+'.root '+leptonB+' Histograms {0}'.format(' '.join(selectionList[1:])))

  dataDumpList = glob.glob('dumps/dataDump*.txt')
  if len(dataDumpList) >0:
    with open('dumps/CombDataDump_'+leptonB+'_'+tag+'.txt','w') as f:
      for dump in dataDumpList:
        with open(dump) as ftemp:
          for line in ftemp:
            f.write(line)
    f.close()

    os.system('rm dumps/dataDump*.txt')


if __name__=="__main__":
  fastHadd()

#hadd -f otherHistos/eleSmear2011.root ~/nobackup/BatchOutput/eeGamma_Combined/eleSmearFile_*
#./hadd.py ForStoyan/higgsHistograms_MuMu2011_Limits_Nominal_LowR9.root mumuGamma File Run2011A Run2011B ggHZG_M120 ggHZG_M125 ggHZG_M130 ggHZG_M135 ggHZG_M140 vbfHZG_M120 vbfHZG_M125 vbfHZG_M130 vbfHZG_M135 vbfHZG_M140

