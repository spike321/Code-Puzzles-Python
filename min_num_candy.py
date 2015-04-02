ratings = [11,2,2,3,4,11,5]
index_lowest = ratings.index(min(ratings))
#min = min(ratings)
#candy = 1
#for x in range(index + 1, len(ratings)):
#    currIndex = x
#    if ratings(currIndex+1)>ratings(currIndex):
#        candy +=

candy = []
neighbour = 1
prev_index = index_lowest
for x in range(index_lowest, len(ratings)):
    if(ratings[prev_index]<ratings[x]):
        neighbour += 1
        prev_index += 1
    candy[x] = neighbour
behind = 1
next_index = index_lowest
for y in range(0, index_lowest):
    if(ratings[index_lowest - y]<ratings[next_index]):
        behind += 1
        next_index -= 1
    candy[index_lowest - y] = behind
print "candy ", candy
print sum(candy)