import requests
from bs4 import BeautifulSoup
import pandas as pd

import md_110_3_2
import md_140_3_2
import md_170_3_2
import md_200_3_2
import md_230_3_2
import md_260_3_2
import md_290_3_2
import md_320_3_2
import md_350_3_2
import md_380_3_2
import md_410_3_2
import md_440_3_2
import md_470_3_2
import md_500_3_2
import md_530_3_2
import md_710_3_2

df_3_2 = pd.concat([md_110_3_2.df_110_3_2,md_140_3_2.df_140_3_2,md_170_3_2.df_170_3_2,\
md_200_3_2.df_200_3_2,md_230_3_2.df_230_3_2,md_260_3_2.df_260_3_2,md_290_3_2.df_290_3_2,\
md_320_3_2.df_320_3_2,md_350_3_2.df_350_3_2,md_380_3_2.df_380_3_2,md_410_3_2.df_410_3_2,\
md_440_3_2.df_440_3_2,md_470_3_2.df_470_3_2,md_500_3_2.df_500_3_2,md_530_3_2.df_530_3_2,\
md_710_3_2.df_710_3_2])         # 행렬 합치기

df_3_2 = df_3_2.reset_index(drop=True) #인덱스 초기화
#print(df_3_2)
df_3_2.to_csv('centerlineinvade_accident_region_frequent.csv', mode = 'w')

