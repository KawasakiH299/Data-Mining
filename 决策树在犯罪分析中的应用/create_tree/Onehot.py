from sklearn.feature_extraction import DictVectorizer

def onehot(train_data,features:list):

   #特征选择
    train_features = train_data[features]

    dvec=DictVectorizer(sparse=False)

    # 调用热编码器fit_transfrom方法，转化为数字特征。
    train_features = dvec.fit_transform(train_features.to_dict('records'))
    print(train_features)
    return train_features