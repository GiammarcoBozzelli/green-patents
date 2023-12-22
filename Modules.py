import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import scipy.stats as stats
from IPython.display import display
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from linearmodels.panel import PanelOLS
from stargazer.stargazer import Stargazer
import pycountry
from IPython.display import Image, display,HTML

def plot_1(df):
  avg_patents_by_year = df.groupby('Year')['patents_number'].mean().reset_index().dropna()
  avg_damage_by_year = df.groupby('Year')['total_affected'].mean().reset_index().dropna()
  plt.figure(figsize=(10, 6))
  plt.plot(avg_patents_by_year['Year'], np.log(avg_patents_by_year['patents_number']), linestyle='-', color='b', label='Yearly average number of patents')
  plt.plot(avg_damage_by_year['Year'], np.log(avg_damage_by_year['total_affected']), linestyle='-', color='r', label='Yearly Average number of people affected')

  plt.title('Average Patents Number and Average Number of Pople Affected Over Time')
  plt.xlabel('Year')
  plt.ylabel('log(Yearly Average)')
  plt.legend()
  plt.grid(True)
  plt.show()

def graphe(): # plot graph to illustrate the Dif-in-dif theoretical model
    x1 = np.linspace(0, 10, 100)
    y1 = 1.5 * x1 + 4

    x2 = np.linspace(0, 10, 100)
    y2 = x2 + 4

    x3 = np.linspace(0, 10, 100)
    y3 = x3 + 2

    plt.figure(figsize=(8, 6))
    plt.plot(x1, y1, color='orange', label='Treated group')
    plt.plot(x2, y2, linestyle='--', color='orange', label='Hypothetical treated group without treatment')
    plt.plot(x3, y3, color='green', label='Control group')

    plt.text(x1[0], y1[0], 'c', fontsize=12, color='black', ha='right', va='bottom')
    plt.text(x1[-1], y1[-1], 'd', fontsize=12, color='black', ha='right', va='bottom')

    plt.text(x2[0], y2[0], '', fontsize=12, color='black', ha='right', va='bottom')
    plt.text(x2[-1], y2[-1], "d'", fontsize=12, color='black', ha='right', va='bottom')

    plt.text(x3[0], y3[0], 'a', fontsize=12, color='black', ha='right', va='bottom')
    plt.text(x3[-1], y3[-1], 'b', fontsize=12, color='black', ha='right', va='bottom')

    plt.title('DID theoretical model')
    plt.xlabel('Time')
    plt.ylabel('Outcome')
    plt.legend()

    return plt.show()


def ratioger_bel():

    df = pd.read_csv('https://raw.githubusercontent.com/GiammarcoBozzelli/green-patents/main/data/cata.csv')
  
    sample = ['germany', 'belgium']

    plt.figure(figsize=(15, 6))
    for pays in sample:
        data_selected = df[(df['Country'] == pays) & (df['Year'].between(1990, 2022))]
        catastrophes_per_year = data_selected['Year'].value_counts().sort_index()
        damage_per_year = data_selected.groupby('Year')["Total Affected"].sum().fillna(0)

        ratio = damage_per_year / catastrophes_per_year

        if pays == 'germany':
            plt.plot(ratio.index, ratio.values, marker='o', linestyle='-', label=pays, color='red')
        elif pays == 'belgium':
            plt.plot(ratio.index, ratio.values, marker='o', linestyle='-', label=pays, color='blue')

    plt.xlabel('Year')
    plt.ylabel('Total Affected per Catastrophe')
    plt.title('Ratio of Total Affected per Catastrophe for Selected Countries between 1990 and 2021')
    plt.legend()
    plt.grid(True)
    plt.show()

def difdifger_bel():
  plt.figure(figsize=(10, 6))

  ger_bel = pd.read_csv('https://github.com/GiammarcoBozzelli/green-patents/raw/main/data/ger_bel.csv')

  germany_data = ger_bel[ger_bel['is Germany'] == 1]
  
  model_germany = sm.OLS(germany_data['Patent per Capita'],
                        sm.add_constant(germany_data[['after chock', 'After Chock Gemrany']]))

  results_germany = model_germany.fit()

  predictions_germany = results_germany.predict()


  belgium_data = ger_bel[ger_bel['is Germany'] == 0]

  model_belgium = sm.OLS(belgium_data['Patent per Capita'],
                          sm.add_constant(belgium_data[['after chock', 'After Chock Gemrany']]))

  results_belgium = model_belgium.fit()

  predictions_belgium = results_belgium.predict()


#Sort data from 1990 to 2021

  germany_data_filtered = germany_data[(germany_data['Year'] >= 1990) & (germany_data['Year'] <= 2021)]
  predictions_germany_filtered = predictions_germany[(germany_data['Year'] >= 1990) & (germany_data['Year'] <= 2021)]

  belgium_data_filtered = belgium_data[(belgium_data['Year'] >= 1990) & (belgium_data['Year'] <= 2021)]
  predictions_belgium_filtered = predictions_belgium[(belgium_data['Year'] >= 1990) & (belgium_data['Year'] <= 2021)]

