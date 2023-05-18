from sklearn import tree
from matplotlib import pyplot as plt

def sk_tree(x, y):
    '''
    :param x:
    :type x:
    :param y:
    :type y:
    :return:model(完成训练的决策树)
    :rtype: 决策树
    :return:clf决策树对象
    :rtype:决策树对象
    '''
    print(x, y)
    # 创建决策树
    clf = tree.DecisionTreeClassifier()
    # 训练模型
    model = clf.fit(x, y)
    score = model.score(x, y)
    return model, clf, score


def predi(model):
    '''
    :param model: 决策树模型
    :type model:
    :return: 预测结果predict_result
    :rtype: list
    '''
    # 手动创建测试集
    predict_data = [[1, 0, 1, 1], [2, 0, 1, 1]]
    # 预测是否
    predict_result = model.predict(predict_data)
    # 概率为
    predict_proba = model.predict_proba(predict_data)

    return predict_result, predict_proba

def clf_plot(clf1):
    plt.figure()
    tree.plot_tree(clf1, filled=True)
    plt.show()



