#Level 1
#1
def add_two_numbers(num_one, num_two):
    sum = num_one + num_two
    return sum
print(add_two_numbers(3, 5)) 

#2
def area_of_circle(radius):
    pi = 3.14
    area = pi * radius ** 2
    return area
print(area_of_circle(5))

#3
def add_all_nums(*args):
    for arg in args:
        if not isinstance(arg, (int, float)):
            return f"{arg} is not a number, please provide numbers only"
    return sum(args)

print(add_all_nums(1, 2, 3))        # 6
print(add_all_nums(1, 2, "hello"))  # hello is not a number, please provide numbers only
print(add_all_nums(1.5, 2.5, 3))    # 7.0

#4
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
print(convert_celsius_to_fahrenheit(0))    # 32.0
print(convert_celsius_to_fahrenheit(100))  # 212.0

#5
def check_season(month):
    month = month.lower()
    if month in ['december', 'january', 'february']:
        return "Winter"
    elif month in ['march', 'april', 'may']:
        return "Spring"
    elif month in ['june', 'july', 'august']:
        return "Summer"
    elif month in ['september', 'october', 'november']:
        return "Autumn"
    else:
        return "Invalid month name"
print(check_season("March"))  # Spring

#6
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Slope is undefined (vertical line)"
    slope = (y2 - y1) / (x2 - x1)
    return slope
print(calculate_slope(1, 2, 3, 4))  

#7
def solve_quadratic_equation(a, b, c):
    import math
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"
    elif discriminant == 0:
        root = -b / (2*a)
        return f"One real root: {root}"
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Two real roots: {root1} and {root2}"
print(solve_quadratic_equation(1, -3, 2))  # Two real roots: 2.0 and 1.0

#8
def print_list(lst):
    for item in lst:
        print(item)
print_list([1, 2, 3, 4, 5])  # Prints each number on a new line

#9
def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr
print(reverse_list([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]


