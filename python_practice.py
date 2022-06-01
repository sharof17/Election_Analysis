

counties = ["Arapahoe","Denver","Jefferson","El Paso"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")

# if "Arapahoe" in counties and "El Paso" in counties:
#     print("Arapahoe and El Paso are in the list of counties.")
# else:
#     print("Arapahoe or El Paso is not in the list of counties.")

# for t in counties:
#     print(t)

# for num in range(5):
#     print(num)

# for i in range(len(counties)):
#     print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county in counties_dict:
#     print(county)

# for county in counties_dict.keys():
#     print(county)

# for voters in counties_dict.values():
#     print(voters)

# for county in counties_dict:
#     print(counties_dict[county])

# for key, value in counties_dict.items():
#     print(f" {key} county has {value} registered voters.")
#     print("%s county has %s registered voters." % (key, value))
#     print("{} HAS {} voters.".format(key, value))
    
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)

# for i in range(len(voting_data)):

#       print(voting_data[i]['county'])

# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

for county_dict in voting_data:
    print(county_dict["registered_voters"])
       