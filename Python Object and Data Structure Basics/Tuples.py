t = ('one',2,3)
mylist = [1,2,3]
print(type(t)) #Tulostaa tyypin
print(type(mylist))
print(len(t)) #Tulostaa pituuden
print(t)
print(t[0]) #Tulostaa ensimmäisen arvon
mylist[0] = 'NEW'
print(mylist)
# t[0] = 'NEW'
# print(t)  #Tuplen lisääminen ei onnistu

u = ('a','a','b')
print(u.count('a')) #Laskee montako on
print(u.index('a')) #Näyttää missä kohtaa listassa on
print(u.index('b'))