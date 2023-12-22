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

def ratioger_bel():
    sample = ['germany', 'belgium']

    plt.figure(figsize=(15, 6))
    for pays in sample:
        data_selected = cata[(cata['Country'] == pays) & (cata['Year'].between(1990, 2022))]
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

