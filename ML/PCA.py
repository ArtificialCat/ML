__author__ = 'KimHongTae'

import numpy as np
from numpy import linalg


def pca(mat, reduceSize):
    cov = np.cov(m=mat, rowvar=True)
    eigenVal, eigenVec = linalg.eig(cov)
    eig_pairs = [(np.abs(eigenVal[i]), eigenVec[:,i]) for i in range(len(eigenVal))]
    eig_pairs.sort()
    eig_pairs.reverse()

    if reduceSize >= len(eig_pairs):
        print 'reduce size is bigger than feature size'

    else:
        wMat = np.vstack(eig_pairs[idx][1] for idx in range(reduceSize))
        principalComp = np.dot(wMat,mat)

        return wMat, principalComp

if __name__ == '__main__':

    testMat = np.array([[1,2,3],[4,7,1],[4,5,2],[4,4,5]])
    reduceSize = 3
    wMat,principalComp = pca(testMat,2)

    print wMat
    print '------------'
    print principalComp
    print '------------'
    print testMat
