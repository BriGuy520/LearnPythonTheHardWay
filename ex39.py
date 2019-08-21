# create a mapping of state to abbreviation

states = {
  'Oregon': 'OR',
  'Florida': 'FL',
  'California': 'CA',
  'New York': 'NY',
  'Texas': 'TX',
  'Illinois': 'IL'
}

cities = {
  'CA': 'San Francisco',
  'TX': 'Austin',
  'IL': 'Chicago',
  'NY': 'New York',
  'FL': 'Miami'
}

cities['OR'] = 'Portland'
cities['TX'] = 'Dallas'

print('-' * 10)
print('NY State has: ', cities['NY'])
print("OR State has: ", cities['OR'])
print("TX State has: ", cities['TX'])
print("IL State has: ", cities['IL'])

# print some states 
print('-' * 10)
print("California's abbreviation is: ", states["California"])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
for abbrev, city in list(cities.items()):
  print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)

for state, abbrev in list(states.items()):
  print(f"{state} state is abbreviated {abbrev}")
  print(f"and has the city {cities[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Nebraska')

if not state:
  print("Sorry, no Nebraska")

# get a city with a default value
city = cities.get('NJ', 'Does Not Exist')
print(f"The city for the state 'NJ' is: {city}")