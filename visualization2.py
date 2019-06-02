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
