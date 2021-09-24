def myfunc(a,b,c=0,d=0,e=0):
    #Returns 5% of the sum a and b
    return sum((a,b,c,d)) * 0.05

print(myfunc(40,60))

print(myfunc(40,60,100))

print(myfunc(40,60,100,100))

def myfunc(*args):  #args esimerkki miten tämä tehdään samalla tavalla
    return sum(args) * 0.05

print(myfunc(40,60))

print(myfunc(40,60,10))

print(myfunc(40,60,100,1,34))

def test(*args):
    for item in args:
        print(item)

print(test(40, 60, 100, 1, 34))

def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choise is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

print(myfunc(fruit='apple',veggie = 'lettuce'))

def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))

print(myfunc(10,20,30,fruit='orange',food='eggs',animal='dog'))