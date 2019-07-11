import pandas as pd


def toCelcius(df):
    li = []
    for i in df['Temp']:
        li.append((i - 32) * 5 / 9)
    return li


# temperature anamalies 1
data = pd.read_csv('1091402.csv', delim_whitespace=True, na_values=-9999)
data = data.drop([0])
data['TAVG'] = data['TAVG'].astype(float)
data['TMIN'] = data['TMIN'].astype(float)
data['TMAX'] = data['TMAX'].astype(float)
nonNa = 0
nonNa = 23716 - data.isna()['TAVG'].sum()
print("Number of non Nrint(monthlyData.resample(rule=1))aN values for tavg:- ", nonNa)

# temperature anamalies 2
nonNa = 23716 - data.isna()['TMIN'].sum()
print("Number of non NaN values for tmin:- ", nonNa)
print("Number of Days:- ", data.__len__())
print("First Observation:- ", data['DATE'][1])
print("Last Observation:- ", data['DATE'][data.__len__()])
print('Avg Temp:- ', data['TAVG'].mean())
maxli = []
ma = data['TMAX'].values
c = 0
for i in data['DATE']:
    # print(i)
    if i[:6] == '196905' or i[:6] == '196906' or i[:6] == '196907' or i[:6] == '196908':
        maxli.append(ma[c])
    c += 1
print('Max Temp:- ', max(maxli))

# temperature anamalies 3
li = []
for i in data['DATE']:
    li.append(i[:6])
data['Monthly'] = li
temp = data.groupby('Monthly')
liMonthly = []
liTemp = []
for i, j in temp:
    liMonthly.append(i)
    liTemp.append(j['TAVG'].mean())
monthlyData = pd.DataFrame({'monthlyData': liMonthly, 'Temp': liTemp})
li = toCelcius(monthlyData)
monthlyData['Tempsc'] = li
monthlyData.to_csv('monthlyData.csv')
monthlyData['monthlyData'] = monthlyData['monthlyData'].astype(int)
monthlyData['months'] = monthlyData['monthlyData'] % 100
li = monthlyData.groupby('months')

# temperature anamalies 4
resM = []
resT = []
for i, j in li:
    resM.append(i)
    resT.append(j['Tempsc'].mean())
referenceTemps = pd.DataFrame({'Month': resM, 'avgTempsC': resT})
li = []
ct = 0
for i in monthlyData['Tempsc']:
    li.append(i - referenceTemps['avgTempsC'][ct])
    ct = (ct + 1) % 12
monthlyData['Diff'] = li
monthlyData.to_csv('Helsinki.csv')
print(monthlyData)
