from typing import List, Any, Union

import pandas as pd


def toFahren(df):
    li = []
    for i in df['temp']:
        li.append((i * 9 / 5) + 32)
    return li


climateDf = pd.DataFrame({'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                          'temp': [12, 13, 14, 11, 15, 11, 10]})
li = toFahren(climateDf)
climateDf['temp2'] = li
print(climateDf)
print(climateDf['temp2'].describe())
print(climateDf)
out = climateDf.to_csv('Climate.csv', index=False)