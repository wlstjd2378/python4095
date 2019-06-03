# 부산시 안전 도로 만들기 
학과 | 학번 | 성명
---- | ---- | ---- 
# 수학과 |201511147 |최진성


## 프로젝트 개요
공공데이터(open-api와 file data)를 이용한 부산시 도로안전 위험 구군과 시급한 개선을 요구하는 사고다발지역을 
DataFrame과 시각화로 밝혀 안전한 부산광역시 교통환경을 조성하고자 함

## 사용한 공공데이터 
[데이터보기]
http://apis.data.go.kr/B552061/frequentzoneLg/getRestFrequentzoneLg?serviceKey=nBR6ds%2BFTLtKBfkc9qEKhBBGdZF09DnpkSRWSKTyxiHp%2BRVBtJbWjTQMqvvMb%2FVf0TGceYhCeGyvpHtJAhIlJA%3D%3D&searchYearCd=2017&siDo=26&guGun=230&type=xml&numOfRows=10&pageNo=1
http://apis.data.go.kr/B552061/jaywalking/getRestJaywalking?serviceKey=nBR6ds%2BFTLtKBfkc9qEKhBBGdZF09DnpkSRWSKTyxiHp%2BRVBtJbWjTQMqvvMb%2FVf0TGceYhCeGyvpHtJAhIlJA%3D%3D&searchYearCd=2015&siDo=11&guGun=320&type=xml&numOfRows=10&pageNo=1
http://apis.data.go.kr/B552061/frequentzoneLgrViolt/getRestFrequentzoneLgrViolt?serviceKey=nBR6ds%2BFTLtKBfkc9qEKhBBGdZF09DnpkSRWSKTyxiHp%2BRVBtJbWjTQMqvvMb%2FVf0TGceYhCeGyvpHtJAhIlJA%3D%3D&searchYearCd=2017&siDo=11&guGun=680&type=xml&numOfRows=10&pageNo=1
https://www.data.go.kr/dataset/fileDownload.do?atchFileId=FILE_000000001486106&fileDetailSn=1&publicDataDetailPk=uddi:33e89a52-4535-4727-bceb-f6685e708421

