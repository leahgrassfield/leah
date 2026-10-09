# 3.1 Say Goodbye
def say_goodbye(name):
    print("Goodbye,", name)
say_goodbye("leah") 

# 3.2 Area of a Circle
def circle_area(radius):
    print(3.14*radius**2)
circle_area(5) 

# 4 Return Functions
# 4.1 Subtract, Multiply, Divide
def subtract(a, b):
    return (a - b)
print(subtract(4, 3))

def multiply(a, b):
    return (a * b)
print(multiply(5, 6))

def divide(a, b):
    return(a / b)
print(divide(9, 3))

# 5 Conditionals
# 5.1 What Should I Wear?
temperature = [50, 65, 66, 70, 72, 73, 80]
print(min(temperature),",", max(temperature))

#5.2 Check if it's the Weekend
def is_weekend(num_day):
    if int(num_day) == 6 or num_day == 7:
        return "It's the weekend!"
    else:
        return "It's not the weekend"
print(is_weekend(3))
print(is_weekend(7))

# 5.3 Fuel Efficiency Calculator
def fuel_efficiency(miles, gallons):
    return(miles / gallons)
print(fuel_efficiency(500, 3))

# 5.4 Secret Code
def secret_code(int):
    if int < 10:
        return int
    last_int = int % 10
    print(last_int)
    other_int = int // 10
    print (last_int)

    x = 1
    while other_int > 0:
        x *= 10
        print(x)
        other_int //= 10
        print(other_int)
    return (last_int * x) + other_int

secret_code(12345)

# 6 Loops 
# 6.1 Oski Stole Your Power
print("newest")
def power(x, y):
    result = x
    counter = 1
    while counter < y:
        result *= x
        counter += 1
    return result
print(power(2, 4))

# 6.2 Min & Max with Loops

# 6.2.1 For Loops

def minimum(list):
    min = 1000
    for num in list:
        if num < min:
            min = num
    return min

input = [20, 30, 40, 10, 60]
print(minimum(input))

def maximum(list):
    max = 0
    for num in list:
        if num > max:
            max = num
    return max

input = [20, 30, 40, 10, 60, 70]
print(maximum(input))

# 6.2.2 While Loops
def minimum(list):
    counter = 0
    min = list[0]
    while counter < len(list):
        if min > list[counter]:
            min = list[counter]
        counter += 1
    return min

list = [10, 4, 20, 49, 80]
print(minimum(list))

def maximum(list):
    counter = 0
    max = list[0]
    while counter < len(list):
        if max < list[counter]:
            max = list[counter]
        counter += 1
    return max

list = [10, 4, 20, 49, 80]
print(maximum(list))

# 6.3 Calculate the Sum

def sumcalc(integer):
   return sum(int(num) for num in str(abs(integer)))

print (sumcalc(416))

# 7.1 Favorite from problem set!
def minimum(list):
    counter = 0
    min = list[0]
    while counter < len(list):
        if min > list[counter]:
            min = list[counter]
        counter += 1
    return min

list = [10, 4, 20, 49, 80]
print(minimum(list))

print(f"the result of minimum with while loops with the list [10, 4, 20, 49, 80] is 4")