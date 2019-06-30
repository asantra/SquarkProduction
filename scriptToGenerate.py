### run like: python scriptToGenerate.py

import os, sys, time
import argparse


def getMasses(stringName):
    massString  = stringName.split('_')
    gluonMass   = massString[6]
    sleptonMass = massString[7]
    return [gluonMass, sleptonMass]

def getDSID(stringName):
    dsidString  = stringName.split('.')
    DSID        = dsidString[3]
    return DSID



def getLHEFileStar(mass):
    massDict = {}
    
    massDict['600'] = 'TXT.16061992._000418.tar.*'
    massDict['800'] = 'TXT.16062006._000025.tar.*'
    massDict['1000'] = 'TXT.16062025._000135.tar.*'
    massDict['1200'] = 'TXT.16062036._000086.tar.*'
    massDict['1400'] = 'TXT.16062052._000205.tar.*'
    massDict['1600'] = 'TXT.16062065._000012.tar.*'
    massDict['1700'] = 'TXT.16062072._000009.tar.*'
    massDict['1800'] = 'TXT.16062080._000010.tar.*'
    massDict['1900'] = 'TXT.16062086._000005.tar.*'
    massDict['2000'] = 'TXT.16062094._000002.tar.*'
    massDict['2200'] = 'TXT.16062101._000003.tar.*'
    massDict['2400'] = 'TXT.16062109._000002.tar.*'
    massDict['2600'] = 'TXT.16062116._000008.tar.*'
    
    return massDict[mass]

def getLHEFile(mass):
    massDict = {}
    
    massDict['600'] = 'TXT.16061992._000418.tar.gz.1'
    massDict['800'] = 'TXT.16062006._000025.tar.gz.1'
    massDict['1000'] = 'TXT.16062025._000135.tar.gz.1'
    massDict['1200'] = 'TXT.16062036._000086.tar.gz.1'
    massDict['1400'] = 'TXT.16062052._000205.tar.gz.1'
    massDict['1600'] = 'TXT.16062065._000012.tar.gz.1'
    massDict['1700'] = 'TXT.16062072._000009.tar.gz.1'
    massDict['1800'] = 'TXT.16062080._000010.tar.gz.1'
    massDict['1900'] = 'TXT.16062086._000005.tar.gz.1'
    massDict['2000'] = 'TXT.16062094._000002.tar.gz.1'
    massDict['2200'] = 'TXT.16062101._000003.tar.gz.1'
    massDict['2400'] = 'TXT.16062109._000002.tar.gz.1'
    massDict['2600'] = 'TXT.16062116._000008.tar.gz.1'
    
    return massDict[mass]





