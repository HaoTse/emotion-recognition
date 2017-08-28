import sys
from os import listdir
import math

speakers = ["03", "08", "09", "10", "11", "12", "13", "14", "15", "16"]
emotions = ["W", "L", "E", "A", "F", "T", "N"]
emoFile = [[], [], [], [], [], [], []]
fivefold = [[], [], [], [], []]

svmPath = "svm"
tenfoldPath = "10fold"
fivefoldPath = "5fold"
files = [f for f in listdir(svmPath)]
"""
# 10-fold
for speaker in speakers:
    trainTxt = ""
    testTxt = ""
    for f in files:
        with open(svmPath + "/" + f, 'r') as fin:
            lines = fin.readlines()
        for line in lines:
            if speaker in f:
                testTxt += (line)
            else:
                trainTxt += (line)
    with open(tenfoldPath + "/test" + speaker + ".txt", 'w') as fout:
        fout.write(testTxt)
    with open(tenfoldPath + "/train" + speaker + ".txt", 'w') as fout:
        fout.write(trainTxt)
"""
# 5-fold
for f in files:
    for emotion in emotions:
        if emotion == f[5]:
            index = emotions.index(emotion)
            emoFile[index].append(f)
            break
for i in range(5):
    for k in range(len(emoFile)):
        start = int(math.floor(len(emoFile[k]) / 5 * i))
        end = len(emoFile[k]) if i == 4 else int(math.ceil(len(emoFile[k]) / 5 * (i + 1)))
        for j in range(start, end):
            fivefold[i].append(emoFile[k][j])
for i in range(5):
    trainTxt = ""
    testTxt = ""
    for f in files:
        with open(svmPath + "/" + f, 'r') as fin:
            lines = fin.readlines()
        for line in lines:
            if f in fivefold[i]:
                testTxt += (line)
            else:
                trainTxt += (line)
    with open(fivefoldPath + "/test" + str(i) + ".txt", 'w') as fout:
        fout.write(testTxt)
    with open(fivefoldPath + "/train" + str(i) + ".txt", 'w') as fout:
        fout.write(trainTxt)
