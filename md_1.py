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









