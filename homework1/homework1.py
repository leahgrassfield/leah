# File: homework1.py

# --- Variables and Data Types ---

a = 10
print(a)
print (type(a)) 
# a is an integer, number w no decimals

b = 1.5
print (b)
print (type(b))
# b is a float, decimal number

c = 3j
print (c)
print (type(c))
# 3j is a complex number

d = "hello"
print (d)
print (type(d))
# d is a string

e = [1, 2, 3]
print (e)
print (type(e))
# e is a list

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print (f)
print (type(f))
# f is a dictionary

g = (1,2)
print (g)
print (type (g))
# g is a tuple

h = ["apple", "banana", "strawberry"]
print (h)
print (type(h))
# h is a list

i = True
print (i)
print (type(i))
# i is a boolean

j = None
print (j)
print (type(j))
# j is a Nonetype

k = [True, "blue", 12]
print (k)
print (type(k))
# k is a list

l = str(14)
print (l)
print (type(l))
# l is a string

m = 1e4
print (m)
print (type(m))
# m is a float

n = range(6)
print (n)
print (type(n))
# n is a range

'''
I found 9 different data types
Integer, float, complex number, string, list, dictionary, tuple, boolean, nonetype
h,e,k are lists
b,m are floats
l,d are strings
l was a string, because str() defines it as such for the computer
I looked up n, a range
'''

# --- Booleans ---

print (10 > 9) #True, 10 > 9
print (10 == 9) #False, 10 doesnt = 9
print (10 <= 9) #False, 10 isnt < or = to 9
print (bool("abc")) #True 
print (bool(123)) #True
print (bool(["apple", "banana", "cherry"])) #True
print (bool([True])) #True
print (bool([False])) #True
print (bool(0)) #False
print (bool("")) #False 
print (bool(" ")) #True
print (bool(())) #False
print (bool([])) #False
print (bool({})) #False
print (bool(True and False)) #False
print (bool(True and True)) #True
print (bool(False and False)) #False
print (bool(True or False)) #True
print (bool(False or False)) #False
print (bool(not(False))) #True
print (bool(not(True))) #False

print (bool(6 < 3))

'''
Everything with a valid interior is true, the things that are empty or say not true are false
Why is 0 false?
6 < 3 is false because 6 > 3
'''

# --- Operators ---

print (10 + 5) #15, add
print (10 - 5) #5, subtract
print (2 * 4) #8, multiply
print (6 / 3) #2, divide
print (5 % 2) #1, remainder
print (3 ** 2) #9, exponent
print (15 // 2) #7 divide and round down

# --- Comparison Operators ---

print (5 == 2) #False, 5 does not = 2
print (10 != 10) #False, 10! does not = 10
print (2 < 5) #True, 2 < 5
print (12 > 5) #True, 12 > 5
print (5 <= 6) #true, 5 < 6
print (1 >= 10) #False, 1 is not > 10 or = 10

# --- Assignments Operators ---

x = 5
x += 5
print (x) #10 add and assign

x = 5
x -= 4
print (x) #1 subtract and assign

x = 5
x *= 3
print (x) #15 multiply and assign

# The operator 'and' says true if both statements are true
print (bool(5 == 5 and 6 > 5))
print (bool(5 == 6 and 6 > 5))

# The operator 'or' says true if one of the statements is true
print (bool(1 < 2 or 2 < 1))
print (bool(5 <5 or 2 < 1))

# The operator 'not' says the opposite of if its true/false
print (bool(not 6 < 5))
print (bool(not 6 > 5))

'''
1. / gives you a float and // rounds down to the nearest integer
2. % gives you the remainder but / gives you the answer
3. I would use %. (8 % 6) is 2
4. They change the x value and then reassign x the new changed value
'''

# --- Strings ---

my_string = "hello"

print (my_string)
print (my_string[0]) #h, 1st letter
print (my_string[1]) #e, 2nd letter
print (my_string[2]) #l, 3rd letter
print (my_string[3]) #l, 4th letter
print (my_string[4]) #o, 5th letter
print (my_string[-1]) #o, last letter
print (my_string[1:3]) #el, 2nd and 3rd letter
print (my_string[0:5:2]) #hlo, 1st, 3rd, and 5th letter
print (len(my_string)) #5, number of letters in string
print (my_string + "goodbye") #hellogoodbye, adds the strings
print (my_string * 7) #hellohellohello... repeats string 7 times

# 1. Slicing is taking out a specific part of the string, used in all lines with specific letters

name = "Oski"
print ("Hello, my name is", name)
print (f"Hello, my name is {name}")
# There is no difference within the printing result

# --- Terminal Commands ---

'''
1. cd
Change Directory: move between folders
Example: cd PythonDecal

2. ls
List: show files in directory
Example: ls

3. ls -a
List All: show all files in directory
Example: ls -a

4. mkdir
Make directory: create a new directory
Example: mkdir PythonDecal

5. cat
Catenate: show contents of file
Example: cat PythonDecal/homework1.py

6. pwd
Print Working Directory: print what directory you're in
Example: pwd

7. cd ..
Change directory up one: move up one directory
Example: cd ..

8. cd .
Change directory: changes directory to the one you're currently in
Example: cd .

9. cd ~
Change directory to home: takes you to your home folder
Example: cd ~

10. cp
copy: copies a file or folder
Example: cp PythonDecal

11. mv
Move: moves file or folder
Example: mv PythonDecal

12. rm
remove: deletes file or folder
Example: rm PythonDecal

13. clear
clear: clears your workspace
Example: clear

14. grep
search through text for lines / patterns ?
Example: grep "5" PythonDecal



1. 
Round: Rounds numbers to the decimal place you select
round(32.67834, 2) = 32.68

input: takes input from the user
input("Enter value: ") = *whatever value the user inputs

capitalize: caitalizes the first letter of a string
str = "hi"
str.capitalize() = "Hi"

2. ls lists files from current directory, ls -a lists all files (including hidden)
3. a hidden file is one not shown in directories by default 
4. 
python -c: run a single python command
python -c "print('hi')"

python -O: ignore assert statements
python -O PythonDecal.py

python -x: ignore the first line of script
python -x: PythonDecal.py
'''
