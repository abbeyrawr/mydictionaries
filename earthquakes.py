# finished
"""
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

"""

import json

##1) print out the number of earthquakes
og = open("eq_data.json", "r")
eq = json.load(og)
print("Number of Earthquakes:", len(eq["features"]))


# 2) iterate through the dictionary and extract the location, magnitude, longitude and latitude of the location and put it in a new
# dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a magnitude > 6. Print out the new dictionary
eq_dict = {}

for x in eq["features"]:
    mag = x["properties"]["mag"]
    longitude = x["geometry"]["coordinates"][0]
    lat = x["geometry"]["coordinates"][1]
    loc = x["properties"]["place"]

    if mag > 6:
        eq_dict[loc] = {
            "location": loc,
            "magnitude": mag,
            "longitude": longitude,
            "latitude": lat,
        }

print(eq_dict)


"""
3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

"""

for x, y in eq_dict.items():
    for a, b in y.items():
        print(f"{a}: {b}")
    print()
