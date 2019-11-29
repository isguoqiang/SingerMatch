import random
import math
import numpy as np
from sklearn.decomposition import PCA

def cosinSim(s1, s2):
    product = sum([int(s1[i]) * int(s2[i]) for i in range(1, len(s1))])
    dem = math.sqrt(sum([int(s1[i]) * int(s1[i]) for i in range(1, len(s1))])) * math.sqrt(sum([int(s2[i]) * int(s2[i]) for i in range(1, len(s2))]))
    return product / dem

def predict(d_valid):
    maxSim = 0
    corLabel = ""
    for i in range(len(Xpca_train)):
        res = cosinSim(Xpca_train[i], d_valid)
        if res > maxSim:
            maxSim = res
            corLabel = trainLabel[i]
        else:
            pass
    return corLabel


path = "/Users/mac126/19fall/cs258/assign2/SingerMatch/singermatch/models/MelodySim/dataSet.txt"
dataSet = []
print(path)
for line in open(path):
    info = line.strip("\n").split(",")
    dataSet.append(info)
random.seed(12)
random.shuffle(dataSet)
trainSize = int(len(dataSet) * 0.9)
validSize = int(len(dataSet) * 0.1)
trainSet = dataSet[:trainSize]
validSet = dataSet[trainSize:]
#testSet = dataSet[validSize:]
print("HERE")
trainData = []
trainLabel = []

for d in trainSet:

    trainData.append([int(i) for i in d[1:-2]])
    trainLabel.append(d[-1])
validData = []
validLabel = []

for d in validSet:
    validData.append([int(i) for i in d[1:-2]])
    validLabel.append(d[-1])
print("now predict")


X_train = np.array(trainData)
X_valid = np.array(validData)
pca = PCA(n_components=27)
pca.fit(X_train)
Xpca_train = np.matmul(X_train, pca.components_.T)
Xpca_valid = np.matmul(X_valid, pca.components_.T)

# prediction
prediction = []
correct = 0
for i in range(len(Xpca_valid)):
    pred = predict(Xpca_valid[i])
    print(pred)
    print(validLabel[i])
    if pred == validLabel[i]:
        correct += 1
        print(correct)
    prediction.append(pred)
# accuracy
pred = np.array(prediction)
print(len(Xpca_valid))
y_valid = np.array(validLabel)
accuracy = float(correct) / len(y_valid)
print(accuracy)

author = ["aerosmith", "beatles", "creedence_clearwater_revival", "cure", "dave_matthews_band", "depeche_mode",
          "fleetwood_mac", "garth_brooks", "green_day", "led_zeppelin", "madonna", "metallica", "prince",
          "queen", "radiohead", "roxette", "steely_dan", "suzanne_vega", "tori_amos", "u2"]

path = "/Users/mac126/19fall/cs258/assign2/SingerMatch/singermatch/models/MelodySim/dataSet.txt"

# dataSet2 = []
#
# print(path)
# for line in open(path):
#     info = line.strip("\n").split(",")
#
#     dataSet.append(info)



