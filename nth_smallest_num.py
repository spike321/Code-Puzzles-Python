#partial selection sort O(kn)


#---------------------------------------------------------------
import numpy as np
import heapq
def nth_smallest_num(a, n):
    return np.partition(a, n)[n]
