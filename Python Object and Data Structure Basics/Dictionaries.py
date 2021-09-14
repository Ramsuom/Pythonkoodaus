my_dict = {'key1':'value1','key2':'value2'}
print(my_dict)    #Luodaan lista

prices_lookup = {'apple':2.99,'oranges':'1.99','milk':'5.80'}
print(prices_lookup['milk'])    #Tulostaa listan

d = {'k1':123,'k2':[0,1,2],'k3':{'insideKey':100}}
print(d['k3']['insideKey'])
print(d['k2'][2])   #Tulostaa yhden arvon listasta

c = {'key1':['a','b','c']}
print(c)
print(c['key1'][2].upper()) #Tulostaa yhden isolla kirjaimella

mylist =c['key1']
print(mylist)
letter = mylist[2]
print(letter.upper())  #Voi tulostaa isolla kirjaimella

a = {'k1':100,'k2':200}     #Lisää key valuen
a['k3']=300
print(a)
a['k1']='NEW VALUE'  #Lisää uuden arvon
print(a)


b = {'k1':100,'k2':200,'k3':300,}
print(b.keys())   #Tulostaa avaimen
print(b.values()) #Tulostaa arvon
print(b.items()) #Tulostaa itemin