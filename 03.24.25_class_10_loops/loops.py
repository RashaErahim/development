

''' While Loops

While loops run as long as the given condition returns a True boolean.

'''

''' Example
Create a while loop that prints every integer from 1 to 10.
'''







# we can choose our end point. our starting point is 0. We will count up by one and display it to the user as long as start is less than end.



# Let's create and infinite loop, a condition we will never see fulfilled, kill your terminal with ctrl + c





''' While loops and user input 

This will keep asking us to input a word until we input "stop" Let's follow it line by line

'''




'''
Improve the login system to allow multiple attempts. You're developing a login system for a website. Write a Python program that checks whether the user has entered the correct username and password. Just like before:
Create two variables called username and password.
Prompt the user to enter their username and password.
Use conditionals and logical operators to check whether the username and password entered by the user match the username and password variables.
As long as the username and password are incorrect, print “Incorrect username or password”, and keep asking the user for their username and password.
If they match, print “Login successful” and end the program.
'''






	




''' For Loops
For loops are used to iterate through something.
For loops perform an action on a group of objects
For loops can be performed on iterables: 

Strings
Lists
Tuples
Dictionaries
Sets

# The Temporary Variable (item, goes out of scope after for loop ends)
for item in collection:
	print(item)

'''

'''
Lets loop through the string "Hello World"

'''



'''
Lets loop through a list of colors
# my_colors = ['red', 'green', 'orange', 'yellow']
'''

'''Lets loop through a tuple

'''



'''
Example
Write a for loop that loops through a string, counts all the letters, and then print how long the string is.

'''


    


'''
Exercise - Lets try to add conditionals to the mix

Take a string from the user. Verify that it’s a number.
Write a for loop that adds all the digits together. Then print the total.

Example:
'14253'
15

Hint: remember to cast to int() for each digit in the loop

'''
userinput=input('please inter a number').isdigit
count=0
for n in userinput:
    count +=userinput
    
print(n)




''' More conditionals in loops'''




''' Cleaning Strings

You’re working on a data analysis project for a company that looks at written text. You’re only interested in letters from A-Z because you’re analyzing language. However, the data you’re given has some values that shouldn’t be there.
Write a Python program that takes a string as input from the user, removes anything from the string that isn’t a letter, and prints the new string.
You can loop through the string in a for loop, use the .isalpha() string method, and remember that strings are immutable, so you will have to build a new string from scratch using string concatenation.

test_string = 'a56b32ra87ca++d#@a*&b21r23a'

'''






# Which numbers are even??
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


