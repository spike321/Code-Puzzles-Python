#sorting a string in alphabetical order

value = "boat"
print value
list = [c for c in value]#NEW convert a string into a list of characters.
print c
print list
list.sort()
#join the characters back together into a string
result = "".join(list)
print(result)

num = [1,44,6,8,44,5,3,44,5,44,44,5,44,8,9]
print num
#dictionary = {num, 0}
#for x in range num:
#    dictionary[x] += 1
#print(dictionary)
sorted_num = sorted(num)
#print sorted_num
length = len(sorted_num)
#print length

list = [] #empty list
total = sum(num)#adding a list of numbers
#print total
mean = total/length
#print mean
tally = []
for item in sorted_num:
    tally.append(sorted_num.count(item))
#print tally
mode = max(tally)

hits = []
tally = []
for item in num:
    tally = num.count(item)#count counts the number of times that specific item occurs in a list
    values = (tally, item)#***NEW i think this is a tuple
    #print values
    if values not in hits:#***NEW if statement
        hits.append(values)#***NEW i think this is a list of tuples
        print hits
hits.sort(reverse=True)
#print hits
mode = hits[0][1]#***NEW you can refer to a list of tuples like this
num_times_mode_appeared = hits[0][0]


