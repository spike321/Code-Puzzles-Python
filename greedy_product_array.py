def get_products_of_all_ints_except_at_index(array):
    new_array = [0 for i in array]
    product = 1
    for i in range(0, len(array)):
        new_array[i] = product
        product *= array[i]
    product = 1
    for i in reversed(range(0, len(array))): # new looping backwards
        new_array[i] *= product
        product *= array[i]
    return new_array

array = [1,7,3,4]
print(get_products_of_all_ints_except_at_index(array))

# this is amazing. doing the n^2 approach in 2 steps