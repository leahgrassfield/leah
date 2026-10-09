# 3 Lists
# 3.1 List Operations

fav_foods = ["cookies", "noodles", "almond pastries", "sushi", "hot chocolate"]

print(fav_foods[1])

print(fav_foods[-1])

fav_foods.append("cucumber")

fav_foods.insert(0, "apple")

del(fav_foods[2])

print(len(fav_foods))

for food in fav_foods:
    print(food.upper())

new_fav_foods = fav_foods[::5]
print(new_fav_foods)
#I accidentally put 7 and 6 for step length before realizing that it is the amount it skips, so I shoud put 5

if "potato" in fav_foods:
    print("A potato!")
else:
    print("No potato!")

# 3.2 Slicing and Striding

numbers = list(range(21)) #I originally put 20, forgetting that range(20) doesn't include 20

def get_first_15(numbers): #gets first 15 numbers
    return numbers[:15]
print(get_first_15(numbers))

def get_every_5th(lst): # gets every 5th # from first 15 numbers
    lst = get_first_15(numbers)
    return lst[::5]
print(get_every_5th(numbers))


def reverse_and_stride(lst): # returns every element of the previous list
    lst = get_every_5th(numbers)
    return lst[-3::-3]
print(reverse_and_stride(numbers))

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

# 3.3 Nested Lists
# 3.3.1 Nested List Operations

numbers = [
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9],
]

print(numbers[2])#apparently the strat is matrix([row][column])
#mistake, it's 2 instead of 3 because the count begins at 0

print(numbers[1][1])
numbers.append([10, 11, 12])

def sum_nested(numbers):
    total = 0
    for num in numbers:
        total += sum(num)
        return total
print(sum_nested(numbers))

# COME BACK TO THIS LATER____________________
'''
def fivebyfive_forloop(num):
    matrix = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(num[i][j])
        matrix.append(row)
    return matrix

print(fivebyfive_forloop(num))
'''
#________________________________________

#4 Dictionaries

#4.1 Dictionary Operations
ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25, 
    "Mira": 48
}

print(ages["Katie"])

ages["Mira"] = 100

ages["Milana"] = 52

del ages["Mariam"]

for name, age in ages.items():
    print(f"{name}, {age}")
