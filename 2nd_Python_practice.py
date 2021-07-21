

counties_dict = {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
# for county in counties_dict.keys():
#     print(county)

# for voters in counties_dict.values():
#     print(voters)

# Getting Key and Value from Dictionaries #

# for county in counties_dict:
#     print(counties_dict[county])

# # Using  .get

# for county in counties_dict:
#     print(counties_dict.get(county))


#Get the Key-Value Pairs of a Dictionary

# for county, voters in counties_dict.items():
#     print(county, " has ", voters, " registered voters.")

# # THank you Andrew for helping me understand this!
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county": "Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
# for c in voting_data:
#     print(c['county'], 'county has ', str(c['registered_voters']), ' registered voters.')


#Import the datetime class from the datetime module.
import datetime

#use the now() attribut on the datetime class to get the present time.
now = datetime.datetime.now()

#print the present time.
print("The time right now is", now)

import datetime as dt
now = dt.datetime.now()
print("The time right now is", now)

