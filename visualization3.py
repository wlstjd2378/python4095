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