## 소스
* [링크로 소스 내용 보기](https://github.com/cybermin/python2019/blob/master/tes.py) 

* 코드 삽입
~~~python
#1 - 부산시 중구 사고다발지역 open-api를 통해 Dataframe 만들기
# (무단횡단&신호위반&중앙선침범 사고다발지역 모두 부산시 각 구군별로 구군코드를 활용하여 같은 방법으로 Dataframe을 만들어 주었음

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



#2 각 구군별 사고 다발지역 Dataframe을 합치고 새로운 csv파일 만들기
# (무단횡단&신호위반&중앙선침범 사고다발지역 모두 부산시 각 구군별로 구군코드를 활용하여 같은 방법으로 Dataframe을 만들어 주었음

import requests
from bs4 import BeautifulSoup
import pandas as pd

import md_110_1
import md_140_1
import md_170_1
import md_200_1
import md_230_1
import md_260_1
import md_290_1
import md_320_1
import md_350_1
import md_380_1
import md_410_1
import md_440_1
import md_470_1
import md_500_1
import md_530_1
import md_710_1

df_1 = pd.concat([md_110_1.df_110_1,md_140_1.df_140_1,md_170_1.df_170_1,\
md_200_1.df_200_1,md_230_1.df_230_1,md_260_1.df_260_1,md_290_1.df_290_1,\
md_320_1.df_320_1,md_350_1.df_350_1,md_380_1.df_380_1,md_410_1.df_410_1,\
md_440_1.df_440_1,md_470_1.df_470_1,md_500_1.df_500_1,md_530_1.df_530_1,\
md_710_1.df_710_1])

df_1 = df_1.reset_index(drop=True)
#print(df_1)
df_1.to_csv('accident_region_frequent.csv', mode = 'w')



#3 17년부산광역시교통사고발생현황&17년_시도_시군구별_도로형태별_교통사고&17년_시도_시군구별_사고유형별_교통사고를 원하는 형태로 
#  분할해 주었음. (사용하지 않은 데이터도 모두 분할함)

import pandas as pd
import numpy as np


dfPusan = pd.read_csv('2017년부산광역시교통사고발생현황.csv', engine = 'python')
#print(dfPusan)
#dfPusan['사망자 수p'] = dfPusan['사망자 수'] / dfPusan['발생건수']
#print(dfPusan)

dfA = pd.read_csv("2017년_시도_시군구별_도로형태별_교통사고.csv", engine ='python')
dfA = dfA.iloc[251:398]
#print(dfA)

dfA_110 = dfA.loc[dfA['시군구'] == '중구', '시군구':'부상자수']
#print(dfA_110)

dfA_140 = dfA.loc[dfA['시군구'] == '서구', '시군구':'부상자수']
#print(dfA_140)

dfA_170 = dfA.loc[dfA['시군구'] == '동구', '시군구':'부상자수']
#print(dfA_170)

dfA_200 = dfA.loc[dfA['시군구'] == '영도구', '시군구':'부상자수']
#print(dfA_200)

dfA_230 = dfA.loc[dfA['시군구'] == '부산진구', '시군구':'부상자수']
#print(dfA_230)

dfA_260 = dfA.loc[dfA['시군구'] == '동래구', '시군구':'부상자수']
#print(dfA_260)

dfA_290 = dfA.loc[dfA['시군구'] == '남구', '시군구':'부상자수']
#print(dfA_290)

dfA_320 = dfA.loc[dfA['시군구'] == '북구', '시군구':'부상자수']
#print(dfA_320)

dfA_350 = dfA.loc[dfA['시군구'] == '해운대구', '시군구':'부상자수']
#print(dfA_350)

dfA_380 = dfA.loc[dfA['시군구'] == '사하구', '시군구':'부상자수']
#print(dfA_380)

dfA_410 = dfA.loc[dfA['시군구'] == '금정구', '시군구':'부상자수']
#print(dfA_410)

dfA_440 = dfA.loc[dfA['시군구'] == '강서구', '시군구':'부상자수']
#print(dfA_440)

dfA_470 = dfA.loc[dfA['시군구'] == '연제구', '시군구':'부상자수']
#print(dfA_470)

dfA_500 = dfA.loc[dfA['시군구'] == '수영구', '시군구':'부상자수']
#print(dfA_500)

dfA_530 = dfA.loc[dfA['시군구'] == '사상구', '시군구':'부상자수']
#print(dfA_530)

dfA_710 = dfA.loc[dfA['시군구'] == '기장군', '시군구':'부상자수']
#print(dfA_710)


dfB = pd.read_csv("2017년_시도_시군구별_사고유형별_교통사고.csv", engine = 'python')
dfB = dfB.loc[361:588,['시군구','사고유형대분류','사고유형','발생건수','사망자수','부상자수','중상','경상']]
#print(dfB)

dfB_110 = dfB.loc[dfB['시군구'] == '중구', '시군구':'부상자수']
#print(dfB_110)

dfB_140 = dfB.loc[dfB['시군구'] == '서구', '시군구':'부상자수']
#print(dfB_140)

dfB_170 = dfB.loc[dfB['시군구'] == '동구', '시군구':'부상자수']
#print(dfB_170)

dfB_200 = dfB.loc[dfB['시군구'] == '영도구', '시군구':'부상자수']
#print(dfB_200)

dfB_230 = dfB.loc[dfB['시군구'] == '부산진구', '시군구':'부상자수']
#print(dfB_230)

dfB_260 = dfB.loc[dfB['시군구'] == '동래구', '시군구':'부상자수']
#print(dfB_260)

dfB_290 = dfB.loc[dfB['시군구'] == '남구', '시군구':'부상자수']
#print(dfB_290)

dfB_320 = dfB.loc[dfB['시군구'] == '북구', '시군구':'부상자수']
#print(dfB_320)

dfB_350 = dfB.loc[dfB['시군구'] == '해운대구', '시군구':'부상자수']
#print(dfB_350)

dfB_380 = dfB.loc[dfB['시군구'] == '사하구', '시군구':'부상자수']
#print(dfB_380)

dfB_410 = dfB.loc[dfB['시군구'] == '금정구', '시군구':'부상자수']
#print(dfB_410)

dfB_440 = dfB.loc[dfB['시군구'] == '강서구', '시군구':'부상자수']
#print(dfB_440)

dfB_470 = dfB.loc[dfB['시군구'] == '연제구', '시군구':'부상자수']
#print(dfB_470)

dfB_500 = dfB.loc[dfB['시군구'] == '수영구', '시군구':'부상자수']
#print(dfB_500)

dfB_530 = dfB.loc[dfB['시군구'] == '사상구', '시군구':'부상자수']
#print(dfB_530)

dfB_710 = dfB.loc[dfB['시군구'] == '기장군', '시군구':'부상자수']
#print(dfB_710)



#각 구별 사고수...

dfPusan_110sum = dfA_110.loc[:,'발생건수':'부상자수'].sum(axis=0)
#print(dfPusan_110sum)

dfPusan_140sum = dfA_140.loc[:,'발생건수':'부상자수'].sum(axis=0)
#print(dfPusan_110sum)

dfPusan_170sum = dfA_170.loc[:,'발생건수':'부상자수'].sum(axis=0)
#print(dfPusan_170sum)

dfPusan_200sum = dfA_200.loc[:,'발생건수':'부상자수'].sum(axis=0)
#print(dfPusan_200sum)

dfPusan_230sum = dfA_230.loc[:,'발생건수':'부상자수'].sum(axis=0)
#print(dfPusan_230sum)

dfPusan_260sum = dfA_260.loc[:,'발생건수':'부상자수'].sum(axis=0)
#print(dfPusan_260sum)

dfPusan_290sum = dfA_290.loc[:,'발생건수':'부상자수'].sum(axis=0)
#print(dfPusan_290sum)

dfPusan_320sum = dfA_320.loc[:,'발생건수':'부상자수'].sum(axis=0)
#print(dfPusan_320sum)

dfPusan_350sum = dfA_350.loc[:,'발생건수':'부상자수'].sum(axis=0)
#print(dfPusan_350sum)

dfPusan_380sum = dfA_380.loc[:,'발생건수':'부상자수'].sum(axis=0)
#print(dfPusan_380sum)

dfPusan_410sum = dfA_410.loc[:,'발생건수':'부상자수'].sum(axis=0)
#print(dfPusan_410sum)

dfPusan_440sum = dfA_440.loc[:,'발생건수':'부상자수'].sum(axis=0)
#print(dfPusan_440sum)

dfPusan_470sum = dfA_470.loc[:,'발생건수':'부상자수'].sum(axis=0)
#print(dfPusan_470sum)

dfPusan_500sum = dfA_500.loc[:,'발생건수':'부상자수'].sum(axis=0)
#print(dfPusan_500sum)

dfPusan_530sum = dfA_530.loc[:,'발생건수':'부상자수'].sum(axis=0)
#print(dfPusan_530sum)

dfPusan_710sum = dfA_710.loc[:,'발생건수':'부상자수'].sum(axis=0)
#print(dfPusan_710sum)

dfB_A1 = dfB.loc[dfB['사고유형'] == '횡단중', '시군구':'부상자수'] #각 구별 횧단중 사고
#print(dfB_A1)

dfB_A2 = dfB.loc[dfB['사고유형'] == '차도통행중', '시군구':'부상자수']
#print(dfB_A2)

dfB_A3 = dfB.loc[dfB['사고유형'] == '길가장자리구역통행중', '시군구':'부상자수']
#print(dfB_A3)

dfB_A4 = dfB.loc[dfB['사고유형'] == '보도통행중', '시군구':'부상자수']
#print(dfB_A4)

dfB_B2 = dfB.loc[dfB['사고유형대분류'] == '차대차', '시군구':'부상자수']
#print(dfB_B3)

dfB_B3 = dfB.loc[dfB['사고유형대분류'] == '차량단독', '시군구':'부상자수']
#print(dfB_B3)

dfB_B1 = dfB.loc[dfB['사고유형대분류'] == '차대사람', '시군구':'부상자수']
#print(dfB_B1)


#4 앞의 1~3과정의 결과로 인해 생긴 dataFrame 설명

'''
md_1     - df_1 부산시 구군별 사고다발지역
md_110_1 - df_110_1 중구(구군코드110) 사고다발지역
 .
 .
 .
md_710_1 - df_710_1 기장군(구군코드710) 사고다발지역



md_2     - df_2 부산시 구군별 무단횡단 사고다발지역
md_110_2 - df_110_2 중구(구군코드110) 사고다발지역
 .
 .
 .
md_710_2 - df_710_2 기장군(구군코드710) 사고다발지역



md_3_1  -    df_3_1 부산시 구군별 신호위반 사고다발지역
md_110_3_1 - df_110_3_1 중구(구군코드110) 사고다발지역
 .
 .
 .
md_710_3_1 - df_710_3_1 기장군(구군코드710) 사고다발지역



md_3_2  -    df_3_2 부산시 구군별 중앙선침범 사고다발지역
md_110_3_2 - df_110_3_2 중구(구군코드110) 사고다발지역
 .
 .
 .
md_710_3_2 - df_710_3_2 기장군(구군코드710) 사고다발지역



mdAB - dfPusan 부산시 교통사고 발생현황

     - dfA     부산시 도로형태별 교통사고
     - dfA_110 중구(구군코드110) 교통사고
     -  .
     -  .
     -  .
     - dfA_710 기장군(구군코드710)교통사고
     
     - dfB     부산시 사고유형별 교통사고
     - dfB_110 중구(구군코드110) 교통사고
     -  .
     -  .
     -  .
     - dfB_710 기장군(구군코드710) 교통사고

     - dfPusan_110sum 중구(구군코드110) 교통사고 발생현황
     -  .
     -  .
     - .
     - dfPusan_710sum 기장군(구군코드710) 교통사고 발생현황

     - dfB_A1 부산시 횡단중 교통사고 발생현황
     - dfB_A2 부산시 차도통행중 교통사고 발생현황
     - dfB_A3 부산시 길가장자리구역통행중 교통사고 발생현황
     - dfB_A4 부산시 보도통행중 교통사고 발생현황

     - dfB_B1 부산시 차대사람 교통사고 발생현황
     - dfB_B2 부산시 차대차 교통사고 발생현황
     - dfB_B3 부산시 차량단독 교통사고 발생현황



oapidata - import를 통해 df_1 df_2 df_3 가져올 수 있음.
                        (필요없는 Unnamed 행을 제거한)
'''



#5 시각화 1
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pylab as plt
import matplotlib.font_manager as fm
fm.get_fontconfig_fonts()
font_location = 'C:/Windows/Fonts/malgun.ttf'
font_name = fm.FontProperties(fname=font_location).get_name()
mpl.rc('font', family=font_name)

import oapidata
import mdAB

a1,a2,a3,a4 = mdAB.dfPusan_110sum['발생건수'],mdAB.dfPusan_140sum['발생건수'],mdAB.dfPusan_170sum['발생건수'],mdAB.dfPusan_200sum['발생건수']
a5,a6,a7,a8 = mdAB.dfPusan_230sum['발생건수'],mdAB.dfPusan_260sum['발생건수'],mdAB.dfPusan_290sum['발생건수'],mdAB.dfPusan_320sum['발생건수']
a9,a10,a11,a12 = mdAB.dfPusan_350sum['발생건수'],mdAB.dfPusan_380sum['발생건수'],mdAB.dfPusan_410sum['발생건수'],mdAB.dfPusan_440sum['발생건수']
a13,a14,a15,a16 = mdAB.dfPusan_470sum['발생건수'],mdAB.dfPusan_500sum['발생건수'],mdAB.dfPusan_530sum['발생건수'],mdAB.dfPusan_710sum['발생건수']

mdAB.dfPusan_110sum['부상자p'] = mdAB.dfPusan_110sum['부상자수']/mdAB.dfPusan_110sum['발생건수']

mdAB.dfPusan_140sum['부상자p'] = mdAB.dfPusan_140sum['부상자수']/mdAB.dfPusan_140sum['발생건수']

mdAB.dfPusan_170sum['부상자p'] = mdAB.dfPusan_170sum['부상자수']/mdAB.dfPusan_170sum['발생건수']

mdAB.dfPusan_200sum['부상자p'] = mdAB.dfPusan_200sum['부상자수']/mdAB.dfPusan_200sum['발생건수']

mdAB.dfPusan_230sum['부상자p'] = mdAB.dfPusan_230sum['부상자수']/mdAB.dfPusan_230sum['발생건수']

mdAB.dfPusan_260sum['부상자p'] = mdAB.dfPusan_260sum['부상자수']/mdAB.dfPusan_260sum['발생건수']

mdAB.dfPusan_290sum['부상자p'] = mdAB.dfPusan_290sum['부상자수']/mdAB.dfPusan_290sum['발생건수']

mdAB.dfPusan_320sum['부상자p'] = mdAB.dfPusan_320sum['부상자수']/mdAB.dfPusan_320sum['발생건수']

mdAB.dfPusan_350sum['부상자p'] = mdAB.dfPusan_350sum['부상자수']/mdAB.dfPusan_350sum['발생건수']

mdAB.dfPusan_380sum['부상자p'] = mdAB.dfPusan_380sum['부상자수']/mdAB.dfPusan_380sum['발생건수']

mdAB.dfPusan_410sum['부상자p'] = mdAB.dfPusan_410sum['부상자수']/mdAB.dfPusan_410sum['발생건수']

mdAB.dfPusan_440sum['부상자p'] = mdAB.dfPusan_440sum['부상자수']/mdAB.dfPusan_440sum['발생건수']

mdAB.dfPusan_470sum['부상자p'] = mdAB.dfPusan_470sum['부상자수']/mdAB.dfPusan_470sum['발생건수']

mdAB.dfPusan_500sum['부상자p'] = mdAB.dfPusan_500sum['부상자수']/mdAB.dfPusan_500sum['발생건수']

mdAB.dfPusan_530sum['부상자p'] = mdAB.dfPusan_530sum['부상자수']/mdAB.dfPusan_530sum['발생건수']

mdAB.dfPusan_710sum['부상자p'] = mdAB.dfPusan_710sum['부상자수']/mdAB.dfPusan_710sum['발생건수']

plt.figure()
plt.subplot(1,2,1)
plt.plot(mdAB.dfPusan_110sum['부상자p'],'o',label ='중구')
plt.plot(mdAB.dfPusan_140sum['부상자p'],'o',label ='서구')
plt.plot(mdAB.dfPusan_170sum['부상자p'],'o',label ='동구')
plt.plot(mdAB.dfPusan_200sum['부상자p'],'o',label ='영도구')
plt.plot(mdAB.dfPusan_230sum['부상자p'],'o',label ='부산진구')
plt.plot(mdAB.dfPusan_260sum['부상자p'],'o',label ='동래구')
plt.plot(mdAB.dfPusan_290sum['부상자p'],'o',label ='남구')
plt.plot(mdAB.dfPusan_320sum['부상자p'],'o',label ='북구')
plt.plot(mdAB.dfPusan_350sum['부상자p'],'o',label ='해운대구')
plt.plot(mdAB.dfPusan_380sum['부상자p'],'o',label ='사하구')
plt.plot(mdAB.dfPusan_410sum['부상자p'],'o',label ='금정구')
plt.plot(mdAB.dfPusan_440sum['부상자p'],'o',label ='강서구')
plt.plot(mdAB.dfPusan_470sum['부상자p'],'o',label ='연제구')
plt.plot(mdAB.dfPusan_500sum['부상자p'],'o',label ='수영구')
plt.plot(mdAB.dfPusan_530sum['부상자p'],'o',label ='사상구')
plt.plot(mdAB.dfPusan_710sum['부상자p'],'o',label ='기장군')
plt.xlabel('구군')
plt.legend(loc='upper right',fontsize='xx-small')
plt.title('구군의 사고발생수와 부상자 비')

plt.subplot(1,2,2)
plt.plot(a1,'o',label ='중구')
plt.plot(a2,'o',label ='서구')
plt.plot(a3,'o',label ='동구')
plt.plot(a4,'o',label ='영도구')
plt.plot(a5,'o',label ='부산진구')
plt.plot(a6,'o',label ='동래구')
plt.plot(a7,'o',label ='남구')
plt.plot(a8,'o',label ='북구')
plt.plot(a9,'o',label ='해운대구')
plt.plot(a10,'o',label ='사하구')
plt.plot(a11,'o',label ='금정구')
plt.plot(a12,'o',label ='강서구')
plt.plot(a13,'o',label ='연제구')
plt.plot(a14,'o',label ='수영구')
plt.plot(a15,'o',label ='사상구')
plt.plot(a16,'o',label ='기장군')
plt.xlabel('구군')
plt.legend(loc='upper right',fontsize='xx-small')
plt.title('구군의 사고발생수')

plt.show()

#동래 해운대구 강서구의 사고가 상대적으로 심각함을 알 수 있다.
#부산진구,해운대구, 사하구의 사고가 상대적으로 많음을 알 수 있다.



#6 시각화 2
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pylab as plt
import matplotlib.font_manager as fm
fm.get_fontconfig_fonts()
font_location = 'C:/Windows/Fonts/malgun.ttf'                 ##한글 사용을 위함
font_name = fm.FontProperties(fname=font_location).get_name()
mpl.rc('font', family=font_name)

import oapidata
import mdAB

oapidata.df_1['부상자p'] = oapidata.df_1['부상자수']/oapidata.df_1['발생건수']
mdAB.dfPusan['부상자p'] = mdAB.dfPusan['부상자 수']/mdAB.dfPusan['발생건수']

#n_df_1 = pd.DataFrame([i for i in oapidata.df_1['부상자p']], index = [i for i in oapidata.df_1['다발지역명']])

print(oapidata.df_1[['다발지역명','부상자p']])

index = []
index0 = []
for i in oapidata.df_1['시군구']:
    index.append(i)
    index0.append(i)
cnt=0
num = -1
index0.append('0')
index_1 = []
for i in index:
    num = num + 1
    if cnt == 0:
        index_1.append(i+str(cnt))
        cnt = cnt + 1
        if i != index0[num+1]:
            cnt = 0
    elif cnt != 0:
        index_1.append(i+str(cnt))
        cnt = cnt +1
        if i != index0[num+1]:
            cnt = 0
#print(index_1)

plt.figure()
plt.bar(index_1,oapidata.df_1['부상자p'],label='사고다발지역', color = 'r')
plt.plot([mdAB.dfPusan['부상자p'] for i in index_1],label = '부산시 평균')
plt.legend(loc='upper right')
plt.title('사고다발지역의 [부상자/발생건수]')
plt.xticks(rotation=90)
plt.show()


#   강서구1 = 강서구 명지동(명지IC 인근)
#     서구0 = 서구 암남동(충무교차로 인근)
#해운대구 1 = 해운대구 우동(올림픽교차로 인근)
#위의 세 다발지역이 상대적으로 매우 높은 수준의 인명피해를 내고있는 곳임을
#확연하게 볼 수있다.



#7 시각화 3
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pylab as plt
import matplotlib.font_manager as fm
fm.get_fontconfig_fonts()
font_location = 'C:/Windows/Fonts/malgun.ttf'                 ##한글 사용을 위함
font_name = fm.FontProperties(fname=font_location).get_name()
mpl.rc('font', family=font_name)

import oapidata
import mdAB

x = mdAB.dfB_A1.sum(axis=0)['부상자수']/mdAB.dfB_A1.sum(axis=0)['발생건수']  #횡단중 사고 부상자수/발생건수

oapidata.df_2['부상자p'] = oapidata.df_2['부상자수']/oapidata.df_2['발생건수']
print(oapidata.df_2[['다발지역명','부상자p']])

index = []
index0 = []
for i in oapidata.df_2['시군구']:
    index.append(i)
    index0.append(i)
cnt=0
num = -1
index0.append('0')
index_1 = []
for i in index:
    num = num + 1
    if cnt == 0:
        index_1.append(i+str(cnt))
        cnt = cnt + 1
        if i != index0[num+1]:
            cnt = 0
    elif cnt != 0:
        index_1.append(i+str(cnt))
        cnt = cnt +1
        if i != index0[num+1]:
            cnt = 0
#print(index_1)

plt.figure()
plt.bar(index_1,oapidata.df_2['부상자p'],label='다발지역', color = 'y')
plt.plot([x for i in index_1],label = '부산시 평균')
plt.legend(loc='upper right')
plt.title('무단횡단사고 다발지역의 [부상자/발생건수]')
plt.xticks(rotation=90)
plt.show()

#서구0 = 서구 충무동1가(충무동사거리 부근)
#진구0 = 부산진구 부전동(메가박스 서면점 부근)
#동래1 = 동래구 온천동(부산온천3동우체국 부근)
#금정0 = 금정구 서동(부산은행 금사공단지점 부근)
#위의 네 다발지역이 상대적으로 매우 높은 수준의 인명피해를 내고있는 곳임을
#확연하게 볼 수 있다.



#8 시각화 4
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pylab as plt
import matplotlib.font_manager as fm
fm.get_fontconfig_fonts()
font_location = 'C:/Windows/Fonts/malgun.ttf'                 ##한글 사용을 위함
font_name = fm.FontProperties(fname=font_location).get_name()
mpl.rc('font', family=font_name)

import oapidata
import mdAB

x = oapidata.df_3_1.sum(axis=0)['부상자수']/oapidata.df_3_1.sum(axis=0)['발생건수'] #신호위반사고 부상자수/발생건수
#print(x)
y = oapidata.df_3_2.sum(axis=0)['부상자수']/oapidata.df_3_2.sum(axis=0)['발생건수'] #중앙선침범사고 부상자수/발생건수
#print(y)

oapidata.df_3_1['부상자p'] = oapidata.df_3_1['부상자수']/oapidata.df_3_1['발생건수']
#print(oapidata.df_3_1[['다발지역명','부상자p']])

oapidata.df_3_2['부상자p'] = oapidata.df_3_2['부상자수']/oapidata.df_3_2['발생건수']
#print(oapidata.df_3_2[['다발지역명','부상자p']])

index_1 = []
index0_1 = []
for i in oapidata.df_3_1['시군구']:
    index_1.append(i)
    index0_1.append(i)
cnt=0
num = -1
index0_1.append('0')
index_1_1 = []
for i in index_1:
    num = num + 1
    if cnt == 0:
        index_1_1.append(i+str(cnt))
        cnt = cnt + 1
        if i != index0_1[num+1]:
            cnt = 0
    elif cnt != 0:
        index_1_1.append(i+str(cnt))
        cnt = cnt +1
        if i != index0_1[num+1]:
            cnt = 0
#print(index_1_1)

index_2 = []
index0_2 = []
for i in oapidata.df_3_2['시군구']:
    index_2.append(i)
    index0_2.append(i)
cnt=0
num = -1
index0_2.append('0')
index_1_2 = []
for i in index_2:
    num = num + 1
    if cnt == 0:
        index_1_2.append(i+str(cnt))
        cnt = cnt + 1
        if i != index0_2[num+1]:
            cnt = 0
    elif cnt != 0:
        index_1_2.append(i+str(cnt))
        cnt = cnt +1
        if i != index0_2[num+1]:
            cnt = 0
#print(index_1_2)

print(oapidata.df_3_1[['다발지역명','부상자p']])
print(oapidata.df_3_2[['다발지역명','부상자p']])

plt.figure()

plt.subplot(2,1,1)
plt.bar(index_1_1,oapidata.df_3_1['부상자p'],label='신호위반 사고다발지역', color = 'g')
plt.plot([x for i in index_1_1],label = '부산시 평균')
plt.legend(loc='upper right')
plt.xticks(rotation=90)
plt.title('부상자 수/발생건 수')

plt.subplot(2,1,2)
plt.bar(index_1_2,oapidata.df_3_2['부상자p'],label='중앙선침범 사고다발지역', color = 'y')
plt.plot([y for i in index_1_2],label = '부산시 평균')
plt.legend(loc='upper right')
plt.xticks(rotation=90)
plt.show()

#    서구0 = 서구 충무동1가(충무교차로 부근)
#    진구2 = 부산진구 부암동(진양삼거리 부근)
#해운대구0 = 해운대구 재송동(재송삼익아파트 부근)
#  수영구1 = 수영구 수영동(감포사거리 부근)
#  사상구0 = 사상구 감전동(학감사거리 부근)
#다섯 곳의 신호위반 사고다발지역이 상대적으로 매우 높은 수준의 인명피해를 내고있는 곳임을
#확연하게 볼 수 있다.

#  서구0 = 서구 서대신동1가(오토맨션 부근)
#영도구0 = 영도구 봉래동1가(부산대교남측 부근)
#금정구0 = 금정구 구서동(남산동훼미리주유소 부근)
#세 곳의 중앙선침범 사고다발지역이 상대적으로 매우 높은 수준의 인명피해를 내굈는 곳임을
#확연하게 볼 수 있다.
