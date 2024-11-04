import numpy as np
import operator

def createDataSet():
    group = np.array([[3, 104], [2, 100], [1, 81], [101, 10], [99, 5], [98, 2]])
    labels = ['爱情片', '爱情片', '爱情片', '动作片', '动作片', '动作片']
    return group, labels
def KNN(in_x, x_labels, y_labels, k):
    x_labels_size = x_labels.shape[0]
    distances = (np.tile(in_x, (x_labels_size, 1)) - x_labels) ** 2
    ad_distances = distances.sum(axis=1)
    sq_distances = ad_distances ** 0.5
    ed_distances = sq_distances.argsort()

    classdict = {}
    for i in range(k):
        voteI_label = y_labels[ed_distances[i]]
        classdict[voteI_label] = classdict.get(voteI_label, 0) + 1

    sort_classdict = sorted(classdict.items(), key=operator.itemgetter(1), reverse=True)
    return sort_classdict[0][0]


if __name__ == '__main__':
    group, labels = createDataSet()
    test_x = [18, 90]
    print('输入数据所对应的类别是: {}'.format(KNN(test_x, group, labels, 3)))
