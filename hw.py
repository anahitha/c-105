import pandas as pd
import math

d = [60,61,65,63,98,99,90,95,91,96]

#mean
total_marks = 0
total_entries = len(d)

for i in d:
    total_marks += i

mean = total_marks / total_entries
print("Mean: "+str(mean))

count = 0
#standard deviation
for i in d:
    x = float(i) - mean 
    x=x*x
    count+=x
dev = count/total_entries
standarddev = math.sqrt(dev)
print(standarddev)

#graph