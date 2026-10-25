# 2.1 Vocabulary Review

#1. Git is the software, but Github is the platform that manages git repositories. 
#2. Terminal is the window where you type things in, but the command line is the actual script going through the computer. 
#3. A local repository is saved locally, on your computer, while a remote repository is stored remotely in the cloud. 
#4. Version control is a system that keeps track of changes made to the code, making it easier to work on, revise, and collaborate. 
#5. A staging arena is a temporary storage space to prepare code before you commit it in Git. 
#6. Git Add adds data to the staging area.
#7. Git commit saves work locally
#8. Git push saves work remotely
#9. Git status checks the status of your repository, its staging area, what is committed, etc. 
#10. git pull pulls changes from a remote repository and updates it to your local repository. 
#11. pwd prints the directory you are on. 
#12. ls lists the files in your current directory. 
#13. cd changes your directory. 
#14. nano creates and edits a text file from your terminal
#15. touch creates a new file in the terminal
#16. mv moves a file to a different directory
#17. rm removes a file from a directory
#18. cat prints the contents of a file into the terminal


# 2.2 A Directory Tree

# 1. pwd will tell you the current working directory
# 2. ls will list all the files in the current directory
# 3. cd python_decal/brianna_repo
#    git pull origin main
# 4. mv homework.py ~/python_decal/judy_decal/homework/homework.py
# 5. cd ~/python_decal/judy_decal/homework
# 6. cat homework.py
# 7. git add .
#    git commit -m "done with homework"
#    git push origin main
# 8. you should call git pull and then do number 7 again
# 9. cd ~/Recent


# 3.1 Data Types
def checkDataType(data):
    return type(data)
print(checkDataType('hello')) 

# 3.2 Conditionals
def evenOrOdd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(evenOrOdd(76))


# 4 Loops
numbers = [1, 2, 3, 4, 5]
def sumWithLoops(numbers):
    total = 0
    for i in numbers:
        total += i
    return total
print (sumWithLoops(numbers))


# 5.1 Lists
list = ['a', 'b', 'c']
def duplicatelist(list):
    return list * 2
print(duplicatelist(list))

# 5.2 Debugging
def square(num):
    return num ** 2 #they accidentally did the mulitply function instead of the exponent function
print(square(10)) 


# 6.2 In Your VS Code Terminal

# My favorite was the sum with loops 
numbers = [20, 30, 40, 50]
print(sumWithLoops(numbers))