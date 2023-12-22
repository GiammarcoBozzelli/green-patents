import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

def graphe(self): # plot graph to illustrate the Dif-in-dif theoretical model
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

