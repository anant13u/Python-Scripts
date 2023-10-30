# Creating a list of states.
states = ['Madhya Pradesh', 'Chhattisgarh', 'Telangana', 'Uttar Pradesh']

# Creating a list of capitals of above-mentioned states.
capitals = ['Bhopal', 'Raipur', 'Hyderabad', 'Lucknow']

# Below we are creating a dictionary from two lists.
statesandcapitals = dict(zip(states,capitals))
for state, capital in statesandcapitals.items():
    print(f'The capital of {state} is {capital}')
# The capital of Madhya Pradesh is Bhopal
# The capital of Chhattisgarh is Raipur
# The capital of Telangana is Hyderabad
# The capital of Uttar Pradesh is Lucknow
