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

