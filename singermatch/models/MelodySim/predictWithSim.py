import random
import math
from collections import defaultdict

import numpy as np
from sklearn.decomposition import PCA

def computeTFIDF():
    # document frequency which appear a melody
    # totalRow total frequency
    print(len(totalData))
    print(len(totalData[0]))
    document = [0] * len(totalData[0])
    totalRow = [0] * len(totalData)
    for i in range(len(totalRow)):
        for j in range(len(document)):
            totalRow[i] += totalData[i][j]
            if totalData[i][j] != 0:
                document[j] += 1
                print(document[j])
    dataIFIDF = []
    for i in range(len(totalData)):
        tmp = []
        for j in range(len(totalData[0])):
            if (totalData[i][j] == 0):
                tmp.append(0)
            else:
                tmp.append((float(totalData[i][j]) / totalRow[i]) * math.log(float(len(totalData)) / document[j], math.e))
        dataIFIDF.append(tmp)
    return dataIFIDF


def cosinSim(s1, s2):
    product = sum([float(s1[i]) * float(s2[i]) for i in range(1, len(s1))])
    dem = math.sqrt(sum([float(s1[i]) * float(s1[i]) for i in range(1, len(s1))])) * math.sqrt(sum([float(s2[i]) * float(s2[i]) for i in range(1, len(s2))]))
    if product == 0:
        return 0
    else:
        return product / dem

def computeMean(s):
    sum = 0
    for i in range(len(s)):
        sum += (s[i] * i)
    return sum / len(s)

def cosinSim2(s1, s2):
    product = 0
    mol1 = 0
    mol2 = 0
    for i in range(len(s1)):
        if s1[i] != 0 and s2[i] != 0:
            product += s1[i]*s2[i]
            mol1 += s1[i] * s1[i]
            mol2 += s2[i] * s2[i]
    dem = (math.sqrt(mol1) * math.sqrt(mol2))
    if dem == 0:
        return 0
    else:
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

def meanSim(m1, m2):
    return abs(m1 - m2)

def predict2(d_valid):
    maxSim = meanSim(computeMean(Xpca_train[0]), computeMean(d_valid))
    corLabel = ""
    for i in range(len(Xpca_train)):
        res = meanSim(computeMean(Xpca_train[i]), computeMean(d_valid))
        if res < maxSim:
            maxSim = res
            corLabel = trainLabel[i]
        else:
            pass
    return corLabel

def predict_ifidf(d_valid):
    maxSim = 0
    corLabel = ""
    for i in range(len(X_train_ifidf)):
        res = cosinSim(X_train_ifidf[i], d_valid)
        if res > maxSim:
            maxSim = res
            corLabel = trainLabel[i]
        else:
            pass
    return corLabel

#
# path = "/Users/mac126/19fall/cs258/assign2/SingerMatch/singermatch/models/MelodySim/dataSet.txt"
# dataSet = []
# print(path)
# for line in open(path):
#     info = line.strip("\n").split(",")
#     dataSet.append(info)
# random.seed(12)
# random.shuffle(dataSet)
# trainSize = int(len(dataSet) * 0.9)
# validSize = int(len(dataSet) * 0.1)
# trainSet = dataSet[:trainSize]
# validSet = dataSet[trainSize:]
# #testSet = dataSet[validSize:]
# print("HERE")
# trainData = []
# trainLabel = []
#
# for d in trainSet:
#
#     trainData.append([int(i) for i in d[1:-2]])
#     trainLabel.append(d[-1])
# validData = []
# validLabel = []
#
# for d in validSet:
#     validData.append([int(i) for i in d[1:-2]])
#     validLabel.append(d[-1])
# print("now predict")
#
#
# X_train = np.array(trainData)
# X_valid = np.array(validData)
# pca = PCA(n_components=27)
# pca.fit(X_train)
# Xpca_train = np.matmul(X_train, pca.components_.T)
# Xpca_valid = np.matmul(X_valid, pca.components_.T)
#
# # prediction
# prediction = []
# correct = 0
# for i in range(len(Xpca_valid)):
#     pred = predict(Xpca_valid[i])
#     print(pred)
#     print(validLabel[i])
#     if pred == validLabel[i]:
#         correct += 1
#         print(correct)
#     prediction.append(pred)
# # accuracy
# pred = np.array(prediction)
# print(len(Xpca_valid))
# y_valid = np.array(validLabel)
# accuracy = float(correct) / len(y_valid)
# print(accuracy)

