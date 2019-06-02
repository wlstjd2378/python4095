import requests
from bs4 import BeautifulSoup

# 지자체별사고 다발지역정보 조회 서비스
# 중구 110 동구 170   부산진구 230 남구 290 해운대구 350 금정구 410 연제구 470 사상구 530
# 서구 140 영도구 200   동래구 260 북구 320   사하구 380 강서구 440 수영구 500 기장군 710


list_region_code = {'중구' : '110', '서구' :'140','동구':'170','영도구':'200','부산진구':'230','동래구':'260','남구':'290','북구':'320','해운대구':'350',\
'사하구':'380','금정구':'410','강서구':'440','연제구':'470','수영구':'500','사상구':'530','기장군':'710'}
#list_region = ['중구','서구','동구','영도구','부산진구','동래구','남구','북구','해운대구','사하구','금정구','강서구','연제구','수영구','사상구','기장군']


list_pusan_data = []
#for i in list_region_code.values():
GuGun = '110'

url = 'http://apis.data.go.kr/B552061/frequentzoneLg/getRestFrequentzoneLg'
queryParams = '?' + 'serviceKey=' + 'nBR6ds%2BFTLtKBfkc9qEKhBBGdZF09DnpkSRWSKTyxiHp%2BRVBtJbWjTQMqvvMb%2FVf0TGceYhCeGyvpHtJAhIlJA%3D%3D' \
+ '&searchYearCd=' + '2017' \
+ '&siDo=' + '26' \
+ '&guGun=' + GuGun \
+ '&type=' + 'xml' \
+ '&numOfRows=' + '25' \
+ '&pageNo=' + '1'

url = url + queryParams

result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")
#print(bs_obj)

data1 = bs_obj.findAll('spot_nm')      #다발지역명
data2 = bs_obj.findAll('occrrnc_cnt')   #발생건수
data3 = bs_obj.findAll('dth_dnv_cnt')   #사망자
data4 = bs_obj.findAll('caslt_cnt')     #사상자
data5 = bs_obj.findAll('se_dnv_cnt')    #중상자
data6 = bs_obj.findAll('sl_dnv_cnt')    #경상자

#    list_data = {'다발지역명':[],'발생건수':[],'사망자수':[],\
#    '부상자수':[],'중상':[],'경상':[],\
#    '시군구':['중구','서구','동구','영도구','부산진구','동래구','남구','북구','해운대구','사하구','금정구','강서구','연제구','수영구','사상구','기장군']}

list_data = []
for i in range(0,len(data1)):
    list_data.append([data1[i].get_text(),data2[i].get_text()\
    ,data3[i].get_text(),data4[i].get_text(),data5[i].get_text(),data6[i].get_text()]) #.get_text() 태그제거임
list_pusan_data.append(list_data)

print(list_pusan_data)
