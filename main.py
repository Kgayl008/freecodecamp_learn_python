# variables, string, we can storage a number without quotations
character_name = "John"
character_age = "50"
is_male = True

print("There once was a man named " + character_name + ",")
print("he was " + character_age + " years old")
print("He really liked the name " + character_name + ",")
print("but didn't like being " + character_age + ".")

#strings = plain text
#Backslash n = \n insert a new line in the string
print("Giraffe\nAcademy")

#Backslash \ + the escape character = tells python whatever character comes sfter it, we want to render!
print("Giraffe\"Academy")

#Concatenation = taking a string and appending another string to it
phrase = "Giraffe Academy"
print(phrase + " is cool")

#Function = perform a specfic operation for us/ always have ()
#to check if the phrase is upper or lower chase, put "is" in front of the function. The output will either be True or False
#you can use functions, one after another
phrase = "Giraffe Academy"
print(phrase.upper().isupper())

phrase = "Giraffe Academy"
print(len(phrase))

phrase = "Giraffe Academy"
print(phrase[0])

phrase = "Giraffe Academy"
print(phrase.index("Acad"))

phrase = "Giraffe Academy"
print(phrase.replace("Giraffe", "Elephant"))

# Print = it is a function, and must be invoked with parentheses.

#Number
#Python supports two type of numbers ! integers (whole numbers), floating point numbers(decimals), and complex numbers
#micing operators betwwon b=numbers and strings is not supported

myint = 7
print()

myfloat = 7.0
print(myfloat)
myfloat = float(7)

one = 1
two = 2
three = one + two
print(three)

a, b = 3, 4
print(a, b)

#Excercise
# The target of this exercise is to create a string, an integer, and a 
# floating point number. The string should be named mystring and should
# contain the word "hello". The floating point number should be named myfloat 
# and should contain the number 10.0, and the integer should be named myint 
# and should contain the number 20.

# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

print(3 * (4 + 5))
print(10 % 3)

#if you want to print a number next to a string, use the string function
my_num = 5
print(str(my_num) + " my favorvite number")

#absolute value of a number
my_num = -3.5
print(abs(my_num))

#power function
print(pow(4, 5))