mobiles = {"Apple": {"model":"Iphone17" , "price":160000 , "color" : "black"}, "samsung":{"model": "s25", "price":100000 , "color":"white"},  "Goggle":{"model": "pixel11", "price":80000 , "color":"black"}}
# return all keys from the dictionary mobiles

print(mobiles.keys()) # dict_keys(['Apple', 'samsung', 'Goggle'])

# To get the keys as a list:===========================================
print(list(mobiles.keys())) # ['Apple', 'samsung', 'Goggle']

# return all values from the dictionary mobiles

print(mobiles.values())
# To get the values as a list:
print(list(mobiles.values()))


# Remember:
# - .keys() → Returns all keys.
# - .values() → Returns all values.
# - .items() → Returns all key-value pairs.

# 1. Return all keys using for loop
for i in mobiles:
    print(i)

# 2. Return all values using for loop
for i in mobiles:
    print(mobiles[i])
    
# 3. Return both keys and values using for loop
for key, value in mobiles.items():
    print(key, value)
    
# Code	Purpose
# for i in mobiles:	Keys
# for i in mobiles.values():	Values
# for k, v in mobiles.items():	Both keys and values

# return model and color name of each beand
for i in mobiles:
    print(mobiles[i]["model"], mobiles[i]["color"])
# Explanation:
# - for i in mobiles: → Iterates through brand names.
# - mobiles[i] → Accesses each brand's inner dictionary.
# - ["model"] → Gets the model name.
# - ["color"] → Gets the color name.

# Difference between your two programs:
# Code	Output
# print(i, mobiles[i]["model"], mobiles[i]["color"])	Brand + Model + Color
# print(mobiles[i]["model"], mobiles[i]["color"])	Model + Color

# return model and color name along with  brand
for i in mobiles:
    print(i, mobiles[i]["model"], mobiles[i]["color"])
    
# How it works:
# 1. for i in mobiles: → Iterates through the brand names (keys).
# 2. mobiles[i] → Accesses the inner dictionary of each brand.
# 3. ["model"] → Retrieves the model name.
# 4. ["color"] → Retrieves the color.
# Remember: This is called a nested dictionary, because a dictionary is stored inside another dictionary.


# return  the model nsmes which having the color black
# # Return model names having black color

for i in mobiles:
    if mobiles[i]["color"] == "black":
        print(mobiles[i]["model"])

# Explanation:
# 1. for i in mobiles: → Iterates through each brand.
# 2. mobiles[i]["color"] == "black" → Checks whether the color is black.
# 3. mobiles[i]["model"] → Prints the corresponding model name.

# return the mobile model name, brand name and price having price btw 80k included and 1.4 lakkhs incuded with black in color
for i in mobiles:
    if 80000 <= mobiles[i]["price"] <= 140000 and mobiles[i]["color"] == "black":
        print(i, mobiles[i]["model"], mobiles[i]["price"])

# Goggle pixel11 80000
# Explanation:
# - 80000 <= mobiles[i]["price"] <= 140000 → Checks the price range.
# - mobiles[i]["color"] == "black" → Checks the black color.
# - print(i, mobiles[i]["model"], mobiles[i]["price"]) → Prints brand, model and price.
# Remember: and means both conditions must be true.

