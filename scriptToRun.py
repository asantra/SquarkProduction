### run it like : python scriptToRun.py <inputTxtName>

import os, sys, time
from subprocess import Popen, PIPE


inputFileName = sys.argv[1]
outputFailed = open('GMSBFailedJobs.txt', 'w')

eosDirectory = '/eos/user/a/asantra/'

with open(inputFileName) as txtFile:
    for lines in txtFile.readlines():
        start = time.time()
        line         = lines.rstrip()
        samplePath   = line.split()[0]
        numberSample = line.split()[1]
        fullPath     = eosDirectory+samplePath
        if 'GMSB600_MC16a' not in numberSample:
            continue
        print '================================================================'
        print '================================================================'
        print 'The code is now processing: ', fullPath        
        process = Popen('run_xAODNtMaker -s '+fullPath+' -d "output/"'+numberSample+' --isAf2 -selector Susy2LJetsLegacySelector', shell=True, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        print 'out: ', stdout
        print 'err: ', stderr
        if not stdout:
            print 'This job failed to submit: ', samplePath
            outputFailed.write(samplePath+' '+numberSample+'\n')
        else:
            print 'This job was submitted: ', samplePath
            
        end = time.time()
        print 'The processing time is: ', (end - start), ' seconds'
        
outputFailed.close()
