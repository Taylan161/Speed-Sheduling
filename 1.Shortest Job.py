import numpy.random as rnd
import matplotlib.pyplot as plt

#queue generator
# true = quick ; false = slow
line = [rnd.randint(10) for x in range(100)]

line = sorted(line,reverse=True) 


#waittime in secounds
wait=[0]
for x in range(1, len(line)):

    if line[x] == True:

        wait.append(wait[x - 1] + 30)

    else:

        wait.append(wait[x - 1] + 150)

print(wait)

