import sys
from os import listdir

speakers = ["03", "08", "09", "10", "11", "12", "13", "14", "15", "16"]
emotions = ["W", "L", "E", "A", "F", "T", "N"]
emoFile = [[], [], [], [], [], [], []]
sortFile = []
maxLen = 0

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
for f in files:
    if f[-3:] != "txt":
        continue
    for emotion in emotions:
        if emotion == f[5]:
            index = emotions.index(emotion)
            emoFile[index].append(f)
            maxLen = len(emoFile[index]) if len(emoFile[index]) > maxLen else maxLen
            break
for i in range(maxLen):
    for emof in emoFile:
        if i < len(emof):
            sortFile.append(emof[i])
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