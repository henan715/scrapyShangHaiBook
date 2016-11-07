# coding:utf-8
import xlrd
import xlwt
def saveToExcel():
    """
    save the content from createBsObj(content) into excel.
    :param content:
    :return:
    """
    wbk = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = wbk.add_sheet("sheet1",cell_overwrite_ok=True)
    wbk.save('data.xls')

    xlsfile=r'./data.xls'
    book = xlrd.open_workbook(xlsfile)
    sheet_name = book.sheet_names()[0]
    sheet1 = book.sheet_by_name(sheet_name)

    nrows = sheet1.nrows
    ncols = sheet1.ncols
    file = open('./test.txt','r')

    i=0
    for line in file.readlines():
        str=line.split(', ')
        sheet.write(nrows+i,ncols,str[0].replace('(','').replace(',',''))
        sheet.write(nrows+i,ncols+1,str[1].replace(',',''))
        sheet.write(nrows+i,ncols+2,str[2].replace(',',''))
        sheet.write(nrows+i,ncols+3,str[3].replace(',',''))
        sheet.write(nrows+i,ncols+4,str[4].replace(',',''))
        sheet.write(nrows+i,ncols+5,str[5].replace(',',''))
        sheet.write(nrows+i,ncols+6,str[6].replace(',','').replace(')',''))
        i=i+1
    # sheet.write(nrows+i,ncols,bookTitle)
    wbk.save('data.xls')

saveToExcel()