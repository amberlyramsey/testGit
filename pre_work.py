# question 1: Write a function to print "hello_USERNAME!"
def hello_name(user_name):
    """Print a simple greeting to a user."""
    for user in user_name:
        print("hello_" + user_name.upper() + "!")
        break
hello_name('username')

# question 2: Write a python function, first_odds that
# prints the odd numbers from 1-100 and returns nothing.
def first_odds(start, end):
    """
    Print a list of odd numbers 1-100, returning no value.
    """
    for num in range(1,101):
        if num % 2 != 0:
            print(num)
            return
first_odds(1, 101)

# question 3: Please write a Python function, to return the max number of a given list.
def max_num_in_list(a_list):
    """Return the max number in a given list."""
    for max_num in max(a_list):
        print("This is the highest value: " + max_num)
        return a_list
m = list(range(1,6))
max_num_in_list(str(max(m)))

# question 4: Write a function to return if the given year is a leap year.
def is_leap_year(a_year):
    """Return a true/false statement for a given year."""
    leap = False
    if a_year % 400 == 0:
        leap = True
    elif a_year % 4 == 0 and a_year % 100 != 0:
        leap = True
    return leap
a_year = int(input("What year would you like to check? "))
print(is_leap_year(a_year))

# question 5: Write a function to check to see if all numbers in list are consecutive numbers.
def is_consecutive(a_list):
    """
    Write a function to check to see if all
    numbers in list are consecutive numbers.
    """
    return sorted(a_list) == list(range(min(a_list), max(a_list) + 1))
lst = [1, 2 , 2, 8, 5, 3]
print(is_consecutive(lst))
con_num = [1, 2, 3, 4]
print(is_consecutive(con_num))