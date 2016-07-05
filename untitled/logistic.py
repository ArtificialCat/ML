import numpy as np
import pandas as pd
import seaborn as sns


def logisticRegression(dataX, dataY, alpha=0.01):
    coefficient = np.random.random_sample((dataX.shape[1],))
    bias = np.random.random_sample((dataX.shape[0],))

    logit = 1/(1+bias+np.exp(-np.dot(dataX,coefficient)))
    cost = (-1/dataX.shape[0])*np.sum(dataY*np.log(logit)+(1-dataY)*np.log(1-logit), axis=0, dtype='float64')

    for j in xrange(1000):
        for idx in range(0,len(coefficient)):
            coefficient[idx] = coefficient[idx] - (alpha/dataX.shape[0])*\
            np.sum(np.multiply((logit - dataY),dataX[dataX.columns[idx]]),axis=0)

    return logit,cost,coefficient


def evaluation(logit,dataY,threshold):
    accuracyCnt = 0
    predictLabel = []

    for pred in range(0,logit.shape[0]):
        if logit[pred] >= threshold:
            predictLabel[pred] = 1.0

        else:
            predictLabel[pred] = 0.0


    for idx in range(0,dataY.shape[0]):
        if predictLabel[idx] + dataY[idx] <> 1.0:
            accuracyCnt += 1

    accuracy = float(accuracyCnt) / dataY.shape[0]
    predictLabel

    return accuracy,predictLabel



if __name__ == '__main__':

    sns.set(color_codes=True)
    red_X = np.random.normal(16, 6, 1000)
    red_Y = np.random.normal(20, 7, 1000)
    blue_X = np.random.normal(30,5, 1000)
    blue_Y = np.random.normal(10,12,1000)

    redData = pd.DataFrame({'X':red_X,'Y':red_Y,'label':0})
    blueData = pd.DataFrame({'X':blue_X, 'Y':blue_Y, 'label':1})
    totalData = redData.append(blueData)
    dataX = totalData[['X','Y']]
    dataY = totalData['label']

    logit,cost,coefficient = logisticRegression(dataX, dataY, 0.05)
    print cost
    print '--------------'
    print logit

    accuracy, predictLabeling = evaluation(logit,dataY,0.65)
    print accuracy