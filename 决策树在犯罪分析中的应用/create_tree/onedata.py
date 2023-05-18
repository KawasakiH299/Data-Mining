import Onehot
import pandas as pd
def readdata():
    train_data = pd.read_excel('../create_data/DATA.xlsx')
    result = Onehot.onehot(train_data)
    return result
