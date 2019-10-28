# Generator transform pre-include
#  Gets us ready for on-the-fly SUSY SM generation
include ( 'MC15JobOptions/MadGraphControl_SimplifiedModelPreInclude.py' )
keepOutput=True
print "@@@@@@@@@@@@############### the new madgraph control file working #####################@@@@@@@@@@@@@@@@@"

gentype=runArgs.jobConfig[0].split('SM')[1].split('_')[1]
if 'SLN1' in runArgs.jobConfig[0]: decaytype='twostepN2_SLN1'
elif 'offshellZN1' in runArgs.jobConfig[0]: decaytype='onestepN2_offshellZN1'
elif 'ZN1' in runArgs.jobConfig[0]: decaytype='onestepN2_ZN1'

# special to handle MadSpin configuration via JO name:
madspindecays=False
if "MadSpin" in runArgs.jobConfig[0]: 
    madspindecays=True

mass_string = runArgs.jobConfig[0].replace('.py','').split('N1_')[1]
deltaM = 0 # mchi20 - mchi10 

#--------------------------------------------------------------
# MadGraph configuration
#--------------------------------------------------------------
if gentype=='SS':
# Direct gluino decay to LSP (0-lepton, grid 1 last year)
    masses['1000001'] = float( mass_string.split('_')[0] ) # squark mass
    masses['1000002'] = float( mass_string.split('_')[0] ) # squark mass
    masses['1000003'] = float( mass_string.split('_')[0] ) # squark mass
    masses['1000004'] = float( mass_string.split('_')[0] ) # squark mass
    masses['1000005'] = float( mass_string.split('_')[0] ) # squark mass
    masses['2000001'] = float( mass_string.split('_')[0] ) # squark mass
    masses['2000002'] = float( mass_string.split('_')[0] ) # squark mass
    masses['2000003'] = float( mass_string.split('_')[0] ) # squark mass
    masses['2000004'] = float( mass_string.split('_')[0] ) # squark mass
    masses['2000005'] = float( mass_string.split('_')[0] ) # squark mass
    masses['1000022'] = float( mass_string.split('_')[1] )  #chi10
    masses['1000023'] = 0.5*(masses['1000001']+masses['1000022'])  #chi20
    deltaM = 0.5*(masses['1000001'] - masses['1000022']) # (msquark - mchi10) / 2 = mchi20 - mchi10 

    if 'SL' in decaytype:
        masses['1000011'] = 0.5*(masses['1000022']+masses['1000023'])  #slepton
        masses['1000012'] = 0.5*(masses['1000022']+masses['1000023'])  #slepton
        masses['1000013'] = 0.5*(masses['1000022']+masses['1000023'])  #slepton
        masses['1000014'] = 0.5*(masses['1000022']+masses['1000023'])  #slepton
        masses['1000015'] = 0.5*(masses['1000022']+masses['1000023'])  #slepton
        masses['1000016'] = 0.5*(masses['1000022']+masses['1000023'])  #slepton
    else:
        masses['1000011'] = 4.5e5 #slepton
        masses['1000012'] = 4.5e5 #slepton
        masses['1000013'] = 4.5e5 #slepton
        masses['1000014'] = 4.5e5 #slepton
        masses['1000015'] = 4.5e5 #slepton
        masses['1000016'] = 4.5e5 #slepton
    #### MadGraph is used to decay squark, Madspin will be used to decay N2
    print "$$$&&&&&&&&&&& in SS setup $$$$$$&&&&&&&"
    #process = '''
    #define susylqA = dl cl sl ur dr cr sr
    #define susylqA~ = dl~ cl~ sl~ ur~ dr~ cr~ sr~
    #generate p p > ul ul~ $ go susyweak susylqA susylqA~ @1
    #add process p p > ul ul~ j $ go susyweak susylqA susylqA~ @2
    #add process p p > ul ul~ j j $ go susyweak susylqA susylqA~ @3
    #'''
    
    process = '''
    define susylqA = ul dl cl sl ur dr cr sr
    define susylqA~ = ul~ dl~ cl~ sl~ ur~ dr~ cr~ sr~
    generate p p > susylqA susylqA~, susylqA > jb n2, susylqA~ > jb n2 $ go susyweak @1
    add process p p > susylqA susylqA~ j, susylqA > jb n2, susylqA~ > jb n2 $ go susyweak @2
    add process p p > susylqA susylqA~ j j, susylqA > jb n2, susylqA~ > jb n2 $ go susyweak @3
    '''
    print "!!!!!!!!!!!process: MadGraph decaying squark with two jets  !!!!!!!!!!!!!!!!!!!!!"
    
