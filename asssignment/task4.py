#Task 4: Aggregation Operations Given a 2D array:

import numpy as np

data = np.array([ 
                [10, 20, 30], 
                [40, 50, 60], 
                [70, 80, 90]
])

# row wise sum
row_sum = np.sum(data,axis=1)
print("Row wise sum : ",row_sum)

# column wise sum 
col_sum = np.sum(data,axis=0)
print("Column wise sum : ",col_sum)

# miniumn , maxiumn value from the data
mini_values = np.min(data,axis = 0)
max_values = np.max(data,axis = 0)

print("minimume value : ",mini_values)
print("Maximum values: ",max_values)

# mean of sales 
mean_value = np.mean(data)
print("overvall mean : ",mean_value)