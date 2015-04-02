num = [9,1,4,7,3,-1,0,5,8,-1,6]
print "num ", num
list = []
map = {}
for x in num:
    if x in map: map[x] +=1
    else:
        map[x] = 1
        list.append(x)
dict = {x: False for x in list}
#print "list ", list
#print "non repeating list ", list
#print "dict ", dict
#print "map  ", map
#print "length of dict", len(dict)
#print "length of map", len(map)
length = 0
other_length = 0
max1 = 0
for x in list:
    #print "dict[%d] = %d"%(x, dict[x])
    if (x+1 in map and not dict[x]):
        length = length + 1
        dict[x] = True
        #print x
        if length > max1:
            max1 = length
        #print "dict ", dict
    else:
        length = 0
#print max1

map = {}
no_repeat_list = []
for x in num:
    if x in map: map[x] += 1
    else:
        map[x] = 1
        no_repeat_list.append(x)
sort = sorted(no_repeat_list)
length = 1
#print "length of no_repeat_list ", len(no_repeat_list)
#for n in range(len(no_repeat_list)):#**** NEW to access index in for loop
    #print "not if ", n
    #if n+1 <= len(no_repeat_list):
        #print n
        #if (n+1 == no_repeat_list[n+1]):
            #length += 1
        #else:
            #length = 0
#print "length ", length

dict = {x: False for x in num} # False means not visited
print "dict ", dict
maxLen = -1
for i in dict:
    if dict[i] == False:
        print "dict[%d] = %d is not visited" % (i, dict[i])
        curr = i+1; lenright = 0
        print "curr ", curr
        print "lenright ", lenright
        while curr in dict:
            lenright += 1; dict[curr] = True; curr += 1
            print "dict ", dict
        curr = i-1; lenleft = 0
        while curr in dict:
            lenleft += 1; dict[curr] = True; curr -= 1
            print "dict ", dict
        maxLen = max(maxLen, lenleft+1+lenright)
        #print "maxLen ", maxLen
        #print "lenLeft ", lenleft
        #print "lenRight ", lenright
        #print "lenLeft+1+lenRight", lenleft+1+lenright
print maxLen