import numpy as np
import pandas


my_array = np.array([[2, 4, 7], [5, 8, 1]])
colname = ['one', 'two', 'three']
rowname = ['$', '@']
dataframe = pandas.DataFrame(my_array, index=rowname, columns=colname)
print(dataframe)
