import random
import os
import sys

name = "Sahiti"
print(name)
# 5 main data types:
# Number,s Strings, Lists, Tuples, Dictionaries
# ** exponential, 5**2 = 25 = 5^2
# // floor division, discard the remainder, 5//2 = 2, it truncates

#String
Var = "\" lalala"
multi_line_quote = '''abc
def'''
adding_strings = Var + multi_line_quote
print("%s %s %s" % ('stuff' , Var, multi_line_quote))
# getting rid of the new line at the end
sys.stdout.write('i dont like ')
print("new lines")
#print 5 new lines
print('\n' * 5)

#Lists
grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
print('First Item: ', grocery_list[0])
print(grocery_list[1:3])#only prints index 0, 1, 2 , not inclusing 3
other_events = ['Wash Car', 'Pick up kids', 'Cash Check']
to_do_lists = [other_events, grocery_list]
print(to_do_lists)
print(to_do_lists[1][1])#print second item in second list
grocery_list.append('Onions')
print(to_do_lists)
grocery_list.insert(1, "Pikle")
grocery_list.remove("Pikle")
grocery_list.sort()
grocery_list.reverse()
del grocery_list[4]
print(to_do_lists)
to_do_list2 = other_events + grocery_list
print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))


#Tuples
#Unlike lists, we can't change Tuples after created
#Tuples are surronded by () like a Ball
#sometimes you dont want data to be changed
pi_tuple = (3,1,4,1,5,9)
convert_to_list = list(pi_tuple)#converting tuple into a list
convert_to_tuple = tuple(pi_tuple)
length = len(pi_tuple)
maximum = max(pi_tuple)
minimum = min(pi_tuple)

#Dictionaries or Maps
# you cannot join dictionaries together like lists
#use curly brace
super_heros = {'Sahiti' : 'Super Woman',
               'lady bug' : 'daboda',
               'x-men' : 'rejects'}
print(super_heros['x-men'])
del super_heros['lady bug']
super_heros['x-men'] = 'assholes'
print(len(super_heros))
print(super_heros.get("Sahiti"))
print(super_heros.keys())
print(super_heros.values())


#for loops
for x in range(0, 10):
    print(x, ' ')
print('\n')
for y in grocery_list:
    print(y)
for x in [2,4,6,8,10]:
    print(x)
num_list = [[1,2,3,], [4,5,6], [7,8,9]]
for x in range (0,3):
    for y in range(0,3):
        print(num_list[x][y])

#while loops
#use it when you have no idea ahead of time how many times you have to loop
rand_num = random.randrange(0,100)
while(rand_num != 15):
    print(rand_num)
    rand_num = random.randrange(0,100)
i = 0
while(i<=20):
    if(i%2==0):
        print(i)
    elif(i==9):
        break
    else:
        i += 1
        continue

    i += 1

#functions
def addnums(fNum, lNum):
    sumNum = fNum + lNum
    return sumNum

print(addnums(1, 4))
string = addnums(1,4)

#input
print('What\'s your name')
name = sys.stdin.readline()
print('Hello', name)

#strings
long_string = "I'll catch you if you fall - The Floor"
print(long_string[0:4])#its not going to print out the 4th index
print(long_string[-5:])#pritn the last 5 characters
print(long_string[:-5])#print everything except the last 5 characters of the string
print(long_string[:4] + " be there")#print the first 4 chars and another string
print("%c is my %s letter and my number %d number is %.5f" %
('X', 'favorite', 1, .14))#%.5f means, print 5 decimal places
print(long_string.capitalize())#captilize the first letter
print(long_string.find("Floor"))#returns the index number of where Floor starts, case sensitive
print(long_string.isalpha())#make sure everthign is letter
print(long_string.isalnum())
print(len(long_string))
print(long_string.replace("Floor", "Ground"))
print(long_string.strip())#strip white space
quote_list = long_string.split(" ")#split a string into a list
print(quote_list)

#FileIO
test_file = open("test.txt" , "wb")#create or opena  file
#if you want to write to the file, send "wb" as a command
#use "ab+" to read & append to file
print(test_file.mode)
print(test_file.name)
#test_file.write(bytes("Write me to the file\n", 'UTF-8'))
test_file.write("Write me to the file\n")
test_file.close()
print("file has been closed")
#how to read info from file
test_file = open("test.txt",  "r+")# reading and writing
test_in_file = test_file.read()
print(test_in_file)
test_file.close()
os.remove("test.txt")

#objects
class Animal( object):
    __name = None # or use can use __name = ""
    __height = 0
    __weight = 0
    __sound = 0#double underscores are private attributes,
    #inorder to change private attributes, use func inside of the class

#constructor
    #constructor is called to setup or define the object
    #when an obj is created we demand all the values to be passed in here
    #when the values are passed in, we want them to be defined
    def __init__(self, name, height, weight, sound):
        self.__name = name#you are initializing those values
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):#this is called encapsulation
        self.__name = name#encapsulation, is the name passed in here valid, if it is, we will set it
    #we do the check here inself
    def get_name(self):
        return self.__name
    def set_height(self, height):
        self.__height = height
    def get_height(self):
        return self.__height
    def set_weight(self, weight):
        self.__weight = weight
    def get_weight(self):
        return self.__weight
    def set_sound(self, sound):
        self.__sound = sound
    def get_sound(self):
        return self.__sound

#polymorphism
    def get_type(self):
        print("Animal") #will print the class name

    def toString(self):#because you are inside a class you dont need to use getters and setters
        return "{} is {} cm tall and {} kg and says {}".format(self.__name, self.__height, self.__weight, self.__sound)

    #create an object called cat
cat = Animal('Whiskers', 33, 10, 'Meow')
print(cat.toString())

#inheritance
    #whenever you inherit from another class, you automatically get all the attributes and methods from the class you are inheriting from.
class Dog(Animal):
        __owner = ""
    #constructor
        def __init__(self, name, height, weight, sound, owner):
            #Animal.__init__(self, name, height, weight, sound)
            self.__owner = owner
            super(self.__class__, self).__init__(name, height, weight, sound)#letting the super classes initialization for the rest of the values, because they are already defined there

        #setter for owner
        def __set_owner(self, owner):
            self.__owner = owner

        def get_owner(self):
            return self.__owner
        #getter for owner
        def get_type(self):
            print("Dog")

        def toString(self):#Overriding: creating the same method name in the subclass and rewriting the method
            return "{} is {} cm tall and {} kg and says {}. His owner is {}".format(self.__name, self.__height, self.__weight, self.__sound, self.__owner)

#method Overloading
    #albe to perform different tasks based off of the attributes that are sent in

        #function with multiple sounds
        def multiple_sounds(self, how_many=None):#attribute how_many time should a dog bark, but because it is set to None, when calling this method, no need to pass in this attribute
            if how_many is None:
                print(self.get_sound())
            else:
                print(self.get_sound() * how_many)
        #REMEMBER indentation, colons, and diffrence between single and double quotes

spot = Dog("Spot", 53, 27, "ruff", "Derek")
print(spot.toString())

#polymorphism
class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()

test_animals = AnimalTesting()
test_animals.get_type(cat)
test_animals.get_type(spot)

spot.multiple_sounds(4)
spot.multiple_sounds()