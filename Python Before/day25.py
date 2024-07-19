countries = ('Spain', 'Italy', 'India', 'England', 'Germany')
temp = list(countries)
temp.append('Russia')
temp.pop(3)
temp[2] = 'Finland'
countries = tuple(temp)
print(countries)

countries2 = ('Pakistan', 'China')
ncountries = countries+countries2
print(ncountries)

tuple3 = (0,2,4,4,4,4,5,1)
res = tuple3.count(4)
print('Count of 3 in tuple is :', res)