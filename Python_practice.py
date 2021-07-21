
counties_dict = ["Arapahoe","Denver","Jefferson"]
if counties_dict[1] =='Denver': 
    print(counties_dict[1])

temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

# What is the score?
score = int(input("WHat is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')

else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your score is a D.')
            else:
                print('Your grade is an F.')


# if-elif-else ELIF STATEMENT

# WHat is the score?
score = int(input("What is your test score?"))

# Determine the grade.
if score >=90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70: 
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else: 
    print("Your grade is an F.")


counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else: print("El Paso is not in the list of counties.")

for county in counties:
    print(county)

# Iterate through Lists and Tuples

for i in range(len(counties)):
    print(counties[i])

# Iterate Through a Dictionary
for county in counties_dict:
    print(county)

#Get Each Dictionary in a List of Dictionaries

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)

#Get the Values from a List of Dictionaries:
    #nested for loop

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

# General format for a number to format in an f-string is:
f'{value:{width},.{precision}}'
 #(comma after width is a thousands separator)
 