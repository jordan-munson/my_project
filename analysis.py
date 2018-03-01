# -*- coding: utf-8 -*-
"""
Spyder Editor

Software Carpentry Workshop
"""
#Import dealios
import pandas as pd
import matplotlib.pyplot as plt


#Read data files
gdp_europe = pd.read_csv('data/gapminder_gdp_europe.csv', index_col = 'country')
gdp_oceania = pd.read_csv('data/gapminder_gdp_oceania.csv', index_col = 'country')
gdp_asia = pd.read_csv('data/gapminder_gdp_asia.csv', index_col = 'country')
gdp_africa = pd.read_csv('data/gapminder_gdp_africa.csv', index_col = 'country')
gdp_all = pd.read_csv('data/gapminder_all.csv', index_col = 'country')

plt.plot(gdp_europe)
plt.show()
