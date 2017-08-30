import sys
from os import listdir
import math

speakers = ["03", "08", "09", "10", "11", "12", "13", "14", "15", "16"]
emotions = ["W", "L", "E", "A", "F", "T", "N"]
emoFile = [[], [], [], [], [], [], []]
sortFile = []

svmPath = "svm"
tenfoldPath = "10fold"
fivefoldPath = "5fold"
files = [f for f in listdir(svmPath)]

# 10-fold
for speaker in speakers:
    trainTxt = ""
    testTxt = ""
    for f in files:
        if f[-3:] != "txt":
            continue
        with open(svmPath + "/" + f, 'r') as fin:
            lines = fin.readlines()
        for line in lines:
            if speaker == f[:2]:
                testTxt += (line)
            else:
                trainTxt += (line)
    with open(tenfoldPath + "/test" + speaker + ".txt", 'w') as fout:
        fout.write(testTxt)
    with open(tenfoldPath + "/train" + speaker + ".txt", 'w') as fout:
        fout.write(trainTxt)

# 5-fold
fileCnt = 0
for f in files:
    if f[-3:] != "txt":
        continue
    fileCnt += 1
    for emotion in emotions:
        if emotion == f[5]:
            index = emotions.index(emotion)
            emoFile[index].append(f)
            break
emoLen = [len(x) for x in emoFile]
emoPro = [int(math.floor(float(l) / 5)) for l in emoLen]
emoRem = [int(emoLen[i] - emoPro[i] * 5) for i in range(len(emoPro))]
emoIdx = [0] * 7
remIdx = 0
for i in range(5):
    for j in range(7):
        for k in range(emoPro[j]):
            if emoIdx[j] >= emoLen[j]:
                break
            idx = emoIdx[j]
            sortFile.append(emoFile[j][idx])
            emoIdx[j] += 1
    while len(sortFile) < fileCnt / 5 * (i + 1):
        remIdx %= 7
        if emoRem[remIdx] <= 0:
            remIdx += 1
            continue
        idx = emoIdx[remIdx]
        sortFile.append(emoFile[remIdx][idx])
        emoIdx[remIdx] += 1
        emoRem[remIdx] -= 1
        remIdx += 1
for i in range(5):
    trainTxt = ""
    testTxt = ""
    startIdx = round(len(sortFile) / 5 * i)
    endIdx = round(len(sortFile) / 5 * (i + 1))
    for j in range(len(sortFile)):
        f = sortFile[j]
        with open(svmPath + "/" + f, 'r') as fin:
            lines = fin.readlines()
        for line in lines:
            if j >= startIdx and j < endIdx:
                testTxt += (line)
            else:
                trainTxt += (line)
    with open(fivefoldPath + "/test" + str(i) + ".txt", 'w') as fout:
        fout.write(testTxt)
    with open(fivefoldPath + "/train" + str(i) + ".txt", 'w') as fout:
        fout.write(trainTxt)
