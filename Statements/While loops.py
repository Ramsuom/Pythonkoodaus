x = 50

while x < 5:
    print(f'The current value of x is {x}')
    x = x + 1  #Tämä on parempi muoto
    #x += 1
else:
    print('X is not less than 5')

x = [1,2,3]

for item in x:
    pass

print('end of my script')

mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':  #Tulostaa vaan S kirjaimen
        break
    print(letter)

x = 0
while x < 5:

    if x == 2:
        break   #Lopettaa scriptin 2 numeroon
    print(x)
    x +=1