# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]



# MY WORK BELOW

# 1
# Update Recorded Damages
# Create a function which returns a new list of updated damages
# The new list will have data converted to floats as full numbers (1M = 1000000)
# The new list will keep the strings "Damages not recorded"
# Make use of the conversion dictionary below
conversion = {"M": 1000000,
              "B": 1000000000}

def convert_damages(lst):
  new_damages = []
  for i in lst:
    if 'M' in i:
      stripped = float(i.strip('M'))
      calculate = float(stripped * conversion['M'])
      new_damages.append(calculate)      
    elif 'B' in i:
      stripped_b = float(i.strip('B'))
      calculate_b = stripped_b * conversion['B']
      new_damages.append(calculate_b)
    else:
      new_damages.append(i)
  return new_damages

# test function by updating damages
new_damages = convert_damages(damages)
#print(new_damages)
print("Completed task 1!")


# 2 
# Create a Table
# Create a list of lists that will be in the dictionary
# Define a function which will make a dictionary from the list of lists with the first list as the dictionary keys
def create_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  my_dict = {}
  for i in range(len(names)):
    my_dict[names[i]] = {'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Damage': damages[i], 'Death': deaths[i]}
  return my_dict

# Create and view the hurricanes dictionary
hurricanes_dict = create_dict(names, months, years, max_sustained_winds, areas_affected, new_damages, deaths)
#print(hurricanes_dict)
#print(hurricanes_dict['Cuba I'])
print('Completed task 2!')


# 3
# Organizing by Year
# Define a fuction that takes the infro from the hurricanes_dict
# and outputs a new dictionary which uses years as keys instead of names
# The dictionary will hold the same information as hurricanes_dict
# just organized differently
def years_from_storms(hurricanes):
  hur_by_year = {}
  for i in hurricanes:
    year = hurricanes[i]["Year"]
    name = hurricanes[i]
    if year not in hur_by_year:
      hur_by_year[year] = [name]
    else:
      hur_by_year[year].append(name)
  return hur_by_year

# create a new dictionary of hurricanes with year and key
years_of_storms = years_from_storms(hurricanes_dict)
#print(years_of_storms[1932])
print("Completed task 3!")


# 4
# Counting Damaged Areas
# Define a function that creates a dictionary
# which holds areas affected as keys
# and values of the number of times those areas were affected
def counting_areas(hurricanes):
  count_affected = {}
  for value in hurricanes.values():
    for i in value["Areas Affected"]:
      if i not in count_affected:
        count_affected[i] = 1
      else:
        count_affected[i] += 1
  return count_affected

# create dictionary of areas to store the number of hurricanes involved in
areas_affected = counting_areas(hurricanes_dict)
#print(areas_affected)
print('Completed task 4!')


# 5 
# Calculating Maximum Hurricane Count
# Define a function which outputs the area most affected by hurricanes
def most_affected(areas_affected):
  max_area = {}
  max_area_count = 7
  for i, n in areas_affected.items():
    if n > max_area_count:
      max_area[i] = n
      max_area_count = n
  return max_area

# find most frequently affected area and the number of hurricanes involved in
# check the most_affected function
most_affected_area = most_affected(areas_affected)
#print(most_affected_area)
print('Completed task 5!')


# 6
# Calculating the Deadliest Hurricane
def deadliest(hurricanes_dict):
  deadliest = ''
  death_count = 0
  for i in hurricanes_dict:
    if hurricanes_dict[i]['Death'] > death_count:
      deadliest = i
      death_count = hurricanes_dict[i]['Death']
  return deadliest, death_count

# find highest mortality hurricane and the number of deaths
deadliest_storm = deadliest(hurricanes_dict)
#print(deadliest_storm)
print('Completed task 6!')

# 7
# Rating Hurricanes by Mortality
# Define a scale for rating how deadly hurricanes are
# Define a function that rates hurrices according to said scale
mortality_scale_settings = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
def mortality_scale(hurricanes):
  m_scale = {}
  zero_list = []
  one_list = []
  two_list = []
  three_list = []
  four_list = []
  for k, v in hurricanes.items():
    if hurricanes[k]["Death"] == 0:
     zero_list.append(v)
     m_scale[0] = zero_list
    elif hurricanes[k]["Death"] <= 100:
     one_list.append(v)
     m_scale[1] = one_list
    elif hurricanes[k]["Death"] <= 500:
     two_list.append(v)
     m_scale[2] = two_list
    elif hurricanes[k]["Death"] <= 1000:
     three_list.append(v)
     m_scale[3] = three_list
    elif hurricanes[k]["Death"] <= 10000:
     four_list.append(v)
     m_scale[4] = four_list
  return m_scale

# categorize hurricanes in new dictionary with mortality severity as key
mortality = mortality_scale(hurricanes_dict)
#print(mortality)
print('Completed task 7!')


# 8 Calculating Hurricane Maximum Damage
def maximum_damage(hurricanes_dict):
  most_damaging = ''
  damage_cost = float(0)
  for i in hurricanes_dict:
    if hurricanes_dict[i]['Damage'] == 'Damages not recorded':
      pass
    elif hurricanes_dict[i]['Damage'] > damage_cost:
      most_damaging = i
      damage_cost = hurricanes_dict[i]['Damage']
  return most_damaging, damage_cost

# find highest damage inducing hurricane and its total cost
most_damaging = maximum_damage(hurricanes_dict)
#print(most_damaging)
print("Completed task 8!")


# 9
# Rating Hurricanes by Damage
damage_scale_settings = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
def damage_scale(hurricanes):
  d_scale = {}
  zero_list = []
  one_list = []
  two_list = []
  three_list = []
  four_list = []
  for k, v in hurricanes.items():
    if hurricanes[k]['Damage'] == 'Damages not recorded':
      pass
    elif hurricanes[k]["Damage"] == 0:
     zero_list.append(v)
     d_scale[0] = zero_list
    elif hurricanes[k]["Damage"] <= 100000000:
     one_list.append(v)
     d_scale[1] = one_list
    elif hurricanes[k]["Damage"] <= 1000000000:
     two_list.append(v)
     d_scale[2] = two_list
    elif hurricanes[k]["Damage"] <= 10000000000:
     three_list.append(v)
     d_scale[3] = three_list
    elif hurricanes[k]["Damage"] <= 50000000000:
     four_list.append(v)
     d_scale[4] = four_list
  return d_scale

# categorize hurricanes in new dictionary with damage severity as key
most_damaging = damage_scale(hurricanes_dict)
#print(most_damaging)
print('Completed task 9!')