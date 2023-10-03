import random as ran
import matplotlib.pyplot as plt

zahlen = []
dict_ziehungen_statistic = {}
for i in range(46):
    zahlen.append(i)
    dict_ziehungen_statistic[i] = 0

def lottoziehung(array, anzahlZiehungen):
    gezogene_zahlen = []
    for i in range(anzahlZiehungen):
        rand = ran.randint(0,45-i)
        array[rand], array[45-i] = array[45-i], array[rand]
        gezogene_zahlen.append(array[45-i])
    return gezogene_zahlen


ziehungen = lottoziehung(zahlen,6)
print(ziehungen)

def lottoziehung_statistic(ziehungen):
    for i in range(ziehungen):
        rand = ran.randint(0, 45)
        dict_ziehungen_statistic[rand] = dict_ziehungen_statistic[rand] + 1
    return dict_ziehungen_statistic




data = lottoziehung_statistic(1000000)
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots()
axs.bar(names, values)
fig.suptitle('Lottozeihungen')
axs.set_ylabel('Anzahl der gezogenen Zahlen')
axs.set_xlabel('Mögliche Zahlen')

plt.show()
