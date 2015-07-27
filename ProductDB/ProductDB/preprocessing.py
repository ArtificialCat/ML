# -*- coding:utf-8 -*-
__author__ = 'KimHongTae'

import sqlite3
import re
import pandas as pd

path = '/Users/KimHongTae/Downloads/GMARKET_Product.csv'
data = pd.read_csv(path, sep=',', engine='python')
data['MARKET'] = pd.Series('G-market', index= data.index)

path_ = '/Users/KimHongTae/Downloads/GSShop_Product.csv'
data_ = pd.read_csv(path_, sep=',', engine='python')
data_['MARKET'] = pd.Series('GSShop', index = data_.index)

## Regular Expression for extract Product code

offer = re.compile('[^ \s/(){}~,.ㄱ-ㅣ가-힣a-z]{8,}')
count = 0

for idx in range(0,len(data['TITLE'])):
    print offer.findall(data['TITLE'][idx])
    if offer.findall(data['TITLE'][idx]) != []:
        count += 1


print '----------------------------------------'

cnt_ = 0

for idx_ in range(0,len(data_['TITLE'])):

    print offer.findall(data_['TITLE'][idx_])
    if offer.findall(data_['TITLE'][idx_]) != []:
        cnt_ += 1

print '\n' + 'Product Code exist:' + str(count)
print 'Total Product count:' + str(len(data))
print '\n'
print 'Product Code exist:' + str(cnt_)
print 'Total Product count:' + str(len(data_))

# con = sqlite3.connect('Matching.db')
# cursor = con.cursor()
# cursor.execute('CREATE TABLE GMARKET_GSSHOP (GMARKET_CODE TEXT, GSSHOP_CODE TEXT)')
# cursor.execute('INSERT INTO VALUES(offer.findall(data["TITLE"]), offer.findall(data_["TITLE"]))')

