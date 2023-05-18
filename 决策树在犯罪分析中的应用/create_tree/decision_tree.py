from sklearn import tree
from matplotlib import pyplot as plt

def data():
    '''
    :return:数字特征
    :rtype: list
    '''
    # 手动构建数字特征
    X = [[0,2,0,0],[1,2,0,0],[2,1,0,0],
         [2,0,1,0],[2,0,1,1],[1,0,1,1],
         [0,1,0,0],[0,0,1,0]]
    # 8条数据的类别
    Y = [0,1,1,1,0,1,0,1]
    return X,Y

def sk_tree(x,y):
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
    print(x,y)
    #创建决策树
    clf = tree.DecisionTreeClassifier()
    #训练模型
    model = clf.fit(x,y)
    score = model.score(x,y)
    return model,clf,score

def predi(model):
    '''
    :param model: 决策树模型
    :type model:
    :return: 预测结果predict_result
    :rtype: list
    '''
    # 手动创建测试集
    predict_data = [[1,0,1,1],[2,0,1,1]]
    #预测是否
    predict_result = model.predict(predict_data)
    #概率为
    predict_proba = model.predict_proba(predict_data)

    return predict_result,predict_proba


def clf_plot(clf,fn):
    #设置特征名称，默认为X[0],X[1],X[2]......
    # fn = ['age','income','student','credit']
    #设置类别种类
    # cn = ['No','Yes']
    plt.figure()
    #filled生成完全树
    # tree.plot_tree(clf,feature_names=fn,class_names=cn,filled=True)
    # for arg in args:
    #     print(arg)
    tree.plot_tree(clf,feature_names=fn,filled=True)
    plt.show()

if __name__ == '__main__':
    x,y = data()
    model,clf,score = sk_tree(x,y)
    result,pro = predi(model)
    clf_plot(clf,fn=['age','income','student','credit'])

    print(result)
    print(pro)
    print(score)


    # 年龄  收入  是否学生   信用状况  是否买电脑
    #  0     2      1        0       1

    # 一个列表的数据表示一个人，如果结果为1表示买电脑，如果为0就是不买电脑。