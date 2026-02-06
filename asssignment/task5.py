import numpy as np

marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])

marks_mean = np.mean(marks)
print("Mean : ",marks_mean)

median_marks = np.median(marks)
print("Median : ",median_marks)

minimum = np.min(marks)
print("minium value : ",minimum)

maximun = np.max(marks)
print("maximun value : ",maximun)

varience_val = np.var(marks)
print("varience : ",varience_val)

std_dev = np.std(marks)
print("stander deviation : ",std_dev)

range_val = maximun - minimum 
print("Range: ",range_val)


