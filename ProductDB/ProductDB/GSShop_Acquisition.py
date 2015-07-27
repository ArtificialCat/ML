# -*- coding:utf-8 -*-

__author__ = 'KimHongTae'

import urllib2
from bs4 import BeautifulSoup

title_list = []
link_list = []
price_list = []
cnt = 140           ## The number of category products in the market


url = 'http://www.gsshop.com/sect/sectM.gs?sectid=1087852&lsectid=1079929&msectid=1087852&lseq=358308&gsid=' \
      'Sect-1079929-0-1&pg=' + str(cnt)

request = urllib2.Request(url)
response = urllib2.urlopen(request)
data = response.read()

soup = BeautifulSoup(data)

Title = soup.find_all('dt')
Price = soup.find_all('dd', {'class': 'price'})
Link = soup.find_all('span', {'new-open'}, 'button')


for idx in range(0, len(Title)-1):                  ## last <dt>...</dt> has commercial
    if str(Title[idx]).__contains__('<dt class') or str(Title[idx]).__contains__('<a href=') or str(Title[idx]).__contains__('<strong>'):
        pass

    elif str(Title[idx]).__contains__('span class'):
        start = '</span>'
        end = '</dt>'
        title_list.append(str(Title[idx]).split(start)[1].split(end)[0])

    else:
        start ='<dt>'
        end ='</dt>'
        title_list.append(str(Title[idx]).split(start)[1].split(end)[0])

for idx_ in range(0, len(Price)):
    if str(Price[idx_]).__contains__('a href'):
        pass

    else:
        start = '<strong>'
        end = '</strong>'
        price_list.append(str(Price[idx_]).split(start)[1].split(end)[0])

for idx__  in range(0, len(Link)):
    start = "goPrdLink('"
    end = "'"
    link_list.append(str(Link[idx__]).split(start)[1].split(end)[0])


f = open('/Users/KimHongTae/Downloads/GSShop.txt', 'w')
for index in range(0,len(title_list)):
    f.write(title_list[index] + '\t' + price_list[index] + '\t' + 'www.gsshop.com/' + link_list[index] + '\n')

f.close()

print str(len(title_list)) + ' ' + str(len(price_list)) + ' ' + str(len(link_list))


option_name = []
option_price = []
#
#
#
# f_ = open('/Users/KimHongTae/Downloads/GSShop_Detail.txt', 'w')
#
# for index_ in range(0, len(link_list)):
#
#     url_ = 'http://' + str(link_list[index_])
#
#     request_ = urllib2.Request(url_)
#     response_ = urllib2.urlopen(request_)
#     data_ = response_.read()
#
#     soup_ = BeautifulSoup(data_)
#     print soup_

