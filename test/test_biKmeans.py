#################################################
# kmeans: k-means cluster
# Author : zouxy
# Date   : 2013-12-25
# HomePage : http://blog.csdn.net/zouxy09
# Email  : zouxy09@qq.com
#################################################

from numpy import *
import time
import matplotlib.pyplot as plt
from biKmeans import biKmeans
from biKmeans import showCluster
# from pca import plotBestFit
# from pca import pca

# step 1: load data
print "step 1: load data..."
dataSet = []
fileIn = open('testSet1.txt')
for line in fileIn.readlines():
    lineArr = line.strip().split(',')
    dataSet.append([float(lineArr[0]), float(lineArr[1]),
                    float(lineArr[2]), float(lineArr[3])])

# step 2: clustering...
print "step 2: show the data..."
dataSet = mat(dataSet)
numSamples = dataSet.shape[0]
for i in xrange(numSamples):
    # markIndex = int(clusterAssment[i, 0])
    plt.plot(dataSet[i, 0], dataSet[i, 1], 'or')
# plt.show()

# plotBestFit(dataSet)
# for i in xrange(dataSet.shape[0]):
#     plt.plot(dataSet[i, 0], dataSet[i, 1], 'or')
# plt.show()
print "step 3: clustering..."
k = 3
centroids, clusterAssment, numSamples = biKmeans(dataSet, k)


# step 3: show the result
print "step 4: show the result..."

showCluster(dataSet, k, centroids, clusterAssment)

print "step 5: compared with the label of the real-world data..."
dataCount = [0, 0, 0]
temp = []
dataCom = []
count = 0
sums = 0
fileIn = open('testSet.txt')
for line in fileIn.readlines():
    lineArr = line.strip().split(',')
    dataCom.append([int(clusterAssment[count, 0]), int(lineArr[4])])
    count += 1
data = mat(dataCom)
for i in range(3):
    pointsInCluster = data[nonzero(clusterAssment[:, 0].A == i)[0]]
    # print pointsInCluster
    for j in range(3):
        temp.append(len(nonzero(mat(pointsInCluster)[:, 1].A == (j + 1))[0]))
    sums += sort(temp)[2]
    temp = []
print float(sums) / len(dataCom)
print numSamples