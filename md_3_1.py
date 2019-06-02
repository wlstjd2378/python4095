import requests
from bs4 import BeautifulSoup
import pandas as pd

import md_110_3_1
import md_140_3_1
import md_170_3_1
import md_200_3_1
import md_230_3_1
import md_260_3_1
import md_290_3_1
import md_320_3_1
import md_350_3_1
import md_380_3_1
import md_410_3_1
import md_440_3_1
import md_470_3_1
import md_500_3_1
import md_530_3_1
import md_710_3_1

df_3_1 = pd.concat([md_110_3_1.df_110_3_1,md_140_3_1.df_140_3_1,md_170_3_1.df_170_3_1,\
md_200_3_1.df_200_3_1,md_230_3_1.df_230_3_1,md_260_3_1.df_260_3_1,md_290_3_1.df_290_3_1,\
md_320_3_1.df_320_3_1,md_350_3_1.df_350_3_1,md_380_3_1.df_380_3_1,md_410_3_1.df_410_3_1,\
md_440_3_1.df_440_3_1,md_470_3_1.df_470_3_1,md_500_3_1.df_500_3_1,md_530_3_1.df_530_3_1,\
md_710_3_1.df_710_3_1])

df_3_1 = df_3_1.reset_index(drop=True)
#print(df_3_1)
df_3_1.to_csv('signalviolation_accident_region_frequent.csv', mode = 'w')
