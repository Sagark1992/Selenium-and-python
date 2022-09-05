myDict = {
    'Name':'Sagar',
    'Surname': 'Karande',
    'Address': 'Sasure',
    'Mob no.': 8600437317,
    'Fav color': ['Black', 'Gray', 'Navy blue'],
}

#  Dictionary methods:
# 1. dict.keys() - It will give the list of keys from given dictionary
print(myDict.keys())

# 2. dict.values() - It will give the list of values from given dictionary
print(myDict.values())

# 3. dict.items() - It will give keys and values in the form of tuple from given dictionary
print(myDict.items())

# 4. dict.update() - It will update the given dictionary with new contents
updateDict = {
    'Fav Food' : 'Mutton'
}

myDict.update(updateDict)
print(myDict)

# 5. dict.get() - It will gives the value of given dictionary, if that given key not present in dictionary it will returns None
print(myDict.get('Name'))   #It will returns value for given key from dictionary
print(myDict['Name'])       #It will returns value for given key from dictionary

# Difference between .get() and [] syntax
print(myDict.get('Name2'))  #It will returns value for given key from dictionary
print(myDict['Name2'])      #It will throws an error (KeyError: 'Name2')

