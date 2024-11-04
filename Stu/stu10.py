import operator
from numpy import tile, zeros, shape, array


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    # argsort方法返回将数组值从小到大排序之后的索引值
    classCount = {}
    # 字典
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def file2matrix(filename):
    fr = open(filename)
    arrayOfLines = fr.readlines()
    numberOfLines = len(arrayOfLines)
    # 得到文件行数
    returnMat = zeros((numberOfLines, 3))
    # 创建二维numpy数组
    classLabelVector = []
    # 创建存放标签的列表
    index = 0
    for line in arrayOfLines:
        line = line.strip()
        # 移除字符串头尾的空格，生成新字符串
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        # 向全零元素的ndarray中添加数据
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector


def autoNorm(dataSet):
    minVals = dataSet.min(0)
    # axis=0按列统计，跨行统计，所有列的最小值
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))
    return normDataSet, ranges, minVals


def datingClassTest():
    TestRatio = 0.10
    # 留出10％做测试数据
    datingDataMat, datingLabels = file2matrix("D:\\chapter6\\datingSet.txt")
    # 加载约会配对数据集
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * TestRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs: m], 3)
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]):
            errorCount += 1.0
    print("the total error rate is: %f" % (errorCount / float(numTestVecs)))
    print("the total error number is: ", errorCount)


def classifyPerson():
    resultList = ['一点也不喜欢', '有点喜欢', '比较喜欢']
    percentTats = float(input("玩游戏、看视频消耗时间百分比："))
    ffMiles = float(input("每年飞行的里程数："))
    iceCream = float(input("每周消费冰淇淋的公升数："))
    datingDataMat, datingLabels = file2matrix("D:\\chapter6\\datingSet.txt")
    norMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles, percentTats, iceCream])
    classifierResult = classify0((inArr - minVals) / ranges, norMat, datingLabels, 3)
    print("\n你对约会对象可能的喜欢程度：", resultList[classifierResult - 1])


datingClassTest()
classifyPerson()
