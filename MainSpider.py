# coding:utf-8
from bs4 import BeautifulSoup
from urllib2 import urlopen
import xlrd
import xlwt
import sys

def getHtml(pageNo):
    """
    get html content and return the raw html page.
    :param pageNo: the page number,from 0~2212.
    :return:
    """
    startUrl = 'http://search.shbookfair.cn/2014.htm?_gat=1&_ga=GA1.2.442062171.1470810485&page='+str(pageNo)
    try:
        html = urlopen(startUrl)
        return html.read()
    except Exception,e:
        print "===Wrong===", str(e)
        return None

def createBsObj(content):
    """
    get html string from getHtml(pageNo), then transform it into a BeautifulSoup object, then get the table content
    of the page.
    :param content:
    :return:
    """
    if(len(content)==0):
        print "===Your Content Is None!==="
        return

    bsObj = BeautifulSoup(content, 'html.parser',from_encoding="gb18030")
    table = bsObj.find("table",{"class":"display"}).find("tbody").findAll("tr")
    table_list=[[]]*len(table)
    i=0
    for trItem in table:
        bookTitle = trItem.find("td",{"class":"bookTitle"}).get_text().strip().replace(',','-')
        bookAuthor = trItem.find("td",{"class":"bookAuthor"}).get_text().strip().replace(' ','.')
        bookEAN = trItem.find("td",{"class":"bookEAN"}).get_text().strip()
        bookAlias = trItem.find("td",{"class":"pubAlias"}).get_text().strip()
        bookPrice = trItem.find("td",{"class":"bookPrice"}).get_text().strip()
        bookYear = trItem.find("td",{"class":"bookYear"}).get_text().strip()
        bookZone = trItem.find("td",{"class":"zones"}).get_text().strip()
        item_dict=(bookTitle, bookAuthor, bookEAN, bookAlias, bookPrice, bookYear, bookZone)
        #print bookTitle
        table_list[i]=item_dict
        i=i+1
    return table_list


def saveToExcel(content):
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
    # sheet.write(nrows+i,ncols,bookTitle)
    wbk.save('data.xls')


# main call function
if __name__=="__main__":
    file = open('./test.txt','w+')
    for i in range(1,2212):#2212
        print 'No '+str(i)+' is running...'
        try:
            lst = createBsObj(getHtml(i))
            for item in lst:
                file.write(str(item).decode("unicode-escape").encode("utf-8").replace("u\'","").replace("\'","").replace("\"","")+'\n')
        except Exception,e:
            print e
            continue
    file.close()