author = ["aerosmith", "beatles", "creedence_clearwater_revival", "cure", "dave_matthews_band", "depeche_mode",
          "fleetwood_mac", "garth_brooks", "green_day", "led_zeppelin", "madonna", "metallica", "prince",
          "queen", "radiohead", "roxette", "steely_dan", "suzanne_vega", "tori_amos", "u2"]

path = "/Users/mac126/19fall/cs258/assign2/SingerMatch/singermatch/models/MelodySim/dataSet.txt"

# dataSet2 = []
dataSet2 = defaultdict(list)

#
# print(path)
for line in open(path):
    info = line.strip("\n").split(",")
    dataSet2[info[-1]].append(info)
trainSet = []
validSet = []
for key in dataSet2:
    total = len(dataSet2[key])
    trainSet += (dataSet2[key][:int(total * 0.90)])
    validSet += (dataSet2[key][int(total * 0.90):])
trainData = []
trainLabel = []
for d in trainSet:
    trainData.append([int(i) for i in d[0:-2]])
    trainLabel.append(d[-1])
validData = []
validLabel = []

for d in validSet:
    validData.append([int(i) for i in d[0:-2]])
    validLabel.append(d[-1])

totalData = trainData + validData

print("now predict")

# X_train = np.array(trainData)
# X_valid = np.array(validData)
# pca = PCA(n_components=100)
# pca.fit(X_train)
# Xpca_train = np.matmul(X_train, pca.components_.T)
# Xpca_valid = np.matmul(X_valid, pca.components_.T)
#
Xpca_train = np.array(trainData)
Xpca_valid =  np.array(validData)
# # prediction
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
# # accuracy
pred = np.array(prediction)
print(len(Xpca_valid))
# y_valid = np.array(validLabel)
accuracy = float(correct) / len(validLabel)
print(accuracy)

# totalData_ifidf = computeTFIDF()
# X_train_ifidf = totalData_ifidf[:len(trainData)]
# X_valid_ifidf = totalData_ifidf[len(trainData):]
#
# for i in range(len(X_valid_ifidf)):
#     pred = predict_ifidf(X_valid_ifidf[i])
#     print(pred)
#     print(validLabel[i])
#     if pred == validLabel[i]:
#         correct += 1
#         print(correct)
#         prediction.append(pred)
# # # # accuracy
# pred = np.array(prediction)
# print(len(Xpca_valid))
# # # y_valid = np.array(validLabel)
# accuracy = float(correct) / len(validLabel)
# print(accuracy)

# from sklearn.svm import SVC
# clf = SVC(gamma='auto')
# clf.fit(Xpca_train, trainLabel)
# pred = clf.predict(Xpca_valid)
# y_valid = np.array(validLabel)
# print(float(sum(pred == y_valid)) / len(pred))


# from sklearn.linear_model import LogisticRegression
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.model_selection import cross_val_score
# import pandas as pd
# models = [
#     RandomForestClassifier(n_estimators=200, max_depth=3, random_state=0),
#     MultinomialNB(),
#     LogisticRegression(random_state=0),
# ]
# CV = 5
# cv_df = pd.DataFrame(index=range(CV * len(models)))
# entries = []
# for model in models:
#     model_name = model.__class__.__name__
#     accuracies = cross_val_score(model, totalData, trainLabel + validLabel, scoring='accuracy', cv=CV)
#     print(accuracies)
#     for fold_idx, accuracy in enumerate(accuracies):
#         entries.append((model_name, fold_idx, accuracy))
# cv_df = pd.DataFrame(entries, columns=['model_name', 'fold_id', 'accuracy'])
# print(cv_df)
