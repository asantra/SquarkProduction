### run like: python extractLog.py --short',

import os, sys, time, glob
import argparse


def getNEvents(gluonMass):
    nEvents = -1
    intMass = int(gluonMass)
    if (intMass <= 600):
        nEvents = 100000
    elif (intMass >= 800 and intMass <=1000):
        nEvents = 50000
    elif intMass >= 1200:
        nEvents = 10000
    
    return str(nEvents)

def getMasses(name):
    massValue = name.split('_SLN1_')[1]
    massValue = massValue.replace('_2L.py','')
    return massValue


def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--short', dest='shortJob', action='store_true')
    args = parser.parse_args()
    
    orderedJobOption = ['MC15.377783.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_600_100_2L.py',
    'MC15.377784.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_600_300_2L.py',
    'MC15.377785.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_600_400_2L.py',
    'MC15.377786.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_600_440_2L.py',
    'MC15.377787.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_600_480_2L.py',
    'MC15.377788.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_600_500_2L.py',
    'MC15.377789.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_600_520_2L.py',
    'MC15.377790.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_600_540_2L.py',
    'MC15.377791.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_600_560_2L.py',
    'MC15.377792.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_600_570_2L.py',
    'MC15.377793.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_800_100_2L.py',
    'MC15.377794.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_800_300_2L.py',
    'MC15.377795.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_800_500_2L.py',
    'MC15.377796.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_800_600_2L.py',
    'MC15.377797.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_800_640_2L.py',
    'MC15.377798.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_800_680_2L.py',
    'MC15.377799.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_800_700_2L.py',
    'MC15.377800.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_800_720_2L.py',
    'MC15.377801.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_800_740_2L.py',
    'MC15.377802.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_800_760_2L.py',
    'MC15.377803.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_800_770_2L.py',
    'MC15.377804.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1000_100_2L.py',
    'MC15.377805.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1000_300_2L.py',
    'MC15.377806.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1000_500_2L.py',
    'MC15.377807.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1000_700_2L.py',
    'MC15.377808.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1000_800_2L.py',
    'MC15.377809.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1000_840_2L.py',
    'MC15.377810.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1000_880_2L.py',
    'MC15.377811.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1000_900_2L.py',
    'MC15.377812.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1000_920_2L.py',
    'MC15.377813.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1000_940_2L.py',
    'MC15.377814.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1000_960_2L.py',
    'MC15.377815.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1000_970_2L.py',
    'MC15.377816.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1200_100_2L.py',
    'MC15.377817.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1200_300_2L.py',
    'MC15.377818.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1200_500_2L.py',
    'MC15.377819.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1200_700_2L.py',
    'MC15.377820.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1200_900_2L.py',
    'MC15.377821.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1200_1000_2L.py',
    'MC15.377822.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1200_1040_2L.py',
    'MC15.377823.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1200_1080_2L.py',
    'MC15.377824.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1200_1100_2L.py',
    'MC15.377825.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1200_1100_2L.py',
    'MC15.377826.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1200_1120_2L.py',
    'MC15.377827.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1200_1140_2L.py',
    'MC15.377828.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1200_1160_2L.py',
    'MC15.377829.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1200_1170_2L.py',
    'MC15.377830.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_100_2L.py',
    'MC15.377831.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_300_2L.py',
    'MC15.377832.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_500_2L.py',
    'MC15.377833.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_700_2L.py',
    'MC15.377834.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_900_2L.py',
    'MC15.377835.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_1100_2L.py',
    'MC15.377836.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_1200_2L.py',
    'MC15.377837.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_1240_2L.py',
    'MC15.377838.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_1280_2L.py',
    'MC15.377839.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_1300_2L.py',
    'MC15.377840.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_1300_2L.py',
    'MC15.377841.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_1320_2L.py',
    'MC15.377842.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_1340_2L.py',
    'MC15.377843.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_1360_2L.py',
    'MC15.377844.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_1370_2L.py',
    'MC15.377845.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_100_2L.py',
    'MC15.377846.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_300_2L.py',
    'MC15.377847.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_500_2L.py',
    'MC15.377848.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_700_2L.py',
    'MC15.377849.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_900_2L.py',
    'MC15.377850.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_1100_2L.py',
    'MC15.377851.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_1300_2L.py',
    'MC15.377852.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_1400_2L.py',
    'MC15.377853.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_1440_2L.py',
    'MC15.377854.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_1480_2L.py',
    'MC15.377855.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_1500_2L.py',
    'MC15.377857.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_1520_2L.py',
    'MC15.377858.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_1540_2L.py',
    'MC15.377859.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_1560_2L.py',
    'MC15.377860.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_1570_2L.py',
    'MC15.377867.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_100_2L.py',
    'MC15.377868.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_300_2L.py',
    'MC15.377869.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_500_2L.py',
    'MC15.377870.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_700_2L.py',
    'MC15.377871.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_900_2L.py',
    'MC15.377872.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_1100_2L.py',
    'MC15.377873.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_1300_2L.py',
    'MC15.377874.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_1500_2L.py',
    'MC15.377875.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_1640_2L.py',
    'MC15.377876.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_1680_2L.py',
    'MC15.377877.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_1700_2L.py',
    'MC15.377878.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_1720_2L.py',
    'MC15.377879.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_1740_2L.py',
    'MC15.377880.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_1760_2L.py',
    'MC15.377881.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_1770_2L.py',
    'MC15.377888.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2000_100_2L.py',
    'MC15.377889.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2000_300_2L.py',
    'MC15.377890.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2000_500_2L.py',
    'MC15.377891.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2000_700_2L.py',
    'MC15.377892.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2000_900_2L.py',
    'MC15.377893.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2000_1100_2L.py',
    'MC15.377894.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2000_1300_2L.py',
    'MC15.377895.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2000_1500_2L.py',
    'MC15.377896.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2000_1700_2L.py',
    'MC15.377897.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2000_1900_2L.py',
    'MC15.377904.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2200_100_2L.py',
    'MC15.377905.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2200_300_2L.py',
    'MC15.377906.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2200_500_2L.py',
    'MC15.377907.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2200_700_2L.py',
    'MC15.377908.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2200_900_2L.py',
    'MC15.377909.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2200_1100_2L.py',
    'MC15.377910.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2200_1300_2L.py',
    'MC15.377911.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2200_1500_2L.py',
    'MC15.377912.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2200_1700_2L.py',
    'MC15.377913.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2200_1900_2L.py',
    'MC15.377914.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2400_100_2L.py',
    'MC15.377915.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2400_300_2L.py',
    'MC15.377916.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2400_500_2L.py',
    'MC15.377917.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2400_700_2L.py',
    'MC15.377918.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2400_900_2L.py',
    'MC15.377919.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2400_1100_2L.py',
    'MC15.377920.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2400_1300_2L.py',
    'MC15.377921.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2400_1500_2L.py']
    
    
    parser      = argparse.ArgumentParser()
    parser.add_argument('--short', dest='shortJob', action='store_true')
    args        = parser.parse_args()
    
    
    outputFile  = open('summaryOfRuns.txt', 'w')
    cpuFile     = open('onlyCPUHours.txt','w')
    effFile     = open('onlyEfficiency.txt','w')
    xsecFile    = open('onlyXsec.txt','w')
    effLumiFile = open('onlyEffLumi.txt','w')
    passedFile  = open('onlyPassedEvents.txt','w')
    totalFile   = open('onlyTotalEvents.txt','w')
    
    
    outputFile.write("Mass Parameter\t\tCPU\t\txsec\t\tEffLumi\t\tEfficiency\t\tPassed events\t\tTotal events\n")
    outputFile.write("--------------\t\t---\t\t----\t\t-------\t\t----------\t\t-------------\t\t------------\n")
    
    
    counter = 0
    for jobOption in orderedJobOption:
        massValues  = getMasses(jobOption)
        massParam   = massValues.split('_')
        
        gluon       = massParam[0]
        slepton     = massParam[1]
        logFileBase = 'log.generate_'
        intGluon    = int(gluon)
        intSlepton  = int(slepton)
        
        if(abs(intGluon - intSlepton) < 41): continue
        
        endName = ""
        if((intGluon >= 600 and intGluon <= 2400) and abs(intGluon - intSlepton)<=200):
            endName   = "_100Events"
        elif((intGluon >= 600 and intGluon <= 2400) and abs(intGluon - intSlepton)<=800):
            endName   = "_200Events"
        else:
            endName   = "_500Events"
            
        logFileName = logFileBase+massValues+endName
            
        nEvents   = getNEvents(gluon)
        command   = 'python logParserSVN.py -i '+logFileName+' -N '+nEvents+' -u asantra --nosvn > checkLog.txt'
        print "+++++++++++++++++++++++++++++++++++++++++++++"
        print 'logFile considered: ', logFileName, ' for massValues: ', massValues
        
        os.system(command)
        
        outFile    = open('checkLog.txt','rb')
        cpuHour    = '-999'
        efficiency = '-1000'
        passed     = '-1000'
        total      = '-1000'
        xsec       = '-1000'
        effLumi    = '-1000'
        
        for line in outFile:
            if 'CPU' in line: 
                cpuHour = line.split()[3]
            if 'EvgenFilterSeq Filter Efficiency' in line: 
                efficiency = line.split()[5]
                passed     = line.split()[6].replace('[','')
                total      = line.split()[8].replace(']','')
            if 'cross-section' in line:
                xsec    = line.split()[4]
            if 'Effective lumi' in line:
                effLumi = line.split()[4]
        
        xsecInPb = xsec #str(float(xsec)*1000)
        outputFile.write(massValues+'\t\t'+cpuHour+'\t\t'+xsecInPb+'\t\t'+effLumi+'\t\t'+efficiency+'\t\t'+passed+'\t\t'+total+'\n')
        
        cpuFile.write(cpuHour+'\n')
        effFile.write(efficiency+'\n')
        xsecFile.write(xsecInPb+'\n')
        effLumiFile.write(effLumi+'\n')
        passedFile.write(passed+'\n')
        totalFile.write(total+'\n')
        
        counter += 1
        if(counter > 1 and args.shortJob):
            exit()
            
    outputFile.close()
    cpuFile.close()
    effFile.close()
    xsecFile.close()
    effLumiFile.close()
    passedFile.close()
    totalFile.close()
    
    
if __name__ == "__main__":
    start = time.time()
    main()
    print "The time taken: ", (time.time() - start)/60.0, " m"
    
