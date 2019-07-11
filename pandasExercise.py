import pandas as pd


def findOut(df):
    ls = []
    maxVal = df['TEMP'].mean() + 2 * df['TEMP'].std()
    minVal = df['TEMP'].mean() - 2 * df['TEMP'].std()
    for i in df['TEMP']:
        if (i >= minVal and i <= maxVal):
            ls.append(True)
        else:
            ls.append(False)
    return ls


def toCelcius(df):
    li = []
    for i in df['TEMP']:
        li.append((i - 32) * 5 / 9)
    return li


def toInt(df):
    li = []
    for i in df['Celsius']:
        li.append(round(i))
    return li


def getNew(df):
    li = []
    for i in df['YR--MODAHRMN']:
        li.append(i // 100)
    return li


# question 1
df = pd.read_csv('6153237444115dat.csv', na_values=['*', '**', '***', '****', '*****', '******'])
print("Rows:- ", df.__len__())
print("Columns:- ", *df.columns)
print("Column Types:- \n", df.dtypes)
print("Mean Temp:- ", df['TEMP'].mean())
print("Standard Deviation Max Temp:- ", df['MAX'].std())
ls = df['USAF'].unique()
print(ls.__len__())

# find outer
df['Outer'] = findOut(df)

# exercise 2
selected = pd.DataFrame({'USAF': list(df['USAF']), 'YR--MODAHRMN': list(df['YR--MODAHRMN']), 'TEMP': list(df['TEMP']),
                         'MAX': list(df['MAX']), 'MIN': list(df['MIN'])})
selected = selected.dropna(axis=0, how='any', subset=['TEMP'])
li = toCelcius(selected)
selected['Celsius'] = li
selected['Celsius'] = toInt(selected)
selectedUSAF = selected.groupby('USAF')
kumpula = selectedUSAF.get_group(29980)
kumpula.to_csv('Kumpula_temps_May_Aug_2017.csv')
rovaniemi = selectedUSAF.get_group(28450)
rovaniemi.to_csv('Rovaniemi_temps_May_Aug_2017.csv')

# exercise 3
li = list(kumpula['TEMP'])
print("Median Kumpula:- ", li[li.__len__() // 2])
li = list(rovaniemi['TEMP'])
print("Median Rovaniemi:- ", li[li.__len__() // 2])
kumpula_may = kumpula[kumpula['YR--MODAHRMN'] // 1000000 == 201705]
kumpula_june = kumpula[kumpula['YR--MODAHRMN'] // 1000000 == 201706]
rovaniemi_may = rovaniemi[rovaniemi['YR--MODAHRMN'] // 1000000 == 201705]
rovaniemi_june = rovaniemi[rovaniemi['YR--MODAHRMN'] // 1000000 == 201706]
print("Kumpala:-")
print("May:-")
print("Mean:-", kumpula_may['TEMP'].mean())
print("Min:-", kumpula_may['TEMP'].min())
print("Max:-", kumpula_may['TEMP'].max())
print("June:-")
print("Mean:-", kumpula_june['TEMP'].mean())
print("Min:-", kumpula_june['TEMP'].min())
print("Max:-", kumpula_june['TEMP'].max())
print("Rovaniemi:-")
print("May:-")
print("Mean:-", rovaniemi_may['TEMP'].mean())
print("Min:-", rovaniemi_may['TEMP'].min())
print("Max:-", rovaniemi_may['TEMP'].max())
print("June:-")
print("Mean:-", rovaniemi_june['TEMP'].mean())
print("Min:-", rovaniemi_june['TEMP'].min())
print("Max:-", rovaniemi_june['TEMP'].max())

# exercise 4
liNew = getNew(df)
df['HRNEW'] = liNew
hour = []
mea = []
ma = []
mi = []
newData = df.groupby('HRNEW')
for i, j in newData:
    hour.append(i)
    mea.append(j["TEMP"].mean())
    ma.append(j["TEMP"].max())
    mi.append(j['TEMP'].min())
lastDF = pd.DataFrame({'Hour': hour, 'Mean': mea, 'Max': ma, 'Min': mi})
print(lastDF)
lastDF.to_csv('LastCSV.csv', index=False)
