from collections import Counter
num = [1, 1, 1,  2, 3, 3,3 ,3 ]
#print num
occurrence = len(num)//2
#print occurrence

d = Counter(num)
#print d
d.most_common()


list = []
for item in num:
    list.append(num.count(item))
#print list
#mode = num[max(list)]
#print mode

for x in list:
    if x>=occurrence:
        answer = num[list.index(x)]
#print answer
#print list

max = len(num)//2
for item in num:
    if num.count(item)>=max:
        answer = item
    break


maj = len(num)//2
#print maj
map = {}
max = 0
for x in num:
    if x in map:
        map[x] += 1
        if map[x] > max:
            max = x
    else:
        map[x] = 1
#print map
#print max


#accepted solution:
myMap = {}#dictionary
maximum = ( '', 0 ) # (occurring element, occurrences) tuple
for n in num:
    if n in myMap: myMap[n] += 1
    else: myMap[n] = 1

    # Keep track of maximum on the go
    if myMap[n] > maximum[1]: maximum = (n,myMap[n])

print "tuple  ", maximum
print "tuple[0]  ", maximum[0]
print "tuple[1]  ", maximum[1]
print "map  ", myMap
print "map[1]  ", myMap[1]
print "map[2]  ", myMap[2]
