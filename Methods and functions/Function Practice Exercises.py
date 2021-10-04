#1. LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        if b < a:
            return b
        else:
            return a
    else:
        if a < b:
            return b
        else:
            return a
    pass

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))

#2. ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(text):
    first_word = text.split(" ")[0].lower()
    second_word = text.split(" ")[1].lower()
    if first_word[0] == second_word[0]:
        return True
    else:
        return False
    pass

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))

#3.MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False¶
def makes_twenty(n1,n2):
    if n1 == 20 or n2 == 20:
        return True
    elif n1 + n2 == 20:
        return True
    else:
        return False
    pass

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))

#LEVEL 1 PROBLEMS
#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
    letters = list(name)
    for index in range(len(name)):
        if index == 0:
            letters[index] = letters[index].upper()
        elif index == 3:
            letters[index] = letters[index].upper()
    return "".join(letters)
    pass

print(old_macdonald('macdonald'))

#MASTER YODA: Given a sentence, return a sentence with the words reversed
def master_yoda(text):
    return ' '.join(text.split()[::-1])
    pass

#print([word[0] for word in st.split()])

print(master_yoda('I am home'))
print(master_yoda('We are ready'))

#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
    return 90 <= n <= 110 or 190 <= n <= 210
    pass

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

#LEVEL 2 PROBLEMS
#FIND 33
# def has_33(nums):
#     for i in range(len(nums)-1):
#         if nums[i:i+2] == [3,3]:
#             return True
#     return False
#     pass
#
# print(has_33([1, 3, 3]))
# print(has_33([1, 3, 1, 3]))
# print(has_33([3, 1, 3]))
# print(has_33([3, 3, 2]))

#PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# def paper_doll(text):
#     return ''.join([c*3 for c in text])
#     pass
#
# print(paper_doll('Hello'))
# print(paper_doll('Mississippi'))

#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'¶
# def blackjack(a,b,c):
#     Ace_count = [a,b,c].count(11)
#
#     total = sum([a,b,c])
#
#     if total <= 21:
#         return (total)
#
#     while total > 21:
#         if Ace_count > 0:
#             Ace_count -= 1
#             total -= 10
#         else:
#             return 'Bust'
#     return (total)
#     pass
#
# print(blackjack(5,6,7))
# print(blackjack(9,9,9))
# print(blackjack(9,9,11))
# print(blackjack(11,11,11))

# #SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.¶
# def summer_69(arr):
#     copyoflist = arr[:]  # makes shallow copy of list
#     while True:
#         if 6 not in copyoflist:
#             return sum(copyoflist)
#
#         indexof6 = copyoflist.index(6)
#         indexof9 = copyoflist.index(9, indexof6 + 1)  # begin search for 9 after 6
#         del copyoflist[indexof6:indexof9 + 1]
#     pass
#
# print(summer_69([1, 3, 5]))
# print(summer_69([4, 5, 6, 7, 8, 9]))
# print(summer_69([2, 1, 6, 9, 11]))

#CHALLENGING PROBLEMS
#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order¶
# def spy_game(nums):
#     flag = False
#     flag_a = False
#     for n in nums:
#         if (n==0 and flag is True):
#             flag_a = True
#             continue
#         elif (n==0):
#             flag = True
#             continue
#         elif (n==7 and flag_a is True):
#             return True
#     return False
#     pass
#
# print(spy_game([1,2,4,0,0,7,5]))  #True
# print(spy_game([1,0,2,4,0,5,7]))  #True
# print(spy_game([1,7,2,0,4,5,0]))  #False
#
# #Another way to do this
# def vakooja_peli(arr:list, segment:list = [0,0,7]) -> bool:
#     l = len(segment)
#     for el in arr:
#         if (el == segment[0]):
#             segment = segment[1:]
#         if(len(segment) == 0):
#             return True
#     return False
#     pass
#
# print(vakooja_peli([1,2,4,0,0,7,5]))  #True
# print(vakooja_peli([1,0,2,4,0,5,7]))  #True
# print(vakooja_peli([1,7,2,0,4,5,0]))  #False

#COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# def count_primes(num):
#     counter = 0
#     for n in range(2,num+1):
#         prime=True
#         for i in range(2,n):
#             if(n%i == 0):
#                 prime=False
#                 break
#         if prime:
#             counter += 1
#     return counter
#     pass
#
# print(count_primes(100))

# def print_big(letter):
#     result_str="";
#     for row in range(0,7):
#         for column in range(0,7):
#             if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
#                 result_str=result_str+"*"
#             else:
#                 result_str = result_str + " "
#         result_str=result_str+"\n"
#     print(result_str);
#     pass
#
# #print(print_big)