s = input("Enter a String to be compared")
# st='rohrohrohrohroh'
st = 'oceans and lakes have much in common but they are also quite different both are bodies of water but oceans are very large bodies of salt water while lakes are much smaller bodies of fresh water lakes are usually surrounded by land while oceans are what surround continents both have plants and animals living in them the ocean is home to the largest animals on the planet whereas lakes support much smaller forms of life when it is time for a vacation both will make a great place to visit and enjoy'
rs = st.replace(' ', '')
li = []
for i in range(s.__len__()):
    for j in range(97, 123):
        li.append(s[:i] + chr(j) + s[i + 1:])
# print(li)
for i in range(0, rs.__len__()):
    temp = rs[i:i + s.__len__()]
    for j in li:
        if j == temp:
            print(j, 'index:- ', i)
            i += s.__len__()
            continue
