import math
import numpy as np

def findMedian(arr):
    res = []

    for i in range(len(arr)):
        sorted_array = sorted(arr[:i + 1])
        mid = i // 2 # integer division to get the mid index

        # even
        if i % 2 == 0: 
            median = sorted_array[mid]
        else:
            median = (sorted_array[mid] + sorted_array[mid + 1]) / 2
    
        res.append(int(median))
    return res


arr = [5,15,1,3]
res = findMedian(arr)
print(res)