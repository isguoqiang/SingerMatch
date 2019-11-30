from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
import numpy as np
from sklearn.model_selection import cross_val_score
import pandas as pd
import random

def computeFrequency(d):
    rowSum = 0
    for i in range(len(d)):
        rowSum += float(d[i])
    return [float(i) /rowSum for i in d]


# reading data
path = "/Users/mac126/19fall/cs258/assign2/SingerMatch/singermatch/models/MelodySim/dataSet.txt"
data = []
for line in open(path):
    info = line.strip("\n").split(",")
    data.append(info)


# reading trainlist
trainlist_path = "/Users/mac126/19fall/cs258/assign2/data/train.list"
trainset = set()
for line in open(trainlist_path):
    trainset.add(line.strip("\r\n").split("/")[-2])

testset = set()
testlist_path = "/Users/mac126/19fall/cs258/assign2/data/test.list"
for line in open(testlist_path):
    testset.add(line.strip("\r\n").split("/")[-2])

Xtrain = []
ytrain = []
Xtest = []
ytest = []

for d in data:
    if d[-2] in trainset:
        Xtrain.append([float(i) for i in d[:-2]])
        ytrain.append(d[-1])
    else:
        Xtest.append([float(i) for i in d[:-2]])
        ytest.append(d[-1])




models = [
    RandomForestClassifier(n_estimators=200, max_depth=3, random_state=0),
    MultinomialNB(),
    LogisticRegression(random_state=0),
]

for model in models:
    model.fit(Xtrain, ytrain)
    ypred = model.predict(Xtest)
    accuracy = float(sum(ypred == np.array(ytest))) / len(ytest)
    print("model:{} ==> accuracy:{}".format(model.__class__.__name__, accuracy))