#regression for germany
  plt.scatter(germany_data_filtered['Year'], germany_data_filtered['Patent per Capita'], label='Patent per Capita - Germany', color='red')
  plt.plot(germany_data_filtered['Year'], predictions_germany_filtered, label='Linear Regression - Germany', color='salmon')

#regression for austria
  plt.scatter(belgium_data_filtered['Year'], belgium_data_filtered['Patent per Capita'], label='Patent per Capita - Belgium', color='blue')
  plt.plot(belgium_data_filtered['Year'], predictions_belgium_filtered, label='Linear Regression - Belgium', color='lightblue')

#shift line
  plt.axvline(x=2002, color='green', linestyle='--', label='Boundary Before/After')

  plt.xlabel('Year')
  plt.ylabel('Patent per Capita')
  plt.title('Linear Regression for Germany and Belgium between 1990 and 2021 with Before/After Boundary')
  plt.legend()
  plt.grid(True)
  plt.show()


def ratiotha_mal():
  cata = pd.read_csv('https://raw.githubusercontent.com/GiammarcoBozzelli/green-patents/main/data/cata.csv')
  
  sample = ['thailand', 'malaysia']
  
  plt.figure(figsize=(15, 6))
  for pays in sample:
    data_selected = cata[(cata['Country'] == pays) & (cata['Year'].between(1995, 2022))]
    catastrophes_per_year = data_selected['Year'].value_counts().sort_index()
    damage_per_year = data_selected.groupby('Year')["Total Affected"].sum().fillna(0)

    ratio = damage_per_year / catastrophes_per_year

    if pays == 'malaysia':
            plt.plot(ratio.index, ratio.values, marker='o', linestyle='-', label=pays, color='purple')
    elif pays == 'thailand':
            plt.plot(ratio.index, ratio.values, marker='o', linestyle='-', label=pays, color='orange')

  #plt.plot(ratio.index, ratio.values, marker='o', linestyle='-', label=pays)

  plt.xlabel('Year')
  plt.ylabel('Total Damage per Catastrophe')
  plt.title('Ratio of Total Damage per Catastrophe for Selected Countries between 1980 and 2021')
  plt.legend()
  plt.grid(True)
  plt.show()

def difdiftha_mal():

  tha_mal = pd.read_csv('https://github.com/GiammarcoBozzelli/green-patents/raw/main/data/tha_mal.csv')

  tha_mal['After Chock Thailand'] = tha_mal['is Thailand'] * tha_mal['After Chock']

  thailand_data = tha_mal[tha_mal['is Thailand'] == 1]

  model_thailand = sm.OLS(thailand_data['Patent per Capita'],
                          sm.add_constant(thailand_data[['After Chock', 'After Chock Thailand']]))

  results_thailand = model_thailand.fit()

  predictions_thailand = results_thailand.predict()

  malaysia_data = tha_mal[tha_mal['is Thailand'] == 0]

  model_malaysia = sm.OLS(malaysia_data['Patent per Capita'],
                          sm.add_constant(malaysia_data[['After Chock', 'After Chock Thailand']]))

  results_malaysia = model_malaysia.fit()

  predictions_malaysia = results_malaysia.predict()

  plt.figure(figsize=(10, 6))

#Sort data from 1990 to 2021
  thailand_data_filtered = thailand_data[(thailand_data['Year'] >= 1995) & (thailand_data['Year'] <= 2021)]
  predictions_thailand_filtered = predictions_thailand[(thailand_data['Year'] >= 1995) & (thailand_data['Year'] <= 2021)]

  malaysia_data_filtered = malaysia_data[(malaysia_data['Year'] >= 1995) & (malaysia_data['Year'] <= 2021)]
  predictions_malaysia_filtered = predictions_malaysia[(malaysia_data['Year'] >= 1995) & (malaysia_data['Year'] <= 2021)]

#regression for Brazil
  plt.scatter(thailand_data_filtered['Year'], thailand_data_filtered['Patent per Capita'], label='Patent per Capita - Thailand', color='orange')
  plt.plot(thailand_data_filtered['Year'], predictions_thailand_filtered, label='Linear Regression - Thailand', color='orange')

#regression for germany
  plt.scatter(malaysia_data_filtered['Year'], malaysia_data_filtered['Patent per Capita'], label='Patent per Capita - Malaysia', color='purple')
  plt.plot(malaysia_data_filtered['Year'], predictions_malaysia_filtered, label='Linear Regression - Malaysia', color='purple')

#shift line
  plt.axvline(x=2010, color='green', linestyle='--', label='Boundary Before/After')

  plt.xlabel('Year')
  plt.ylabel('Patent per Capita')
  plt.title('Linear Regression for Thailand and Malaysia between 1995 and 2021 with Before/After Boundary')
  plt.legend()
  plt.grid(True)
  plt.show()
