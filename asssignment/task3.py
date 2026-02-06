import numpy as np

Values = np.array([2,4,6,8,10])

# square of every elemnet 
sqrt_value = np.sqrt(Values)
print("Square root of each element : \n", sqrt_value)

# exponetial of every element
exp_value = np.exp(Values)
print("Exponential of each element \n: ", exp_value)

# logirithm of every element 
log_value = np.log(Values)
print("Logarithm of each element : \n", log_value)

# total of values  
total_sum = np.sum(Values)
print("Total sum of all elements : \n", total_sum)

cumulative_sum = np.cumsum(Values)
print("Cumulative sum of each element : \n", cumulative_sum)


