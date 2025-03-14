
''' Strings Part 2'''

# Strings are immutable

# Just applying the method to the string won't change the original value



'''Indexing, with square brackets'''




# Create a variable to capture the first letter of this string



# Grab the last letter in a variable




# Using the length and bracket notation, access the last letter in the variable below


# Using bracket notation access the letter x, the letter e, and the letter d 
first_name = 'Alexandra'
letter_x = first_name[3]
letter_e=first_name[2]
letter_d=first_name[6]
print(letter_x)
print(letter_e)
print(letter_x)
# print(letter_x)




'''Reverse indexing'''



# Using bracket notation and reverse indexing, access the letter g, the letter i, the letter p



''' Slicing '''
# There are 3 parameters available with indexing with bracket notation [start:stop:step]



# Using slicing please create a string that accesses 'rica' in 'America'




# Using slicing please create a string that accesses 'ora' in 'Dora the explorer'


# Using slicing please create a string that accesses 'explo' in 'Dora the explorer'


# Using slicing please create a string that accesses 'albo' in 'Rocky Balboa'
boxer = 'Rocky Balboa'
# print(boxer[7:11])



# Let's step through this string 2 characters at a time
superheroine = 'Wonder Woman'
print(superheroine[::2])

# Lets step through this entire word and skip by 4
word = 'Supercalifragilisticexpialidocious'


'''Slicing in reverse 
Refer to slice image as a guide if needed

'''


'''

D A Y C A R E
0 1 2 3 4 5 6


D   A   Y   C   A   R   E
-7 -6  -5  -4  -3  -2  -1

'''
random_word = 'daycare' 

# Fun with reverse indexing




'''
Write some code to print the second half of a string.
Example:
python
hon
'''





# End Parameter


# Sep Parameter


'''
Get input from the user and store it in a variable called userin.
Then print the user input. The output should follow exactly this format, including the colon and period at the end:
You entered: userin.
Where userin is what you got from the user.
You must format the print statement like this:
print("You entered",userin)
How can you add sep and end keywords to get the exact formatting shown above?
'''


'''
You need to write a script that will generate an email to a customer who has just made a purchase. You have 3 variables:
name, which stores the customer's name as a string
product, which stores the product name as a string
price, which stores the price of the product as a float
Use an f-string to generate an email message with the following text, and print it. Make sure to round the price to 2 decimal places. The email should be one multi-line string.
Dear {name},
Thank you for your purchase of a {product}. Your credit card has been charged ${price}.
We appreciate your business and look forward to serving you again.
Sincerely,
The ABC Company
'''

name = 'Josiah Wilson'
product = 'ABC Sneakers'
price = 74.95343452342





'''
Write some code that takes a string and tells if it is a palindrome (same forwards and backwards).
Hint: Use indexing/slicing and boolean expressions

Examples:
racecar: True
cat: False
'''

