import numpy as np

sales = np.array([1200, 1500, 900, 2000, 1800, 1700, 1600])

# sum of sales 
total = np.sum(sales)
print("Weekly sales:  ",total)

average = total / len(sales)
print("average : ",average)

# Highest and lowest sales 

highest = np.max(sales)
lowest = np.min(sales)

print("Highest sales day : ",highest)
print("lowest sales day : ",lowest)

# Stander deviation
std_dev = np.std(sales)
print("stander deviation : ",std_dev)


# identity above average days 
mask = sales > average
print(sales[mask])