import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'http://apis.data.go.kr/B552061/frequentzoneLg/getRestFrequentzoneLg'
queryParams = '?' + 'serviceKey=' + 'nBR6ds%2BFTLtKBfkc9qEKhBBGdZF09DnpkSRWSKTyxiHp%2BRVBtJbWjTQMqvvMb%2FVf0TGceYhCeGyvpHtJAhIlJA%3D%3D' \
+ '&searchYearCd=' + '2017' \
+ '&siDo=' + '26' \
+ '&guGun=' + '110' \
+ '&type=' + 'xml' \
+ '&numOfRows=' + '25' \
+ '&pageNo=' + '1'

url = url + queryParams

result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")

data1 = bs_obj.findAll('spot_nm')      #다발지역명
data2 = bs_obj.findAll('occrrnc_cnt')   #발생건수
data3 = bs_obj.findAll('dth_dnv_cnt')   #사망자
data4 = bs_obj.findAll('caslt_cnt')     #부상자
data5 = bs_obj.findAll('se_dnv_cnt')    #중상자
data6 = bs_obj.findAll('sl_dnv_cnt')    #경상자

#    list_data = {'다발지역명':[],'발생건수':[],'사망자수':[],\
#    '부상자수':[],'중상':[],'경상':[],\
#    '시군구':['중구','서구','동구','영도구','부산진구','동래구','남구','북구','해운대구','사하구','금정구','강서구','연제구','수영구','사상구','기장군']}
data = {'시군구': [],'다발지역명':[],'발생건수':[],'사망자수':[],'부상자수':[],'중상':[],'경상':[]}
d1,d2,d3,d4,d5,d6,d7 = [],[],[],[],[],[],[]

for i in range(0,len(data1)):
    d1.append(data1[i].get_text())
    d2.append(data2[i].get_text())
    d3.append(data3[i].get_text())
    d4.append(data4[i].get_text())
    d5.append(data5[i].get_text())
    d6.append(data6[i].get_text())
    d7.append('중구')

data['다발지역명'] = d1
data['발생건수'] = d2
data['사망자수'] = d3
data['부상자수'] = d4
data['중상'] = d5
data['경상'] = d6
data['시군구'] = d7

df_110_1 = pd.DataFrame(data, columns = ['시군구','다발지역명','발생건수','사망자수','부상자수','중상','경상'])
#print(df_110_1)
