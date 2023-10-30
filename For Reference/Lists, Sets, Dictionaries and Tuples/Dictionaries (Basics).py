# Dictionaries are unordered mappings for storing objects. They use a key-value pairing. This key-value pair allows a 
# user to quickly grab objects without needing to know an index location.
# Dictionaries use curly braces and colons to signify the keys and their associated values. 
# Syntax - {'key1': 'value1', 'key2': 'value2'}
# Objects are retrieved by key name. They are unordered and can not be sorted.

# Creating a dictionary with the name 'person' and assigning it the key/value pairs.
person = {'name': 'Anant', 'age': 31, 'interests': ['Playing Cricket','Driving']}

person['phone']='8297411942' #T his is how we can add a key and its value in the dictionary.
person['age']=30 # Doing this will update the value for the mentioned key in our dictionary.
print(person)
# {'name': 'Anant', 'age': 30, 'interests': ['Playing Cricket', 'Driving'], 'phone': '8297411942'}

print(person.get('phone'))
# 8297411942
print(person['phone']) # Printing the value of the key 'phone' in the dictionary 'person'.
# 8297411942

person.update({'name':'AU','phone':8299999999,'age':32}) # Updating the dictionary 'person' with the new key/value pairs.
# person |= {'name':'AU','phone':8299999999,'age':32} # Alternate method to update a dictionary.

del person['age'] #The del keyword helps in deleting a key/value from the dictionary.
phone = person.pop('phone') #The pop method (just like in lists) will remove the last item or key/value from our dictionary. It can be also saved in a variable to be printed out later.
print(phone)
# 8299999999

print(person.keys())
# dict_keys(['name', 'interests'])

print(person.values())
# dict_values(['AU', ['Playing Cricket', 'Driving']])

print(person.items())
# dict_items([('name', 'AU'), ('interests', ['Playing Cricket', 'Driving'])])

for key, value in person.items():
    print(key, value)
# name AU
# interests ['Playing Cricket', 'Driving']

print(person)
# {'name': 'AU', 'interests': ['Playing Cricket', 'Driving']}
