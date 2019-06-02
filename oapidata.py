import pandas as pd
import numpy as np


df_1 = pd.read_csv('accident_region_frequent.csv')                  #부산시 사고 다발지역
df_1 = df_1.drop('Unnamed: 0',axis = 1)                                      #열 제거
#print(df_1)

df_2 = pd.read_csv('freewalker_accident_region_frequent.csv')       #부산시 무단횡단사고 다발지역
df_2 = df_2.drop('Unnamed: 0',axis = 1)
#print(df_2)

df_3_1 = pd.read_csv('signalviolation_accident_region_frequent.csv')#부산시 신호위반사고 다발지역
df_3_1 = df_3_1.drop('Unnamed: 0',axis = 1)
#print(df_3_1)

df_3_2 = pd.read_csv('centerlineinvade_accident_region_frequent.csv')#부산시 중앙선침범사고 다발지역
df_3_2 = df_3_2.drop('Unnamed: 0',axis = 1)
#print(df_3_2)


