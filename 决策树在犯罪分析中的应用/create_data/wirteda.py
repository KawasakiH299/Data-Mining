import xlsxwriter
workbook = xlsxwriter.Workbook('DATA2.xlsx')
worksheet = workbook.add_worksheet('sheet1')

data =(['有无固定职业', '家庭经济状况','年龄','文化程度','有无特长','社会犯罪记录', '违法记录','家庭和睦状况','犯罪记录次数','是否经常赌博','犯罪程度'],
    ['无','差','30-40','初中','否','有','差','有',4,'是','严重'],
    ['有','中','20-30','中专','否','无','差','无',0,'是','较轻'],
    ['有','差','<20','高中','否','无','中','无',1,'否','较轻'],
    ['无','差','30-40','初中','有','无','中','有',1,'是','严重'],
    ['无','差','>40','初中','有','有','差','无',2,'是','严重'],
    ['有','差','20-30','高中','有','有','中','有',6,'是','严重'],
    ['无','差','20-30','中专','否','无','中','有',1,'否','较轻'],
    ['有','差','30-40','大专','有','有','差','无',3,'是','严重'],
    ['无','中','<20','初中','有','无','好','有',5,'是','严重'],
    ['无','差','20-30','初中','否','有','差','无',0,'否','严重'],
    ['有','好','<20','高中','否','无','差','有',1,'是','较轻'],
    ['无','差','30-40','初中','有','无','中','有',0,'是','严重'],
    ['无','中','30-40','初中','否','无','差','有',1,'是','较轻'],
    ['有','差','>40','小学','否','有','中','无',2,'否','严重'],
    ['无','差','>40','初中','否','无','差','无',0,'否','严重'],
    ['无','差','30-40','高中','否','无','好','无',4,'否','较轻'],
    ['无','好','20-30','中专','有','无','差','有',2,'否','较轻'],
       )

def read_data(source_data):
    '''
    :param source_data: 写入表格的数据
    :type source_data: tuple
    :return: 一个生成器
    :rtype: list
    '''
    for data in source_data:
        yield data

def write_data(source_data):
    '''
    :param source_data: 写入表格的数据
    :type source_data: tuple
    :return: None
    :rtype: None
    '''
    for i in range(len(source_data)):
        worksheet.write_row(i,0,tuple(read_data(source_data))[i])

if __name__ == '__main__':
    write_data(data)
    workbook.close()
