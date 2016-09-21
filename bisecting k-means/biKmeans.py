# -*- coding: utf-8 -*-
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


# calculate Euclidean distance
def euclDistance(vector1, vector2):
    return sqrt(sum(power(vector2 - vector1, 2)))

# init centroids with random samples


def initCentroids(dataSet, k):
    numSamples, dim = dataSet.shape
    centroids = zeros((k, dim))
    for i in range(k):
        index = int(random.uniform(0, numSamples))
        centroids[i, :] = dataSet[index, :]
    return centroids

# k-means cluster


def kmeans(dataSet, k):
    numSamples = dataSet.shape[0]
    # first column stores which cluster this sample belongs to,
    # second column stores the error between this sample and its centroid
    clusterAssment = mat(zeros((numSamples, 2)))
    clusterChanged = True

    # step 1: init centroids
    centroids = initCentroids(dataSet, k)

    while clusterChanged:
        clusterChanged = False
        # for each sample
        for i in xrange(numSamples):
            minDist = 100000.0
            minIndex = 0
            # for each centroid
            # step 2: find the centroid who is closest
            for j in range(k):
                distance = euclDistance(centroids[j, :], dataSet[i, :])
                if distance < minDist:
                    minDist = distance
                    minIndex = j

            # step 3: update its cluster
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True
                clusterAssment[i, :] = minIndex, minDist**2

        # step 4: update centroids
        for j in range(k):
            pointsInCluster = dataSet[nonzero(clusterAssment[:, 0].A == j)[0]]
            centroids[j, :] = mean(pointsInCluster, axis=0)

    print 'Congratulations, cluster using k-means complete!'
    return centroids, clusterAssment

# bisecting k-means cluster


def biKmeans(dataSet, k):
    numSamples = dataSet.shape[0]
    # first column stores which cluster this sample belongs to,
    # second column stores the error between this sample and its centroid
    clusterAssment = mat(zeros((numSamples, 2)))

    # step 1: the init cluster is the whole data set
    # -*- coding: utf-8 -*-  axis=0计算列，1计算行但是tolist()[0]表示去掉括号
    centroid = mean(dataSet, axis=0).tolist()[0]
    centList = [centroid]
    for i in xrange(numSamples):
        clusterAssment[i, 1] = euclDistance(mat(centroid), dataSet[i, :])**2

    while len(centList) < k:
        # min sum of square error
        minSSE = 100000.0
        # len(centList)中心点的个数
        numCurrCluster = len(centList)
        # for each cluster
        for i in range(numCurrCluster):
            # step 2: get samples in cluster i
            pointsInCurrCluster = dataSet[
                nonzero(clusterAssment[:, 0].A == i)[0], :]
            #  .A的意思：获取到的nonzero(clusterAssment[:,0]元素的一个属性

            # step 3: cluster it to 2 sub-clusters using k-means
            centroids, splitClusterAssment = kmeans(pointsInCurrCluster, 2)

            # step 4: calculate the sum of square error after split this
            # cluster
            splitSSE = sum(splitClusterAssment[:, 1])
            notSplitSSE = sum(clusterAssment[nonzero(
                clusterAssment[:, 0].A != i)[0], 1])
            currSplitSSE = splitSSE + notSplitSSE

            # step 5: find the best split cluster which has the min sum of
            # square error
            if currSplitSSE < minSSE:
                minSSE = currSplitSSE
                bestCentroidToSplit = i
                bestNewCentroids = centroids.copy()
                bestClusterAssment = splitClusterAssment.copy()

        # step 6: modify the cluster index for adding new cluster
        bestClusterAssment[nonzero(bestClusterAssment[:, 0].A == 1)[
            0], 0] = numCurrCluster
        bestClusterAssment[nonzero(bestClusterAssment[:, 0].A == 0)[
            0], 0] = bestCentroidToSplit

        # step 7: update and append the centroids of the new 2 sub-cluster
        centList[bestCentroidToSplit] = bestNewCentroids[0, :]
        centList.append(bestNewCentroids[1, :])

        # step 8: update the index and error of the samples whose cluster have
        # been changed
        clusterAssment[nonzero(clusterAssment[:, 0].A ==
                               bestCentroidToSplit), :] = bestClusterAssment

    print 'Congratulations, cluster using bi-kmeans complete!'
    return mat(centList), clusterAssment

# show your cluster only available with 2-D data


def showCluster(dataSet, k, centroids, clusterAssment):
    numSamples, dim = dataSet.shape
    if dim != 2:
        print "Sorry! I can not draw because the dimension of your data is not 2!"
        return 1

    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    if k > len(mark):
        print "Sorry! Your k is too large! please contact Zouxy"
        return 1

    # draw all samples
    for i in xrange(numSamples):
        markIndex = int(clusterAssment[i, 0])
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])

    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
    # draw the centroids
    for i in range(k):
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize=12)

    plt.show()
