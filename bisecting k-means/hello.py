# Your optional code here
# You can import some modules or create additional functions

from numpy import *
import time
import matplotlib.pyplot as plt
from biKmeans import biKmeans
from biKmeans import showCluster

# step 1: load data
print "step 1: load data..."
dataSet = []
fileIn = open('testHello.txt')
for line in fileIn.readlines():
    lineArr = line.strip().split('\t')
    dataSet.append([float(lineArr[0]), float(lineArr[1])], float(lineArr[2])], float(lineArr[3])], float(lineArr[4])])

# step 2: clustering...
print "step 2: clustering..."
dataSet = mat(dataSet)
 for i in xrange(dataSet.shape[0]):
    plt.plot(dataSet[i, 1:16], dataSet[i, 1], 'or')
 plt.show()
# k = 4
# centroids, clusterAssment = biKmeans(dataSet, k)

# step 3: show the result
print "step 3: show the result..."
# showCluster(dataSet, k, centroids, clusterAssment)

#figure
#hold on
#row_num = size(Dat, 1)
#marker = '+o*.xv^><'
#
#    for i = 1:
#        row_num
#plt.plot(Data(i, 1: 16), marker(Data(i, 17)))
#end