if gentype=='GG':
# Direct gluino decay to LSP (0-lepton, grid 1 last year)
    masses['1000021'] = float( mass_string.split('_')[0] )  #gluino
    masses['1000022'] = float( mass_string.split('_')[1] )  #chi10
    masses['1000023'] = 0.5*(masses['1000021']+masses['1000022'])  #chi20
    deltaM = 0.5*(masses['1000021'] - masses['1000022']) # (mgluino - mchi10) / 2 = mchi20 - mchi10 

    if 'SL' in decaytype:
        masses['1000011'] = 0.5*(masses['1000022']+masses['1000023'])  #slepton
        masses['1000012'] = 0.5*(masses['1000022']+masses['1000023'])  #slepton
        masses['1000013'] = 0.5*(masses['1000022']+masses['1000023'])  #slepton
        masses['1000014'] = 0.5*(masses['1000022']+masses['1000023'])  #slepton
        masses['1000015'] = 0.5*(masses['1000022']+masses['1000023'])  #slepton
        masses['1000016'] = 0.5*(masses['1000022']+masses['1000023'])  #slepton
    else:
        masses['1000011'] = 4.5e5 #slepton
        masses['1000012'] = 4.5e5 #slepton
        masses['1000013'] = 4.5e5 #slepton
        masses['1000014'] = 4.5e5 #slepton
        masses['1000015'] = 4.5e5 #slepton
        masses['1000016'] = 4.5e5 #slepton
        
    #### MadGraph is used to decay gluino, Madspin will be used to decay N2
    print "$$$&&&&&&&&&&& in GG setup $$$$$$&&&&&&&"
    process = '''
    generate p p > go go
    add process p p > go go j
    add process p p > go go j j
    '''

evgenConfig.contact  = ["arka.santra@cern.ch" ]

if 'SS' in gentype: 
    evgenConfig.keywords += ['simplifiedModel','squark','Z']
    evgenConfig.description = 'SUSY Simplified Model with squark production and decays via Z with MadGraph/Pythia8, m_squ = %s GeV, m_N2 = %s GeV, m_N1 = %s GeV'%(masses['1000001'],masses['1000023'],masses['1000022'])
    
if 'GG' in gentype: 
    evgenConfig.keywords += ['simplifiedModel','gluino', 'Z']
    evgenConfig.description = 'SUSY Simplified Model with gluino production and decays via Z with MadGraph/Pythia8, m_glu = %s GeV, m_N2 = %s GeV, m_N1 = %s GeV'%(masses['1000021'],masses['1000023'],masses['1000022'])

#--------------------------------------------------------------
# Madspin configuration
#--------------------------------------------------------------
msdecaystring = ""
if 'SS' in gentype:
    print "$$$&&&&&&&&&&& in SS setup in MadSpin $$$$$$&&&&&&&"
    msdecaystring="""
    define all = e+ e- mu+ mu- ta+ ta- u u~ d d~ c c~ s s~ b b~ ve vm vt ve~ vm~ vt~
    decay n2 > all all n1
    """
    
if 'GG' in gentype:
    msdecaystring="""
    define all = e+ e- mu+ mu- ta+ ta- u u~ d d~ c c~ s s~ b b~ ve vm vt ve~ vm~ vt~
    decay go > jb jb n2, n2 > all all n1
    """

