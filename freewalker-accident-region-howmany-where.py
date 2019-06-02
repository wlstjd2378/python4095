import requests
from bs4 import BeautifulSoup

#보행자무단횡단사고다발지역정보서비스
list_region_code = ['110','140','170','200','230','260','290','320','350','380'\
,'410','440','470','500','530','710']
list_pusan_data = []

for i in list_region_code:
    GuGun = i

    url = 'http://apis.data.go.kr/B552061/jaywalking/getRestJaywalking'
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
    #    print(bs_obj)

    data1 = bs_obj.findAll('spot_nm')      #다발지역명
    data2 = bs_obj.findAll('occrrnc_cnt')   #발생건수
    data3 = bs_obj.findAll('caslt_cnt')     #사상자
    data4 = bs_obj.findAll('dth_dnv_cnt')   #사망자
    data5 = bs_obj.findAll('se_dnv_cnt')    #중상자
    data6 = bs_obj.findAll('sl_dnv_cnt')    #경상자

    list_data = []
    for i in range(0,len(data1)):
        list_data.append([data1[i].get_text(),data2[i].get_text()\
        ,data3[i].get_text(),data4[i].get_text(),data5[i].get_text(),data6[i].get_text()]) #.get_text() 태그제거임
    list_pusan_data.append(list_data)

#print(len(list_pusan_data))
for i in list_pusan_data:
    print(i)
