#greedy means keep track of your answer while you traverse

def find_highest_product_from_three_ints_tril1(array):
    max = [None, None, None]
    for i in range(0, len(array)):
        if(array[i] > max[0]):
            max[2] = max[1]
            max[1] = max[0]
            max[0] = array[i]
    return max

def find_highest_product_from_three_ints_tril2(array):
    if(len(array)<3):
        raise Exception("aray less than 3")
    max = [array[0], None, None]
    min = [None, None, None]
    for i in range(0,len(array)):
        if(array[i]>max[0]):
            max[2] = max[1]
            max[1] = max[0]
            max[0] = array[i]
        if(array[i]<min[0]):
            min[2] = min[1]
            min[1] = min[0]
            min[0] = array[i]
        return max(max[2]*max[1]*max[0], max[0]*max[1]*min[0], max[0]*min[0]*min[1], min[0]*min[1]*min[2]) # can't fill all maxs and mins, some are still NoneTyep

def find_highest_product_from_three_ints_tril2(array):

    highest_product = 0
    highest = None
    second_highest = None
    lowest = None
    second_lowest = None
    for i in range(0,len(array)):
        if array[i]>highest:
            second_highest = highest
            highest = array[i]
        if array[i]<lowest:
            second_lowest = lowest
            lowest = array[i]
        if (i>3):
            highest_product = max(highest*second_highest*array[i], lowest*second_lowest*array[i])
    return highest_product

array = [-10,-10,1,3,2]
print(find_highest_product_from_three_ints_tril2(array))
