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
#부산진구,해운대구, 사하구의 사고가 상대적으로 많으믈 알 수 있다.
