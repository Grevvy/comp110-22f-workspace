"""Demonstrations of dictionary capabilites."""


# Declaring the type of dictionary
schools: dict[str, int]

# Initialize to an empty dicitionary
schools = dict()

# Set a key-value pairing in the dicitionary
schools["UNC"] = 19_400
schools["Duke"] = 6_717
schools["NCSU"] = 26_150

# Print a dictionary literal representation
print(schools)

# Access a value b its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from a dictionary
# By its key.
schools.pop("Duke")

# Test for the existance of a key
if "Duke" in schools:
    print("Found the key 'Duke' in schools")
else:
    print("No key 'Duke' in schools")

# update / reassign a key-value pair
schools["UNC"] = 20_000
schools["NCSU"] += 200

print(schools)

# Demonstration of dictionary literals

# Empty dictionary literal
schools = {} # Same as dict()
print(schools)

# Alternatively, initialize key-value pairs
schools = {
    "UNC": 19400, 
    "Dukie": 6717, 
    "NCSU": 26150
}

print(schools)

# What happens when a key does not exist?
# print(schools["UNCC"])

# Example looping over the keys of a dict
# for key in schools:
#     print(f"Key: {key} -> Value: {schools[key]}")

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")