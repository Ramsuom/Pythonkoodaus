mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print('hello')

for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')

list_sum = 0

for num in mylist:
    list_sum = list_sum + num

    print(list_sum)

mystring = 'Hello world'
for letter in mystring:
    print('Nice')

tuple = (1,2,3)

for item in tuple:
    print(item)

mylist = [(1,2),(3,4),(5,6),(7,8)]
print(len(mylist))

for a,b in mylist:
    print(a)
    print(b)

lista = [(1,2,3),(4,5,6),(7,8,9)]
for (a,b,c) in lista:
    print(c)

d = {'k1':1,'k2':2, 'k3':3 }

for value in d.values():
    print(value)
