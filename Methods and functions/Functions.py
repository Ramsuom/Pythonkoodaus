def say_hello(name='Default'):
    print(f'Hello {name}')

say_hello('Rami')

def add_num(num1,num2):
    return num1+num2

result = add_num(10,20)
print(result)

def print_result(a,b):
    print(a+b) #Tulostaa None arvon

print(print_result(20,20))

def return_result(a,b):
    return a+b

result = return_result(30,20)

print(result)

def myfunc(a,b):
    print(a+b)
    return a+b

result = myfunc(40,20)

def sum_numbers(num1,num2):
    return num1+num2

print(sum_numbers('10','20'))