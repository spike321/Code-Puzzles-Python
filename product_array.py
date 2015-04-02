def get_product_of_all_ints_except_at_index(array):
    product = 1
    flag_zero = 0
    new_array = [0 for i in array]
    for i in range (0, len(array)):
        if(array[i] != 0):
            product = product * array[i]
        else:
            flag_zero += 1
            if(flag_zero == 1):
                index_of_first_zero = i
    if(flag_zero == 1):
        new_array[index_of_first_zero] = product
        return new_array
    if(flag_zero > 1):
        return new_array
    for i in range(0, len(array)):
        if(array[i] != 0):
            new_array[i] = product /  array[i]
        else:
            new_array[i] = product
    return new_array

array = [7,3,4,0,5,6,7,9,2,0,3,6,8,9]
print(get_product_of_all_ints_except_at_index(array))