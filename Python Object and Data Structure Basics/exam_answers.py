# Answer the following questions:
# Numbers: Integers, hole numbers not decimals
#
# Strings: Word
#
# Lists: List where you gather different information and other stuff
#
# Tuples: Starts with (). They cannot be changed
#
# Dictionaries: Need a key and value

#Exam answers
#1.
(60 + (10 ** 2) / 4 * 7) - 134.75

#2.
print(4 * (6 + 5))
print(4 * 6 + 5)
print(4 + 6 * 5)

#3.
#What is the type of the result of the expression 3 + 1.5 + 4?
# float
#What would you use to find a number’s square root, as well as its square?:
#sqrt = number ** 0.5

#Strings
#Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
s = 'hello'
print(s[1])
#Reverse the string 'hello' using slicing:
print (s[::-1])
#Given the string hello, give two methods of producing the letter 'o' using indexing.
print(s[4])
print(s[-1])

#Lists
mylist =  [0,0,0]
print(mylist)
new_list = [0,0]
newer_list = [0]
the_list = new_list + newer_list
print(the_list)
chill_list = [0]*3
print(chill_list)

#2.
list3 = [1,2,[3,4,'hello']]
list3[2][2]='goodbye'
print(list3)

#3.
list4 = [5,3,4,6,1]
#list4.sort()
print(sorted(list4))

#Dictionaries
#Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

# Can you sort a dictionary? Why or why not?
# Answer: No! Because normal dictionaries are mappings not a sequence.

#Tuples
#What is the major difference between tuples and lists?
#Tuples are immutable

#How do you create a tuple?
t = ('one',2,3)
print(t)

#Sets
#What is unique about a set?
#They don't allow for duplicate items!

#Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))

#Booleans
#1. False
# 2. False
# 3. False
# 4. True
# 5. False
# 6. False

# a=3.0
# b=3

print(2 > 3)

print(3 <= 2)

print(3 == 2.0)

print(3.0 == 3)

print(4**0.5 != 2)

l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

print(l_one[2][0] >= l_two[2]['k1'])
#False