def yie_da():

    yield (1,2,3)

tu = yie_da()
tu2 = tuple(tu)
print(type(tu2))
print(tu2)

def writ_xlmx(tu2):
    import  xlsxwriter
    workbook = xlsxwriter.Workbook('test2.xlsx')
    worksheet = workbook.add_worksheet('test1')
    worksheet.write_row('A1',tu2[0])
    workbook.close()