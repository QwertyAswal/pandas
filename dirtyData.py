import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

dirty = pd.read_csv('dirty_data.csv')
outer = pd.read_csv('outliers.csv')
missing = pd.read_csv('missing_value.csv')


# Function To remve Dirty Data
def remdirt():
    global dirty
    # renaming Id column
    dirty.rename(columns={'Unnamed: 0': 'Id'}, inplace=True)

    # check if id is unique
    print(len(dirty['Id'].unique()))

    # cleaning 'Uber Type' column
    fl = 0
    for i, j in dirty.iterrows():
        if j['Id'][2] == '1':
            dirty.loc[i, 'Uber Type'] = 0
        if j['Id'][2] == '3':
            dirty.loc[i, 'Uber Type'] = 1
        if j['Id'][2] == '5':
            dirty.loc[i, 'Uber Type'] = 2

    # cleanig Dirty Latitude
    for i, j in dirty.iterrows():
        if j['Origin Latitude'] > 0:
            dirty.loc[i, 'Origin Latitude'] = -dirty.loc[i, 'Origin Latitude']
    for i, j in dirty.iterrows():
        if j['Destination Latitude'] > 0:
            dirty.loc[i, 'Destination Latitude'] = -dirty.loc[i, 'Destination Latitude']

    # x = np.array(list(dirty['Origin Latitude'].values))
    # y = np.array(list(dirty['Origin Region'].values))
    # xD = np.array(list(dirty['Destination Latitude'].values))
    # yD = np.array(list(dirty['Destination Region'].values))
    # l = np.array(dirty['Journey Distance(m)'].values)
    # t = np.array(dirty['Travel Time(s)'].values)
    # # plt.scatter(l, t, label='Origin')

    # cleaning dirty date
    date = np.array(dirty['Departure Date'].values)
    mn = []
    day = []
    dat = []
    for i in date:
        temp = i.split('-')
        if int(temp[1]) > 12:
            t = temp[1]
            temp[1] = temp[2]
            temp[2] = t
        if int(temp[1]) == 2 and int(temp[2]) > 28:
            temp[2] = 28
        elif int(temp[1]) % 2 == 1 and int(temp[1]) < 8 and int(temp[2]) > 31:
            temp[2] = 31
        elif int(temp[1]) % 2 == 0 and int(temp[1]) > 7 and int(temp[2]) > 31:
            temp[2] = 31
        elif int(temp[1]) % 2 == 0 and int(temp[1]) < 8 and int(temp[2]) > 30:
            temp[2] = 30
        elif int(temp[1]) % 2 == 0 and int(temp[1]) > 7 and int(temp[2]) > 30:
            temp[2] = 30
        dat.append(str(temp[2]) + '-' + str(temp[1]) + '-' + str(temp[0]))
        mn.append(temp[1])
        day.append(temp[2])

    # cleaning dirty Departure And Arrival Time
    dirty['Departure Date'] = dat
    c = 0
    for i, j in dirty.iterrows():
        temp = j['Departure Time'].split(':')
        temp1 = j['Arrival Time'].split(':')
        arri = int(temp1[0]) * 60 * 60 + int(temp1[1]) * 60 + int(temp1[2])
        dep = int(temp[0]) * 60 * 60 + int(temp[1]) * 60 + int(temp[2])
        if dep > arri:
            arri += 24 * 60 * 60
        if arri - dep >= int(j['Travel Time(s)']) - 100 and arri - dep <= int(j['Travel Time(s)']) + 100:
            c += 1
        else:
            if j['Journey Distance(m)'] / j['Travel Time(s)'] * 18 / 5 > j['Journey Distance(m)'] / (
                    arri - dep) * 18 / 5:
                arri = dep + j['Travel Time(s)']
                sec = arri % 60
                arri /= 60
                mi = arri % 60
                arri /= 60
                hr = arri % 24
                dirty.loc[i, 'Arrival Time'] = str(hr) + ':' + str(mi) + ':' + str(sec)
            else:
                dirty.loc[i, 'Travel Time(s'] = arri - dep
    dirty.to_csv('dirty.csv')


remdirt()


