# print(2 % 2)
#
# print(3 % 2)
#
# print(41 % 40)
#
# print(20 % 2)
#
# print(20 % 2 == 0)
#
# print(21 % 2 == 0)

def even_check(number):
    return number % 2 == 0

print(even_check(20))

# Return true if any number is even inside the list
def check_even_list(num_list):
    #return all the even numbers in a list

    #Placeholder variables
    even_numbers = []

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass

    return even_numbers

print(check_even_list([1,2,3,4,5]))

print(check_even_list([1,3,5]))
#
# print(check_even_list([2,4,5]))
#
# print(check_even_list([2,1,1,1]))
#
# print(check_even_list([1,1,1,2]))