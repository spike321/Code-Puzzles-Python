import collections
import string

word = "aacbbcabcddaaababcdzabzdcdddddddddddd"

#--------------------------------------------------------------------------
dict = {c: 0 for c in word}
print (dict)

for c in word:
    dict[c] += 1
print dict

#not sorted, need sorted string, below
st = ""
for key,val in dict.iteritems():
    st = st + key + str(val)
print (st)
#----------------------------------------------------------------------------
d = collections.defaultdict(int)
print (d)
for c in word:
    d[c] += 1
print (d)
st2 = ""
for c in sorted(d, key=d.get, reverse=False):
    print '%s %6d' % (c, d[c])
    st2 = st2 + c
print ("st2", st2)
#above is the final solution, it took a sting, converted to dict, sorted by freq, convert it back to string
#----------------------------------------------------------------------------
    #sorted_dict[c] = d[c]
#sorted_dict = {c:d[c] for c in sorted(d, key=d.get, reverse=True) }
#print (sorted_dict)

#----------------------------------------------------------------------------
char_counter = collections.Counter(word)
print (char_counter)

for key in char_counter:
    print key

for char, count in char_counter.most_common():
    if char in word:
        print(char, count)
#-----------------------------------------------------------------------------

