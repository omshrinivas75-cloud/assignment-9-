import numpy as np 

marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])
sorted_array = np.sort(marks)

print(sorted_array)

average = np.mean(marks)
print("Avreage marks : ",average)

# 25th , 50th , 75th percentile
p25 = np.percentile(marks, 25)
p50 = np.percentile(marks, 50)
p75 = np.percentile(marks, 75)

print("25th Percentile:", p25)
print("50th Percentile (Median):", p50)
print("75th Percentile:", p75)

count_above_avg = np.sum(marks > average)
print("student above average : ",count_above_avg)


