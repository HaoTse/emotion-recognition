#!/bin/bash
#vi .bash_profile
PATH=$PATH:$HOME/bin

openSMILEPath = /Usrs/tse/Downloads/openSMILE-2.1.0 
dir = $openSMILEPath/emotion-recognition/wav
OPATH = $openSMILEPath/emotion-recognition/arff
 
for wav in $(ls $dir); do
    $openSMILEPath/inst/bin/SMILExtract -C $openSMILEPath/config/IS09_emotion.conf -I $dir/$wav -O $OPATH/$wav.txt
    echo "$wav is extracted"
done
 
echo "work finished!"