def main():
    
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--short', dest='shortJob', action='store_true')
    args = parser.parse_args()
    
    if not os.path.exists("logDirectory"):
        os.makedirs("logDirectory")
        
    if not os.path.exists("rootDirectory"):
        os.makedirs("rootDirectory")
    
    
    ### old list from CVMFS without MET100 filter
    #jobOptionsList = [
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377783.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_600_100_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377784.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_600_300_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377785.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_600_400_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377786.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_600_440_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377787.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_600_480_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377788.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_600_500_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377789.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_600_520_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377790.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_600_540_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377791.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_600_560_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377792.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_600_570_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377793.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_800_100_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377794.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_800_300_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377795.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_800_500_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377796.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_800_600_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377797.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_800_640_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377798.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_800_680_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377799.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_800_700_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377800.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_800_720_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377801.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_800_740_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377802.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_800_760_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377803.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_800_770_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377804.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1000_100_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377805.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1000_300_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377806.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1000_500_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377807.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1000_700_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377808.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1000_800_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377809.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1000_840_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377810.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1000_880_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377811.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1000_900_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377812.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1000_920_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377813.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1000_940_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377814.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1000_960_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377815.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1000_970_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377816.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1200_100_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377817.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1200_300_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377818.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1200_500_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377819.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1200_700_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377820.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1200_900_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377821.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1200_1000_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377822.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1200_1040_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377823.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1200_1080_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377824.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1200_1100_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377825.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1200_1100_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377826.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1200_1120_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377827.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1200_1140_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377828.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1200_1160_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377829.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1200_1170_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377830.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_100_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377831.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_300_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377832.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_500_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377833.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_700_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377834.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_900_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377835.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_1100_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377836.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_1200_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377837.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_1240_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377838.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_1280_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377839.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_1300_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377840.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_1300_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377841.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_1320_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377842.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_1340_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377843.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_1360_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377844.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1400_1370_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377845.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_100_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377846.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_300_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377847.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_500_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377848.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_700_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377849.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_900_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377850.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_1100_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377851.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_1300_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377852.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_1400_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377853.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_1440_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377854.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_1480_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377855.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_1500_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377856.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_1500_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377857.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_1520_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377858.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_1540_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377859.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_1560_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377860.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1600_1570_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377861.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1700_100_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377862.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1700_300_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377863.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1700_500_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377864.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1700_700_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377865.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1700_900_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377866.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1700_1100_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377867.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_100_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377868.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_300_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377869.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_500_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377870.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_700_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377871.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_900_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377872.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_1100_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377873.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_1300_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377874.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_1500_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377875.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_1640_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377876.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_1680_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377877.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_1700_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377878.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_1720_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377879.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_1740_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377880.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_1760_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377881.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1800_1770_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377882.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1900_100_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377883.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1900_300_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377884.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1900_500_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377885.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1900_700_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377886.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1900_900_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377887.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_1900_1100_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377888.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2000_100_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377889.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2000_300_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377890.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2000_500_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377891.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2000_700_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377892.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2000_900_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377893.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2000_1100_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377894.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2000_1300_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377895.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2000_1500_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377896.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2000_1700_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377897.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2000_1900_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377904.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2200_100_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377905.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2200_300_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377906.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2200_500_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377907.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2200_700_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377908.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2200_900_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377909.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2200_1100_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377910.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2200_1300_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377911.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2200_1500_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377912.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2200_1700_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377913.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2200_1900_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377914.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2400_100_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377915.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2400_300_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377916.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2400_500_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377917.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2400_700_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377918.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2400_900_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377919.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2400_1100_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377920.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2400_1300_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377921.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2400_1500_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377922.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2600_100_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377923.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2600_300_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377924.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2600_500_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377925.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2600_700_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377926.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2600_900_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377927.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2600_1100_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377928.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2600_1300_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377929.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2600_1500_2L.py',
    #'/cvmfs/atlas.cern.ch/repo/sw/Generators/MC15JobOptions/latest/share/DSID377xxx/MC15.377930.MGPy8EG_A14N23LO_SM_GG_N2_SLN1_2600_1700_2L.py'
    #]
    
    
    ## new list with ZN1 staying locally
    jobOptionsList = [
    '../mc15joboptions/share/DSID377xxx/MC15.377783.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_600_100_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377784.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_600_300_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377785.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_600_400_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377786.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_600_440_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377787.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_600_480_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377788.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_600_500_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377789.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_600_520_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377790.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_600_540_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377791.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_600_560_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377792.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_600_570_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377922.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_600_576_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377923.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_600_580_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377924.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_600_584_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377925.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_600_588_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377793.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_800_100_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377794.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_800_300_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377795.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_800_500_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377796.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_800_600_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377797.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_800_640_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377798.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_800_680_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377799.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_800_700_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377800.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_800_720_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377801.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_800_740_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377802.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_800_760_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377803.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_800_770_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377926.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_800_776_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377927.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_800_780_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377928.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_800_784_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377929.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_800_788_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377804.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1000_100_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377805.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1000_300_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377806.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1000_500_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377807.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1000_700_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377808.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1000_800_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377809.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1000_840_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377810.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1000_880_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377811.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1000_900_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377812.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1000_920_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377813.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1000_940_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377814.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1000_960_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377815.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1000_970_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377930.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1000_976_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377931.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1000_980_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377932.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1000_984_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377933.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1000_988_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377816.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1200_100_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377817.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1200_300_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377818.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1200_500_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377819.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1200_700_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377820.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1200_900_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377821.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1200_1000_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377822.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1200_1040_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377823.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1200_1080_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377824.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1200_1100_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377825.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1200_1100_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377826.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1200_1120_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377827.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1200_1140_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377828.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1200_1160_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377829.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1200_1170_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377934.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1200_1176_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377935.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1200_1180_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377936.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1200_1184_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377937.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1200_1188_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377830.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1400_100_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377831.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1400_300_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377832.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1400_500_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377833.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1400_700_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377834.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1400_900_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377835.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1400_1100_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377836.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1400_1200_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377837.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1400_1240_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377838.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1400_1280_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377839.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1400_1300_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377840.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1400_1300_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377841.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1400_1320_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377842.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1400_1340_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377843.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1400_1360_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377844.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1400_1370_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377938.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1400_1376_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377939.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1400_1380_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377940.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1400_1384_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377941.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1400_1388_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377845.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1600_100_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377846.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1600_300_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377847.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1600_500_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377848.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1600_700_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377849.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1600_900_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377850.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1600_1100_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377851.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1600_1300_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377852.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1600_1400_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377853.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1600_1440_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377854.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1600_1480_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377855.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1600_1500_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377856.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1600_1500_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377857.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1600_1520_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377858.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1600_1540_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377859.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1600_1560_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377860.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1600_1570_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377942.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1600_1576_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377943.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1600_1580_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377944.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1600_1584_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377945.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1600_1588_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377861.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1700_100_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377862.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1700_300_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377863.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1700_500_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377864.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1700_700_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377865.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1700_900_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377866.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1700_1100_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377867.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1800_100_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377868.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1800_300_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377869.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1800_500_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377870.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1800_700_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377871.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1800_900_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377872.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1800_1100_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377873.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1800_1300_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377874.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1800_1500_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377875.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1800_1640_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377876.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1800_1680_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377877.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1800_1700_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377878.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1800_1720_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377879.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1800_1740_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377880.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1800_1760_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377881.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1800_1770_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377946.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1800_1776_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377947.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1800_1780_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377948.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1800_1784_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377949.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1800_1788_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377882.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1900_100_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377883.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1900_300_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377884.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1900_500_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377885.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1900_700_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377886.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1900_900_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377887.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_1900_1100_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377888.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2000_100_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377889.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2000_300_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377890.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2000_500_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377891.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2000_700_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377892.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2000_900_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377893.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2000_1100_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377894.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2000_1300_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377895.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2000_1500_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377896.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2000_1700_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377897.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2000_1900_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377950.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2000_1960_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377951.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2000_1970_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377952.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2000_1976_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377953.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2000_1980_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377954.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2000_1984_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377955.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2000_1988_2LMET100_MadSpin.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377904.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2200_100_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377905.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2200_300_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377906.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2200_500_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377907.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2200_700_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377908.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2200_900_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377909.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2200_1100_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377910.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2200_1300_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377911.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2200_1500_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377912.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2200_1700_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377913.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2200_1900_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377914.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2400_100_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377915.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2400_300_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377916.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2400_500_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377917.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2400_700_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377918.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2400_900_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377919.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2400_1100_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377920.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2400_1300_2LMET100.py',
    '../mc15joboptions/share/DSID377xxx/MC15.377921.MGPy8EG_A14N23LO_SM_SS_N2_ZN1_2400_1500_2LMET100.py'
    ]
    
    
    
    
    counter  = 0
    for jobOption in jobOptionsList:
        
        massParticles = getMasses(jobOption)
        dsidJob       = getDSID(jobOption)
        intGluon      = int(massParticles[0])
        intSlepton    = int(massParticles[1])
        
        if(True):
            print "++++++++++++++++++++++++++++++++++++++++++++++++"
            print "Running on this jobOption:    ", jobOption
            
            print "Gluon mass: ", massParticles[0]," Slepton mass: ", massParticles[1]
            print "DSID:  ", dsidJob 
            maxEvents = -999
            endName   = ""
            
            #if(abs(intGluon - intSlepton) > 40): continue
            
            if((intGluon >= 600 and intGluon <= 2400) and abs(intGluon - intSlepton)<=200):
                maxEvents = 20
                endName   = "_20Events"
            elif((intGluon >= 600 and intGluon <= 2400) and abs(intGluon - intSlepton)<=800):
                maxEvents = 50
                endName   = "_50Events"
            else:
                maxEvents = 100
                endName   = "_100Events"
            
            print "++++++++++++++++++++++++++++++++++++++++++++++++"
            txtFileGZ  = getLHEFile(massParticles[0])
            baseTxt    = txtFileGZ.split('tar')[0]
            evntTxt    = baseTxt+'events'
            
            command = "Generate_tf.py --ecmEnergy=13000 --runNumber="+dsidJob+" --firstEvent=1 --jobConfig="+jobOption+" --outputEVNTFile=arka_"+massParticles[0]+"_"+massParticles[1]+endName+".root --maxEvents="+str(maxEvents)+" --inputGeneratorFile="+getLHEFile(massParticles[0])
            
            print "The command to execute: ", command
            counter += 1
            print "Job number :", counter
            
            
            os.system('rm *.dat')
            os.system(command)
            os.system('mv log.generate log.generate_'+massParticles[0]+'_'+massParticles[1]+endName)
            os.system('mv log.gene* logDirectory/')
            os.system('mv *.root rootDirectory/')
            
            if(counter > 1 and args.shortJob):
                break
            
        
        
if __name__ == "__main__":
    start = time.time()
    main()
    print "The time taken: ", (time.time() - start)/60.0, " m"
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