# Outliers
def remout():
    global outer

    # Removing Outlier
    # print(outer['Unnamed: 0'].is_unique)
    # plt.hist(outer['Uber Type'], bins=20, label='Uber Type')
    # plt.legend
    # plt.show()
    # plt.hist(outer['Origin Latitude'], bins=20, label='Origin Latitude')
    # plt.legend
    # plt.show()
    # plt.hist(outer['Origin Longitude'], bins=20, label='Origin Latitude')
    # plt.legend
    # plt.show()
    # plt.scatter(outer['Origin Latitude'], outer['Origin Longitude'], label='Test')
    # plt.legend
    # plt.show()
    mLatO = outer['Origin Latitude'].mean()
    sdLatO = outer['Origin Latitude'].std()
    c = 0
    print(mLatO, sdLatO)
    for i, j in outer.iterrows():
        if j['Origin Latitude'] >= mLatO + sdLatO or j['Origin Latitude'] <= mLatO - sdLatO:
            outer = outer.drop(i)
            # print(j)
            c += 1
    mLonO = outer['Origin Longitude'].mean()
    sdLonO = outer['Origin Longitude'].std()
    c = 0
    # print(mLonO, sdLonO)
    for i, j in outer.iterrows():
        if j['Origin Longitude'] >= mLonO + 2 * sdLonO or j['Origin Longitude'] <= mLonO - 2 * sdLonO:
            outer = outer.drop(i)
            # print(j)
            c += 1
    print(c)
    print(outer.__len__())
    plt.scatter(outer['Origin Latitude'], outer['Origin Longitude'], label='Test')
    plt.legend
    plt.show()
    mLatD = outer['Destination Latitude'].mean()
    sdLatD = outer['Destination Latitude'].std()
    c = 0
    # print(mLatO, sdLatO)
    plt.scatter(outer['Destination Latitude'], outer['Destination Longitude'], label='Test')
    plt.legend
    plt.show()
    for i, j in outer.iterrows():
        if j['Destination Latitude'] >= mLatD + sdLatD or j['Destination Latitude'] <= mLatD - sdLatD:
            outer = outer.drop(i)
            # print(j)
            c += 1
    mLonD = outer['Destination Longitude'].mean()
    sdLonD = outer['Destination Longitude'].std()
    c = 0
    # print(mLonO, sdLonO)
    for i, j in outer.iterrows():
        if j['Destination Longitude'] >= mLonD + sdLonD or j['Destination Longitude'] <= mLonD - sdLonD:
            outer = outer.drop(i)
            # print(j)
            c += 1
    print(c)
    plt.scatter(outer['Destination Latitude'], outer['Destination Longitude'], label='Test')
    plt.legend
    plt.show()

    outer.to_csv('outer.csv')


remout()

from sklearn import linear_model as l_m


# Missing Value

def remmissing():
    global missing
    jd = []
    tt = []
    fr = []
    ut = []
    miss = pd.read_csv('missing_value.csv')
    column = miss.columns
    print(column)
    lic = 0
    erli = []
    testJd = []
    testTt = []
    testUt = []
    for i in column:
        erli.append(miss[i].isnull().sum())
    li = ({'1': 0, '3': 1, '5': 2})
    for i, j in missing.iterrows():
        if np.isnan(j['Uber Type']):
            miss.loc[i, 'Uber Type'] = li[j['Unnamed: 0'][2]]
        if np.isnan(j['Fare$']):
            testJd.append(j['Journey Distance(m)'])
            testTt.append(j['Travel Time(s)'])
            testUt.append(miss['Uber Type'][i])
        else:
            jd.append(j['Journey Distance(m)'])
            tt.append(j['Travel Time(s)'])
            fr.append(j['Fare$'])
            ut.append(miss['Uber Type'][i])
    re = pd.DataFrame()
    re['ut'] = ut
    re['jd'] = jd
    re['tt'] = tt
    re['fr'] = fr
    rcs = l_m.LinearRegression()
    rcs.fit(re[['ut', 'jd']], re['fr'])
    for i in range(testTt.__len__()):
        print('Journey Distane: ', testJd[i], 'Travel Time: ', testTt[i], 'Uber Type: ', testUt[i])
        print('Fare: ', rcs.predict([[testUt[i], testJd[i]]]))


remmissing()
