states = ['Madhya Pradesh','Chhattisgarh','Telangana','Uttar Pradesh']
capitals=['Bhopal','Raipur','Hyderabad','Lucknow']

for index, city in enumerate(capitals):
    print(f'{index} - {city}')
# 0 - Bhopal
# 1 - Raipur
# 2 - Hyderabad
# 3 - Lucknow

for index, city in enumerate(capitals,start=1):
    print(f'City#{index} is {city}')
# City#1 is Bhopal
# City#2 is Raipur
# City#3 is Hyderabad
# City#4 is Lucknow

for capital, state in zip(capitals,states):
    print(f'The capital of {state} is {capital}')
# The capital of Madhya Pradesh is Bhopal
# The capital of Chhattisgarh is Raipur
# The capital of Telangana is Hyderabad
# The capital of Uttar Pradesh is Lucknow

[print(f'The capital of {state} is {capital}') for capital, state in zip(capitals,states)] # Using List comprehension to get the same result as above code.
# The capital of Madhya Pradesh is Bhopal
# The capital of Chhattisgarh is Raipur
# The capital of Telangana is Hyderabad
# The capital of Uttar Pradesh is Lucknow

for index, (capital, state) in enumerate(zip(capitals,states),start=1):
    print(f'{index}. The capital of {state} is {capital}')
# 1. The capital of Madhya Pradesh is Bhopal
# 2. The capital of Chhattisgarh is Raipur
# 3. The capital of Telangana is Hyderabad
# 4. The capital of Uttar Pradesh is Lucknow
    
