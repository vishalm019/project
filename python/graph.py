import matplotlib.pyplot as plt
from matplotlib import style
import csv 
  
x = []
y = []
x2 = []
y2 = []
  
with open('Salary_Data.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        x.append(row[0])
        y.append(int(row[1]))
        x2.append(row[2])
        y2.append(int(row[3]))
  
plt.plot(x,y,'g',label='line one',linewidth=5)
plt.plot(x2,y2,'c',label='line two',linewidth=5)


plt.title("Info")
plt.ylabel("Y axis")
plt.xlabel("X axis")

plt.legend()
plt.grid(True,color='k')
plt.show()



