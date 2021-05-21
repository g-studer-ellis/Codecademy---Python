import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# load rankings data here:
wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
print(wood.head())
print(wood.info())

steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
print(steel.head())
print(steel.info())

# write function to plot rankings over time for 1 roller coaster here:
def ranking_over_time(df, c_name, c_park):
  coaster_ranking = df[(df['Name'] == c_name) & (df['Park'] == c_park)]
  sns.lineplot(data = coaster_ranking, x = 'Year of Rank', y = 'Rank')
  plt.show()
  plt.clf()
  return coaster_ranking

el_toro = ranking_over_time(wood, 'El Toro', 'Six Flags Great Adventure')

plt.clf()

# write function to plot rankings over time for 2 roller coasters here:

def plot_2_coaster_rankings(name_1, park_1, name_2, park_2, df):
  ranking_1 = df[(df['Name'] == name_1) & (df['Park'] == park_1)]
  ranking_2 = df[(df['Name'] == name_2) & (df['Park'] == park_2)]
  fig, ax = plt.subplots()
  ax.plot(ranking_1['Year of Rank'], ranking_1['Rank'], color = 'green', label = name_1)
  ax.plot(ranking_2['Year of Rank'], ranking_2['Rank'], color = 'red', label = name_2)
  ax.invert_yaxis()
  plt.title("{} vs {} Rankings".format(name_1,name_2))
  plt.xlabel('Year')
  plt.ylabel('Ranking')
  plt.legend()
  plt.show()

plot_2_coaster_rankings('El Toro','Six Flags Great Adventure','Boulder Dash','Lake Compounce',wood)

plt.clf()

# write function to plot top n rankings over time here:
def plot_n_coasters(df, n):
  top_n = df[df['Rank'] <= n]
  fig, ax = plt.subplots()
  for coaster in set(top_n['Name']):
    ranking = top_n[top_n['Name'] == coaster]
    ax.plot(ranking['Year of Rank'], ranking['Rank'], label = coaster)
  ax.invert_yaxis()
  plt.title("Top " + str(n) + " Roller Coaster Rankings")
  plt.xlabel('Year')
  plt.ylabel('Ranking')
  plt.legend(loc=4)
  plt.show()
  plt.clf()

plot_n_coasters(wood, 5)

# load roller coaster data here:
coasters = pd.read_csv('roller_coasters.csv')
print(coasters.head())
print(coasters.info())

# write function to plot histogram of column values here:
def make_histogram(df, column):
  sns.histplot(data = df, x = column)
  plt.show()
  plt.clf()

make_histogram(coasters, 'speed')

make_histogram(coasters, 'length')

make_histogram(coasters, 'num_inversions')

make_histogram(coasters, 'height')

# write function to plot inversions by coaster at a park here:
def inversion_bar_plot_by_park(df, park):
  p_coasters = df[df['park'] == park]
  p_coasters = p_coasters.sort_values('num_inversions', ascending = False)
  sns.barplot(data = p_coasters, x = 'name', y = 'num_inversions')
  plt.xlabel('Roller Coasters')
  plt.ylabel('Number of Inversions')
  plt.title('How many inversions does each roller coaster have at ' + str(park) + '?')
  plt.xticks(rotation = 45)
  plt.show()
  plt.clf()

inversion_bar_plot_by_park(coasters, 'Dollywood')

# write function to plot pie chart of operating status here:
def status_pie(df):
  operating = df[df['status'] == 'status.operating']
  closed = df[df['status'] == 'status.closed']
  status_counts = [len(operating), len(closed)]
  plt.pie(status_counts, autopct = '%0.1f%%', labels = ['Operating', 'Closed'])
  plt.axis('equal')
  plt.show()
  plt.clf()

status_pie(coasters)

# write function to create scatter plot of any two numeric columns here:
def scatter_comp(df, column1, column2):
  sns.scatterplot(data = df, x = column1, y = column2)
  plt.show()
  plt.clf()

scatter_comp(coasters, 'speed', 'height')
