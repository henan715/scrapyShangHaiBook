# scrapyShangHaiBook
2016年8月上海图书馆，上海书展爬虫，用于爬取所有展出的4万余本书的书名、作者、ISBN编号、出版社、价格、展览区域信息，保存为Excel。

## 主要库
- BeautifulSoup
- Urllib2
- xlrd
- xlwt

## 代码结构
代码分为两块：MainSpider用于下载数据，通过BeautifulSoup解析网页内容，然后存储为Excel，刚开始打算存数据库，后来发现数据量太小，直接存储Excel吧，text2excel用于将txt数据转换为Excel数据（后来废弃不用了）。

![效果图Alt text](https://github.com/henan715/scrapyShangHaiBook/blob/master/screen.png)
