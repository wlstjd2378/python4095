import requests
from bs4 import BeautifulSoup
import pandas as pd

import md_110_2
import md_140_2
import md_170_2
import md_200_2
import md_230_2
import md_260_2
import md_290_2
import md_320_2
import md_350_2
import md_380_2
import md_410_2
import md_440_2
import md_470_2
import md_500_2
import md_530_2
import md_710_2

df_2 = pd.concat([md_110_2.df_110_2,md_140_2.df_140_2,md_170_2.df_170_2,\
md_200_2.df_200_2,md_230_2.df_230_2,md_260_2.df_260_2,md_290_2.df_290_2,\
md_320_2.df_320_2,md_350_2.df_350_2,md_380_2.df_380_2,md_410_2.df_410_2,\
md_440_2.df_440_2,md_470_2.df_470_2,md_500_2.df_500_2,md_530_2.df_530_2,\
md_710_2.df_710_2])


df_2 = df_2.reset_index(drop=True)
#print(df_2)
df_2.to_csv('freewalker_accident_region_frequent.csv', mode = 'w')
