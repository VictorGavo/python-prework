# Question 1:
# Write a function to print "hello_USERNAME!" USERNAME is the input of the
# function.

def hello_name(user_name):
    print(f"hello_{user_name.upper()}!")

hello_name(input("Please enter your username: "))


# Question 2:
# Write a python function, first_odds that prints the odd numbers from 1-100 and
# returns nothing

def first_odds():
    for i in range(1,101):
        if i % 2 == 1:
            print(i)

first_odds()


# Question 3:
# Please write a Python function, max_num_in_list to return the max number of a 
# given list.


def max_num_in_list(a_list):
    a_list.sort()
    return a_list.pop()

ex_list = [9, 2, 1, 3, 5, 8, 120, 54, 32, 18, 88, 0]
ex_1_list = [1, 1, 1, 88, 1, 1, 1, 2, 5, 3, 1, 1, 1]
print(max_num_in_list(ex_list))
print(max_num_in_list(ex_1_list))


# Question 4:
# Write a function to return if the given year is a leap year. A leap year is 
# divisible by 4, but not divisible by 100, unless it is also divisible by 400.
# The return should be boolean Type (true/false)


def is_leap_year(a_year):
    is_leap = False
    if a_year % 400 == 0 and a_year % 100 == 0:
        is_leap = True
    elif a_year % 4 == 0:
        is_leap = True
    return is_leap

print(is_leap_year(int(input("Enter a year: "))))


# Question 5:
# Write a function to check to see if all numbers in list are consecutive 
# numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are 
# not consecutive numbers. The return type should be boolean Type.


def is_consecutive(a_list):
    consec = True
    index = a_list[0]
    for item in a_list:
        if item != index:
            consec = False
            break
        index += 1
    return consec
    

list_1 = [1,2,3,4,5]
list_2 = [5,6,7,8,9]
list_3 = [10,11,12,15,16,17]
        
print(is_consecutive(list_1))
print(is_consecutive(list_2))
print(is_consecutive(list_3))
