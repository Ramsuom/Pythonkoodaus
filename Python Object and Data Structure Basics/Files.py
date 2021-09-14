myfile = open('C:\\Users\\Rami\\Documents\\myfile.txt')  #avataan tiedosto
print(myfile.read())  #Luetaan tiedosto
print(myfile.readlines())  #Luetaan tiedosto
myfile.close()

with open('readme.txt', 'w') as f:  #Luodaan uusi tiedosto
    f.write('Create a new text file!')

with open('readme.txt', 'r') as f:  #Luetaan uusi tiedosto
    print(f.read())

with open('readme.txt', 'a') as f:   #Lisätään uusi lause
    f.write('\nUUSI LAUSE!!!!')

with open('readme.txt', 'r') as f:   #Luetaan uusi tiedosto
    print(f.read())

with open('uusitiedosto.txt', 'w') as f:  #Luodaan uusi tiedosto
    f.write('I CREATED THIS FILE!')

with open('uusitiedosto.txt', 'r') as f:   #Luetaan uusi tiedosto
    print(f.read())
