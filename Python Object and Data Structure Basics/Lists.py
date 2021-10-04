my_list = [1,2,3]
my_list = ['STRING', 100,23.2]
print(len(my_list))

new_list = ['one', 'two', 'three']
print(new_list[1:])

another_list = ['four','five']
print(new_list + another_list)

newer_list = new_list + another_list
print(newer_list)

newer_list[0] = 'ONE ALL CAPS'
print(newer_list)

newer_list.append('six')
print(newer_list)

newer_list.append('seven')
print(newer_list)

newer_list.pop()
print(newer_list)

popped_item = newer_list.pop(3)
print(popped_item)

newer_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]
newer_list.sort()

print(newer_list)

my_sorted_list = new_list.sort()

print(type(my_sorted_list))

num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)