if madspindecays==True:
  if msdecaystring=="":
    raise RuntimeError("Asking for MadSpin decays, but no decay string provided!")
  madspin_card='madspin_card.dat'

  mscard = open(madspin_card,'w') 

  mscard.write("""#************************************************************
#*                        MadSpin                           *               
#*                                                          *               
#*    P. Artoisenet, R. Frederix, R. Rietkerk, O. Mattelaer *               
#*                                                          *               
#*    Part of the MadGraph5_aMC@NLO Framework:              *               
#*    The MadGraph5_aMC@NLO Development Team - Find us at   *               
#*    https://server06.fynu.ucl.ac.be/projects/madgraph     *               
#*                                                          *               
#************************************************************               
#Some options (uncomment to apply)                                           
#                                                                           
# set Nevents_for_max_weigth 75 # number of events for the estimate of the max. weight
set BW_cut 100                # cut on how far the particle can be off-shell         
set max_weight_ps_point 400  # number of PS to estimate the maximum for each event   
#
set seed %i
set spinmode none
# specify the decay for the final state particles
        
%s

# running the actual code                       
launch"""%(runArgs.randomSeed,msdecaystring))                   
  mscard.close()

#--------------------------------------------------------------
# Pythia configuration
#--------------------------------------------------------------
# This comes after all Simplified Model setup files
evgenLog.info('Will use Pythia8...')

pythia = genSeq.Pythia8

pythia.MaxFailures = 100

#--------------------------------------------------------------
# Algorithms Private Options
#--------------------------------------------------------------
filters=[]

# Two-lepton+Met filter
if '2LMET100' in runArgs.jobConfig[0]:
    evt_multiplier = 200
    include('MC15JobOptions/MultiLeptonFilter.py')
    MultiLeptonFilter = filtSeq.MultiLeptonFilter
    filtSeq.MultiLeptonFilter.Ptcut = 5000.
    filtSeq.MultiLeptonFilter.Etacut = 2.8
    filtSeq.MultiLeptonFilter.NLeptons = 2  

    include("MC15JobOptions/MissingEtFilter.py")
    filtSeq.MissingEtFilter.METCut = 100*GeV            # MET > 100 GeV
  
    filtSeq.Expression = "(MultiLeptonFilter) and (MissingEtFilter)"
    
    
# Two-lepton filter
elif '2L' in runArgs.jobConfig[0]:
    evt_multiplier = 20
    include('MC15JobOptions/MultiLeptonFilter.py')
    MultiLeptonFilter = filtSeq.MultiLeptonFilter
    filtSeq.MultiLeptonFilter.Ptcut = 5000.
    filtSeq.MultiLeptonFilter.Etacut = 2.8
    filtSeq.MultiLeptonFilter.NLeptons = 2
    
    
elif 'MET100' in runArgs.jobConfig[0]:
    evt_multiplier *= 2
    include ( 'MC15JobOptions/MissingEtFilter.py' )
    MissingEtFilter = filtSeq.MissingEtFilter
    filtSeq.MissingEtFilter.METCut = 100*GeV


#--------------------------------------------------------------
# Z->ll for low deltaM
#--------------------------------------------------------------
# For low deltaM = m(N2) - m(N1) in the ZN1 grid, if there's a Z in the event we need to use madspin for the decays
if "ZN1" in decaytype and deltaM <= 20 and madspindecays==False:
    print "Mass difference smaller than 20 GeV, m_N2 - m_N1 = ", deltaM, ", need to decay the Z using madspin for this to work. Exiting..." 
    sys.exit()

njets = 1
include('MC15JobOptions/MadGraphControl_SimplifiedModelPostInclude.py')


#### this is to use the MCORE settings
if 'ATHENA_PROC_NUMBER' in os.environ:
    print 'Noticed that you have run with an athena MP-like whole-node setup.  Will re-configure now to make sure that the remainder of the job runs serially.'
    njobs = os.environ.pop('ATHENA_PROC_NUMBER')
    # Try to modify the opts underfoot
    if not hasattr(opts,'nprocs'): print 'Did not see option!'
    else: opts.nprocs = 0
    print opts

if njets>0:
    genSeq.Pythia8.Commands += [ "Merging:Process = guess" ]
    
    ### needed to use "guess" option of Pythia.
    if "UserHooks" in genSeq.Pythia8.__slots__.keys():
        genSeq.Pythia8.UserHooks += ['JetMergingaMCatNLO']
    else:
        genSeq.Pythia8.UserHook = 'JetMergingaMCatNLO'
