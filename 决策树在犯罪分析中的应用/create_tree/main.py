from Onehot import onehot
from become_onehot import sk_tree,clf_plot
import pandas as pd


if __name__ == '__main__':
    train_data = pd.read_excel('../create_data/DATA.xlsx')
    y_features = ['犯罪程度']
    y_data = onehot(train_data=train_data,features=y_features)
    x_features = []
    for item in train_data.columns[:-2]:
        x_features.append(item)
    x_data = onehot(train_data=train_data,features=x_features[::])
    try:
        model,clf_1,score = sk_tree(x=x_data,y=y_data)
    except:
        raise Exception('训练错误')
    try:
        clf_plot(clf_1)
    except:
        raise Exception('画图错误')
    print(len(x_data[0]))
