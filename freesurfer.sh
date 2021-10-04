#!/bin/bash
# script to run FreeSurfer
export FREESURFER_HOME=/Storage2/freesurfer_dir/freesurfer
export SUBJECTS_DIR=$FREESURFER_HOME/subjects
source $FREESURFER_HOME/SetUpFreeSurfer.sh

# run recon all on all the subjects
python3 freesurfer_reconall_pipeline.py
