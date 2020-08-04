#!/bin/bash

cluster=$1
process=$2

# CMSSW setup etc
export SCRAM_ARCH="slc7_amd64_gcc700"
export VO_CMS_SW_DIR="/cms/base/cmssoft"
export COIN_FULL_INDIRECT_RENDERING=1
source $VO_CMS_SW_DIR/cmsset_default.sh

cd /users/h2/rsk146/JTTest/SL7/CMSSW_10_2_15/src/signalM_100MC
eval `scramv1 runtime -sh`

cmsRun nano0.py >& /users/h2/rsk146/JTTest/SL7/CMSSW_10_2_15/src/condorFiles/logfiles_$1_$2.log
