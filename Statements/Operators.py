mylist = [1,2,3]
for num in list(range(0,11,2)):
    print(num)

index_count = 0
word = 'abcde'

for letter in word:
    print(word[index_count])
    index_count += 1

for item in enumerate(word):
    print(item)
    index_count += 1

for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

mylist1 = [1,2,3,4,5,6]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]
for item in zip(mylist1,mylist2,mylist3):
    print(item)

mylist1 = [1,2,3,4,5,6]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]
for item in zip(mylist1,mylist2,mylist3):
    print(list(zip(mylist1,mylist2)))

mylist1 = [1,2,3,4,5,6]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]
for a,b,c in zip(mylist1,mylist2,mylist3):
    print(b)

print('x' in [1,2,3])
print('x' in ['x','y','z'])
print('a' in 'a world')
print('mykey' in {'mykey':345})
d = {'mykey':345}
print('d' in {'mykey':345})
print(345 in d.values())
print(345 in d.keys())

mylist = [10,20,30,40,100]
print(min(mylist))
print(max(mylist))

from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)
print(mylist)

from random import randint
print(randint(0,100))

mynum = randint(0,10)
print(mynum)

result = print(input('What is your name: '))
#print('Moi ' + result)

