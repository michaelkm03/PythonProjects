import urllib2
import re

symbols_dict = {}
with open('stocks.txt','r') as symbol_list:
    for i in symbol_list:
        words = str.split(i)
        stock_symbol = words[0]


i = 0
while i > -1:
    url = 'http://finance.yahoo.com/q?s='+stock_symbol+"&q1=1"
    htmlfile = urllib2.urlopen(url)
    htmltext = htmlfile.read()
    regex = '<span id="yfs_l84_'+stock_symbol+'">(.+?)</span>'
    pattern = re.compile(regex)
    price = re.findall(pattern,htmltext)
    print 'Last price of',stock_symbol,'is: ',''.join(price)
    i +=1