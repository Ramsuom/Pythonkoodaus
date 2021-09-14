print('This is a string {}'.format('INSERTED'))
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
print('The {f} {f} {f}'.format(f='fox', b='brown', q='quick'))

result = 100/777
print("The result was {r:1.5f}".format(r=result))

name = "Sam"
age = 3
print(f'Hello, his name is {name}')
print(f'{name} is {age} years old')