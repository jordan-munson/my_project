# -*- coding: utf-8 -*-
"""
Spyder Editor

Software Carpentry Workshop
"""
#Import dealios
import pandas as pd
import matplotlib.pyplot as plt


#Read data files
gdp_europe = pd.read_csv('data/gapminder_gdp_europe.csv')
gdp_oceania = pd.read_csv('data/gapminder_gdp_oceania.csv')
gdp_asia = pd.read_csv('data/gapminder_gdp_asia.csv')
gdp_africa = pd.read_csv('data/gapminder_gdp_africa.csv')
gdp_all = pd.read_csv('data/gapminder_all.csv')

plt.plot(gdp_europe)
plt.show()
