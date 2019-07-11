import pandas as pd


def toCelcius(df):
    li = []
    for i in df['TAVG']:
        li.append((i - 32) * 5 / 9)
    return li


lokka = pd.read_csv("lokkaFinal.txt", delimiter='\s+', na_values=-9999, engine='python')
lokka = lokka.drop(0)
lokka['ELEVATION'] = lokka['ELEVATION'].astype(float)
lokka['LATITUDE'] = lokka['LATITUDE'].astype(float)
lokka['LONGITUDE'] = lokka['LONGITUDE'].astype(float)
lokka['PRCP'] = lokka['PRCP'].astype(float)
lokka['TMAX'] = lokka['TMAX'].astype(float)
lokka['TMIN'] = lokka['TMIN'].astype(float)
lokka['TAVG'] = (lokka['TMIN'] + lokka['TMAX']) / 2
l = toCelcius(lokka)
lokka['TAVG'] = l
li = []
for i in lokka['DATE']:
    li.append(i[:6])
lokka['Month'] = li
temp = lokka.groupby('Month')
liMonthly = []
liTemp = []
for i, j in temp:
    liMonthly.append(i)
    liTemp.append(j['TAVG'].mean())
monthData = pd.DataFrame({'Month': liMonthly, 'TempsC': liTemp})
monthData['Month'] = monthData['Month'].astype(int)
monthData['MonthE'] = monthData['Month'] % 100
li = monthData.groupby('MonthE')
resM = []
resT = []
for i, j in li:
    resM.append(i)
    resT.append(j['TempsC'].mean())
referenceTemps = pd.DataFrame({'Month': resM, 'avgTempsC': resT})
li = []
ct = 0
for i in monthData['TempsC']:
    li.append(i - referenceTemps['avgTempsC'][ct])
    ct = (ct + 1) % 12
monthData['Diff'] = li
monthData.to_csv('Sodankyla.csv')
sodankyla = pd.read_csv('Sodankyla.csv')
helsinki = pd.read_csv('Helsinki.csv')
diffMonth = []
diffTemp = []
for i in range(1, 790):
    for j in range(1, 675):
        if helsinki['monthlyData'][i] == sodankyla['Month'][j]:
            diffMonth.append(sodankyla['Month'][j])
            diffTemp.append(sodankyla['TempsC'][j] - helsinki['Tempsc'][i])
resFinal = pd.DataFrame({'Month': diffMonth, 'TempDiff': diffTemp})
resFinal.to_csv('Problem4Exercise2.csv', index=0)
print(resFinal)
