#!/bin/bash

cluster=$1
process=$2

# CMSSW setup etc
export SCRAM_ARCH="slc6_amd64_gcc700" 
export VO_CMS_SW_DIR="/cms/base/cmssoft"
export COIN_FULL_INDIRECT_RENDERING=1
source $VO_CMS_SW_DIR/cmsset_default.sh

cd /users/h2/rsk146/CMSSW_10_2_2/src
eval `scramv1 runtime -sh`

cd /users/h2/rsk146/CMSSW_10_2_2/src/ZprimeGamma


export MYSCRIPT=/users/h2/rsk146/CMSSW_10_2_2/src/ZprimeGamma/TreeNoCut_GJets_$2.py

#---------------------------------------------------------------

echo "Running script " $MYSCRIPT 

python $MYSCRIPT >& /users/h2/rsk146/CMSSW_10_2_2/src/ZprimeGamma/condor_logfiles2/logfile_$1_$2.log 
