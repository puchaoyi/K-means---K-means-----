from numpy import *
import time
import matplotlib.pyplot as plt
from biKmeans import biKmeans
from biKmeans import showCluster

# step 1: load data
print "step 1: load data..."
dataSet = []
fileIn = open('E:\pythoncode\bisecting k-means\testHello.txt')
for line in fileIn.readlines():
    lineArr = line.strip().split('\t')
    dataSet.append([float(lineArr[0]), float(lineArr[1]), float(lineArr[2]), float(lineArr[3]), float(lineArr[4])])
print "step 2: clustering..."
dataSet = mat(dataSet)
 for i in xrange(dataSet.shape[5]):
    plt.plot(dataSet[i, 1:4], dataSet[i, 5], 'or')
 plt.show()