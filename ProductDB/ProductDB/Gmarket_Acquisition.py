__author__ = 'KimHongTae'


import urllib2
from bs4 import BeautifulSoup


title_list = []
link_list = []
price_list = []

for page in range(1, 45):

    url = 'http://category.gmarket.co.kr/listview/List.aspx?page=' + str(page) + '&page2=1&page_size=80&keyword=&keywordSeq=&list_type=LIST&searchType=&gdlc_cd=100000032&gdmc_cd=200001054&gdsc_cd=&InResult=&PrevKeyword=&exceptKeyword=&sortfield=focus_rank_desc&IsMileage=&IsDiscount=&IsStamp=&IsOversea=&IsOld=&IsFeeFree=&IsGuild=&IsVisit=&IsGift=&IsWithoutFee=&delFee=&TradWay=&OrderType=&PriceStart=5500&PriceEnd=11000000&keywordOrg=&keywordCVT=&keywordCVTi=&SearchClassFormWord=&IsTabSearch=&anchor=list_top_anchor&ecp_gdlc=&ecp_gdmc=&IsNickName=&IsReturnFeeFree=&IsLotteItem=&IsBrandOnItem=&IsGlobalItem=&categoryType=M&inventoryIndex=&attributeElementList=&catalogID=&brfd_brand_no=&pp_sell_cust_no=&IsTpl=&SubdivYN=&vclass_cd=&sel_attrib_1=&sel_attrib_2=&sel_attrib_3=&sel_attrib_4=&sel_attrib_5=&sel_attrib_6=&sel_idx_1=&sel_idx_2=&sel_idx_3=&sel_idx_4=&callFrom=&plusGoodsCount=5&smartShippingItemCount=0#list_top_anchor'
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    data = response.read()

    soup = BeautifulSoup(data)

    Title_Link = soup('div', {'class': 'title', })
    Price = soup('a', {'class': 'discount-price', })


    for tit in Title_Link:
        tit_ = str(tit)
        start ='">'
        end = '</a>'

        title = ((tit_.split(start)[2]).split(end)[0]).lstrip()
        link = (((tit_.split(start)[1].split(end)[0])).split('http://')[1]).split(', ')[0]

        title_list.append(str(title))
        link_list.append(link)
        # print title
        print title + '\n' + link

    for var in Price:

        var_ = str(var)
        start = '<span>'
        end = '</span>'

        price = (var_.split(start)[1]).split(end)[0]
        price_list.append(price)
        print price


f = open('/Users/KimHongTae/Downloads/MainTitle.txt', 'w')

for idx in range(0,len(title_list)):
    Result = title_list[idx] + '\t' + price_list[idx] + '\t' + link_list[idx]
    f.write(Result + '\n')

f.close()


link_list_ = []         ## link list for option list
option_list = []        ## product option list
price_list_ = []         ## price list for option list


for idx_ in range(1, len(link_list)):

    if str(link_list[idx_]).__contains__('smartclick'):
        pass

    elif str(link_list[idx_]).__contains__('pds'):
        pass

    else:
        url_ = 'https://' + str(link_list[idx_]).replace("'", '')
        request_ = urllib2.Request(url_)
        response_ = urllib2.urlopen(request_)
        data_ = response_.read()
        # print data_

        soup_ = BeautifulSoup(data_)
        option_ = soup_.find_all('option')[3:len(soup_.find_all('option'))-3]
        print option_

        if len(option_) != 0:
            for index in range(0,len(option_)):
                link_list_.append(link_list[idx_])
                option_list.append(option_[index])

        else:
            link_list_.append(link_list[idx_])
            option_list.append('No option')

print len(link_list_)
print len(option_list)


f_ = open('/Users/KimHongTae/Downloads/DetailOption.txt', 'w')

for index__ in range(0, len(link_list_)):

    Result_ = str(link_list_[index__]) + '\t' + str(option_list[index__])
    f_.write(Result_ + '\n')

f_.close()