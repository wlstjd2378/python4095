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