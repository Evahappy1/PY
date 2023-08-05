# name = input('whats your name:')
# print('welcome:', name)


# a = int(input('insert number'))
# b = int(input('insert number'))
# print(a+b)

# # 1. The volume of a sphere with radius r is (4/3πr3). what is the volume of a sphere with radius 5?
# b = 22/7
# a = 4/3
# r = 5**3
# print(a * b * r)
# 2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
# cp = 24.95
# disc = 60/100 * 24.95
# # first copy $3
# sc = 0.75
# x = 60
# z = (x - 1)*sc
# y = z + 3
# print(y + disc)






# 3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast? 
 
# easy_pace = 8 * 60 + 15
# tempo = 7 * 60 +12
# total_time = (easy_pace * 2) + (tempo * 3)
# total_time_min = total_time //60
# total_time_sec = total_time % 60


# departure_time = (6 * 60 )+ 52
# breakfast_time_hour = (departure_time + total_time_min) //60
# breakfast_time_min = (departure_time + total_time_min) % 60
# print(f'{breakfast_time_hour}: {breakfast_time_min}:{total_time_sec}')

# print(f'{total_time_min}:{total_time_sec}')



# 25/7/2023
# Function exercises 
# 1. Write a function named right_justify that takes a string named s as a parameter
# and prints the string with enough leading spaces so that the last letter of the string is in column 70
# of the display.
# >>> right_justify('monty')
#                                                                                                                            monty
# Hint: Use string concatenation and repetition. Also, Python provides a built-in function called len
# that returns the length of a string, so the value of len('monty') is 5

# def right_justify(s):
    #  print(' ' * 69 + s)

# right_justify('monty')

     


#     2. A function object is a value you can assign to a variable or pass as an argument. For
# example, do_twice is a function that takes a function object as an argument and calls it twice:

# def do_twice(f):
# f()
# f()

# Here’s an example that uses do_twice to call a function named print_spam twice.

# def print_spam():
# print('spam')

# do_twice(print_spam)

# 1. Type this example into a script and test it.
# 2. Modify do_twice so that it takes two arguments, a function object and a value, and calls the
# function twice, passing the value as an argument.
# 3. Copy the definition of print_twice from earlier in this chapter to your script.
# 4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an
# argument.
# 5. Define a new function called do_four that takes a function object and a value and calls the
# function four times, passing the value as a parameter. There should be only two statements in
# the body of this function, not four.
# 1. Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |	 |	 |
# |	 | 	 |
# |	 |	 |
# |	 |  	 |
# + - - - - + - - - - +
# |	 |	 |
# |	 | 	 |
# |	 |	 |
# |	 | 	 |
# + - - - - + - - - - +
# Hint: to print more than one value on a line, you can print a comma-separated sequence of
# values:
# print('+', '-')
# By default, print advances to the next line, but you can override that behavior and put a
# space at the end, like this:
# print('+', end=' ')
# print('-'


# def do_twice(f, obi):
#  f(obi)
#  f(obi)
    

# Here’s an example that uses do_twice to call a function named print_spam twice.

# def print_spam():
    # print('spam')

# do_twice(print, "fgjddffjf")


# def print_twice(bruce):
    # print(bruce)
    # print(bruce)


# print_twice('spam')


# print_twice(42)

# def cat_twice(part1, part2):
    # cat= part1 + part2
    # print_twice(cat)

# line1 ='Bing tiddle'
# line2 = 'tiddle bang.'
# cat_twice(line1, line2)

# def do_four(y, vio):
#    do_twice(y, vio)
#    do_twice(y, vio)
   
   
   

# do_four(print, "Engr")


# 1. Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |	 |	 |
# |	 | 	 |
# |	 |	 |
# |	 |  	 |
# + - - - - + - - - - +
# |	 |	 |
# |	 | 	 |
# |	 |	 |
# |	 | 	 |
# + - - - - + - - - - +
# Hint: to print more than one value on a line, you can print a comma-separated sequence of
# values:
# print('+', '-')
# By default, print advances to the next line, but you can override that behavior and put a
# space at the end, like this:
# print('+', end=' ')
# print('-'


# SOLUTION
# def draw_grid_plus():
#         print('+', '-'*4, '+', '-'*4, '+')

# def draw_grid_column():
#         print('|', ' '*4, '|', ' '*4, '|')

# def draw_grid():
#         draw_grid_plus()
#         draw_grid_column()
#         draw_grid_column()
#         draw_grid_column()
#         draw_grid_column()
#         draw_grid_plus()
#         draw_grid_column()
#         draw_grid_column()
#         draw_grid_column()
#         draw_grid_column()
#         draw_grid_plus()


# draw_grid()

# OR
def do_twice(f):
    f()
    f()
    
    def do_4xs(f):
        do_twice(f)
        do_twice(f)

    def print_first():
        print('+', end = ' ')
        print('-'*4, end = ' ')

        def print_complete():




# 27/7/2023

# Write a program to create a function show_employee() using the following conditions. It should accept the employee’s name and salary and display both. If the salary is missing in the function call then assign default value 9000 to salary
# SOLUTION

# def show_employee(name, salary):
    
#     name = ('employer')

#     salary = (9000)
#     salary = 9000

# print(show_employee)

# Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.

# SOLUTION

# def calculation(a, b): 
#  # Your Code 
#   plus = int(input('insert number'))
#   minus = int(input('insert number'))
# print(a+b)

#  res = calculation(40, 10)
#   print(res)

# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10
# A recursive function is a function that calls itself again and again.
# Expected Output:55
# SOLUTION

def down_count(n):