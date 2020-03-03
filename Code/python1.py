#!/usr/bin/env python3	
def one(input1, input2):
	st1 = len(input1)
	st2 = len(input2)
	if len(input1)> len(input2):
		return input1
	elif len(input2)> len(input1):
		return input2
	else:
		return input1+" "+input2
	

	# <QUESTION 2>

    # Return the string that is between the first and last appearance of "bert" in the given string
	
	# Return the empty string "" if there is not 2 occurances of "bert" 
	
	# IGNORE CASE
    
    # <EXAMPLES>


	# <HINT>

	# What was the name of the function we have seen to seperate a String? How can we make a string all upper or lower case?
	
	# Use your CLI to access the Python documentation and get help manipulating strings - help(str).

def two(input):
	string = input
	stren = ''
	for i in range(len(string)):
		if 'bert' in string.lower():
			stren = string[i]+string[i+1]+string[i+2]+string[i+3]
			stren = stren.lower()
		if stren == 'bert':
			string = string[i+4:]
			break
	if 'bert' in string.lower():
		for i in range(len(string)):
			stren = string[i]+string[i+1]+string[i+2]+string[i+3]
			stren = stren.lower()
			if stren == 'bert':
				string = string[:i]
				break
            
	else:
		string = ''

	#string = string[::-1]
	return string




	# <QUESTION 3>

    # given a number
	# if this number is divisible by 3 return "fizz"
	# if this number is divisible by 5 return "buzz"
	# if this number is divisible by both 3 and 5 return "fizzbuzz"
	# if this number is not divisible by 3 or 5 return "null"
	    
    # <EXAMPLES>



	# <HINT>

	# No Hints for this question

def three(arg1):
	if arg1%15==0:
		return 'fizzbuzz'
	elif arg1 % 3 == 0:
		return 'fizz'
	elif arg1 % 5 == 0:
		return 'buzz'
	else:
		return "null"


	# <QUESTION 4>

    # Given a string seperate the string into the individual numbers present, then add each digit of each number to get a final value for each number

	# String example = "55 72 86"
	
	# "55" will = the integer 10
	# "72" will = the integer 9
	# "86" will = the integer 14
	
	# You then need to return the highest value, in the example above this would be 14.
	 
    # <EXAMPLES>



	# <HINT>

	# help(int) for working with numbers and help(str) for working with Strings.

def four(arg1):
	numbers = arg1.split()
	values = []
	for i, el in enumerate(numbers):
		c=0
		for p in range(len(el)):
			c+=int(el[p])
		values.append(c)
	return max(values)

	# <QUESTION 5>

    # Given a large string that represents a csv, the structure of each record will be as follows:
    
    # owner,nameOfFile,encrypted?,fileSize
    
    # "Bert,private.key,True,1447,Bert,public.key,False,1318,Jeff,private.key,False,1445"
    
    # For each record, if it is not encrypted, return the names of the owners of the files in a String Array.
    # Do not include duplicate names.
	# If all records are encrypted, return an empty Array.
    
    # <EXAMPLES>
    
   
    
	# <HINT>

	# Dont't forget, False is a String, not a Boolean value in the Tests above.

	# help(str) and help(list), you might also need to use a function that can create a list of numbers for you, try help(range).

def five(input):
	order = input.split(',')
	names =[]
	for i, el in enumerate(order):
		if el == 'private.key':
			if order[i+1]=='False':
				names.append(order[i-1])

	return names

	# <QUESTION 6>

    # There is a well known mnemonic which goes "I before E, except after C", which is used to determine which order "ei" or "ie" should be in a word.
    
    # Write a function which returns the boolean True if a string follows the mnemonic, and returns the boolean False if not.

	# <EXAMPLES>



	# <HINT>

	# Step through the logic here in order to solve the problem, you may find help(range) helpful.


def six(input):
	for i in range(len(input)):
		if input[i]=='i' and input[i+1]=='e' and input[i-1] != 'c':
			return True
		elif input[i]=='e' and input[i+1]=='i' and input[i-1] == 'c':
			return True
	return False

	# <QUESTION 7>

    # Write a function which returns the integer number of vowels in a given string. 
    # You should ignore case.

	# <EXAMPLES>



	# <HINTS>

	# How do we ignore case in a String? help(str) may offer some insight.

def seven(input):
	vowels ='AEIOUaeiou'
	c = 0
	for i in range(len(input)):
		if input[i] in vowels:
			c+=1
	return c

	# <QUESTION 8>

	# Write a function which takes an input (between 1 and 10 inclusive) and multiplies it by all the numbers before it.
	# eg If the input is 4, the function calculates 4x3x2x1 = 24 

	# <EXAMPLES>



	# <HINT>

	# You may need to create a list of numbers from 0 to i, take a look at help(range).

def eight(input):
	c = 1
	for i in range(1,input+1):
		c*=i

	return c

	# <QUESTION 9>

    # Given a string and a char, returns the position in the String where the char first appears.
    # Ensure the positions are numbered correctly, please refer to the examples for guidance.
    # DO NOT ignore case
    # IGNORE whitespace
    # If the char does not occur, return the number -1.
    
    # <EXAMPLES>



	# <HINT>

	# Take a look at the documentation for Strings, List and range.

def nine(inputString, char):
	pos = -1
	inputString=inputString.replace(" ","")
	if char in inputString:
		pos = inputString.index(char)+1
	return pos

	# <QUESTION 10>

    # Given a string, int and a char, return a boolean value if the 'nth' 
    # (represented by the int provided) char of the String supplied is the same as the char supplied.
    # The int provided will NOT always be less than than the length of the String.
    # IGNORE case and Whitespace. 
    
    # <EXAMPLES>


	# How do we find the length of a container, take a look at help(len), you will also need to look at help(str) for String manipulation.
 
def ten(string, int, char):
	if len(string)<int:
		return False
	if string[int-1].lower()==char.lower():
		return True
	else:
		return False

