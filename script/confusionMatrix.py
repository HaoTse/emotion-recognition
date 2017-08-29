import sys

fname = "10fold/test16.txt"
resultName = "Result_test.txt"
emotionDict = {ord('W') - ord('A'): 0, ord('L') - ord('A'): 1, ord('E') - ord('A'): 2, ord('A') - ord('A'): 3, ord('F') - ord('A'): 4, ord('T') - ord('A'): 5, ord('N') - ord('A'): 6}
emotions = ["anger", "boredom", "disgust", "anxiety/fear", "happiness", "sadness", "neutral version"]
testLabel = []
resultLabel = []
confusionMatrix = [[0] * 7 for _ in range(7)]

# read file
with open(fname, "r") as fin:
    lines = fin.readlines()
for line in lines:
    testLabel.append(line.split(" ")[0])
with open(resultName, "r") as fin:
    fin.readline() # skip line 1
    lines = fin.readlines()
for line in lines:
    resultLabel.append(line.split(" ")[0])

# caculate the confusion martix
for x in testLabel:
    y = resultLabel[testLabel.index(x)]
    x_ = emotionDict[int(x)]
    y_ = emotionDict[int(y)]
    confusionMatrix[x_][y_] += 1
# ouptut format
outputTxt = "               |"
for emotion in emotions:
    outputTxt += "%15s|" % (emotion)
outputTxt += "\n"
for i in range(len(confusionMatrix)):
    outputTxt += "%15s|" % (emotions[i])
    sum_ = sum(confusionMatrix[i])
    for j in confusionMatrix[i]:
        text = "     %3d (%.2f)" % (j, j / sum_)
        outputTxt += text + "|"
    outputTxt += "\n"
print outputTxt