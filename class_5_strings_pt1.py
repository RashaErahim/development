''' Strings 

Strings are how we store text in python.
Strings are actually a sequence of characters.
Strings are immutable - this means that if we want to change a string we have to completely remake the string. (More on this next class)

'''

''' Printing 

You have a variable called hours which equals 24, the number of hours in a day.
Print There are 24 hours in a day. Make sure to use your variable.
First, print using commas. Remember that using commas automatically adds spaces!
Now, print using string concatenation. Remember to cast hours to a string and manually add the spaces!


'''
# Commas

# Concatenating

# Formatted Strings

''' Concatenation and Multiplication '''


# Concatenation




'''
Create 2 variables, color_one and color_two, and assign two colors to them as string variables.
Create a 3rd variable called new_color which concatenates the two and displays them connected with a dash. For example 'green' and 'blue' would print as 'green-blue'
'''



# Multiplication




'''
Create a variable called fav_food, and assign a string value of your favorite food. Create a second variable, called result, which multiplies your fav_food variable by 10
'''
fav_food= 'fish'+" "
result=fav_food*10
print(result)

'''
Using the 'in' keyword solve the following

Is 'a' in giraffe?
Is 'z' in birthday?
Is 'w' in wrapper?

'''



'''
Using the len function find the number of characters in the following strings

Pardon
Halloween
Ice Cream
Tank
Laptop
'''




''' Let's try some string methods '''

# capitalize() Converts the first character to upper case



# casefold() Converts string into lower case




# center() Returns a centered string


# count() Returns the number of times a specified value occurs in a string


# Optional Parameters, start and end


# expandtabs() Sets the tab size of the string




# find() Searches the string for a specified value and returns the position of where it was found


# Find position of e in day


# Find position of J in month

# Find the position of R in movie


# Note: Find returns -1 if the character is not in the string

# Find the position of b in movie


# index() Searches the string for a specified value and returns the position of where it was found



# Error if letter doesnt exist



'''
Create a variable called index_of_y and apply the index string method to locate the index position of the letter y.  What happens if we try to locate a letter that does not exist in our string?
'''


''' More string methods '''

# isalnum() Returns True if all characters in the string are alphanumeric (Letters and Numbers)




# isalpha() Returns True if all characters in the string are in the alphabet (Letters only)
word_four ='abcd'
word_five='abcd123'
word_six='^&**(())'
print(word_five.isalpha())
print(word_four.isalpha())
print(word_six.isalpha())



# isdecimal() Returns True if all characters in the string are numbers




# Isdigit
# all characters in the string are digits


# 'a' is not a digit


# isdigit fails if there's whitespace


# it must be at least one char long


# dots '.' are also not digit


''' Is decimal'''
# isdecimal


# negative sign, false

# decimal point, false

# islower() Returns True if all characters in the string are lower case



# print(house_type_lower)

''' Try the islower method to test if the following strings are upper and lower case'''



# isupper() Returns True if all characters in the string are upper case

# isnumeric() Returns True if all characters in the string are numeric






# isspace() Returns True if all characters in the string are whitespaces





# istitle() Returns True if the string follows the rules of a title







# join() Joins the elements of an iterable to the end of the string



# lower() Converts a string into lower case


# Partition - looks for the match and separates into a tuple with before match, match, after match




# replace() Returns a string where a specified value is replaced with a specified value



# split() Splits the string at the specified separator, and returns a list



# # splitlines splits at new line


# startswith() Returns true if the string starts with the specified value


# strip() Returns a trimmed version of the string





# reference vs value equality: == vs is




# What is your name


# Let's shorten our code



# Let's sanitize our string!


'''
Example

Write some code that will take a string from the user and print if it is a number or not.

Examples:
apple
False

4
True

'''





'''
Take a word from the user. Then take a number from the user. Then print whether the word is longer than the number.

Examples:
apple
6
False

python
4
True

Hint: use len() to find the length of the string, and don’t forget to cast to int()

'''




'''
Write some code that takes a string from the user, and prints how many vowels are in the string. (Vowels are a, e, i, o, u)
How will you count both uppercase and lowercase vowels?
What string method can you use to count the number of vowels?

'''





''' Exercise - Challenge

Write some code that will print a box around a string.

Examples:
User input: hello
*******
*hello*
*******

User input: programming is fun
********************
*programming is fun*
********************
Hint: You will have to use the len() function, string concatenation (+), and string multiplication (*)

'''

