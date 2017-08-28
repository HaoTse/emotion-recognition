#!/bin/bash
#vi .bash_profile
PATH=$PATH:$HOME/bin
 
dir=/Users/tse/Downloads/openSMILE-2.1.0/emotion-recognition/arff
OPATH=/Users/tse/Downloads/openSMILE-2.1.0/emotion-recognition/svm
 
for wav in $(ls $dir); do
    python arff2svm.py $dir/$wav $OPATH/$wav
    echo "$wav is converted"
done
 
echo "work finished!"
