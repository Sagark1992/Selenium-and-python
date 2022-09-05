myDict = {
    'Name':'Sagar',
    'Surname': 'Karande',
    'Address': 'Sasure',
    'Mob no.': 8600437317,
    'Fav color': ['Black', 'Gray', 'Navy blue'],
}

print(myDict['Mob no.'])

# Properties of Dictionary: 
# 1. It is unordered- we cannot first item as first, it is unordered

# 2. It is mutable(can be update)
myDict['Name']= 'Sumit'
print(myDict)

# 3. It is indexed by keys- we can call values by keys
print(myDict['Name'])

# 4. It cannot contain duplicate keys- it will replace latest key value to previous one
dict1 = {
    'Roll no.': 101,
    'Name': 'Sagar Karande',
    'Class': '9th Standard',
    'Name': 'Sumit Karande'
}

print(dict1)