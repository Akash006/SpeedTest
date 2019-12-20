import matplotlib.pyplot as plt
import csv

x = []
y = []

for q in range(41):
    x.append(q)
    y.append(q)

'''
with open('output_01.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        #x.append(int(row[0]))
        a = int(row[6]) / 1000/1000
        y.append(a)
'''

plt.plot(x,y,marker='0')

plt.title('SpeedTest')

plt.xlabel('Time')
plt.ylabel('Speed')

plt.show()
