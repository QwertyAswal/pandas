import pandas as pd

"""df = pandas.read_csv('nyc_weather.csv')
print(df)
maxT = df['Temperature'].max()
print(maxT)
print(df[df['Events'] == 'Rain']['EST'])
print(df[df['Events'] == 'Rain']['WindSpeedMPH'].mean())"""
"""df1 = pd.read_csv('weather_data.csv')
print(df1)"""
list_tuple = [['1/1/2017', 32, 6, 'Rain'], ['1/2/2017', 35, 7, 'Sunny'], ['1/3/2017', 28, 6, 'Snow'],
              ['1/4/2017', 24, 7, 'Snow'], ['1/5/2017', 32, 4, 'Rain'], ['1/6/2017', 31, 2, 'Sunny']]
"""print(*list_tuple, sep='\n')"""
li = pd.DataFrame(list_tuple, columns=['Day', 'Temperature', 'Windspeed', 'Event'])
"""print(li)
print(li.shape)
print(li[2:5])
print(li[['Day','Temperature']])
print(li.columns)
print(li['Temperature'].min())
print(li['Temperature'].max())"""
"""print(li['Temperature'].describe())
print(li[li['Temperature'] == li['Temperature'].max()])
li.to_csv('output.csv', index=False)"""
# ti = pd.read_excel('weather_data.xlsx')
# print(ti)
# ti.to_excel('output12.xlsx',sheet_name='sheet1')
tt = pd.read_csv('weather_data_cities.csv')
# print(tt)
rr = tt.groupby('city')
"""for city_name, city_df in rr:
    print(city_name)
    print(city_df)"""
get_city = rr.get_group('paris')
"""print(get_city.describe())
print(get_city.max())
print(rr.describe())
print(rr.max())"""
"""df = pd.DataFrame({'city': ['a', 'b', 'c'], 'temp': [65, 70, 30]})
# print(df)
df1 = pd.DataFrame({'city': ['q', 'w', 'e', 'r'], 'temp': [2, 3, 4, 5]})
# print(df1)
dfTest = pd.concat([df, df1], ignore_index=True)
print(dfTest)
dfTest1 = pd.concat([df, df1], axis=1)
print(dfTest1)
temp_df = pd.DataFrame({'city': ['a', 'b', 'c', 'd', 'e'], 'temp': [1, 2, 3, 4, 5]})
humidity_df = pd.DataFrame({'city': ['a', 'b', 'c', 'd'], 'humidity': [1.11, 2.22, 3.33, 4.44]})
test_df = pd.merge(temp_df, humidity_df, on='city', how='outer')
print(test_df)
"""

# NUMERICAL INDEXING

df = pd.DataFrame(['a', 'b', 'c', 'd'], index=[3, 4, 7, 14 ^ 12])
print(df.loc[4:14^12])
