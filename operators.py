my_age = 18 #1
my_height = 186.0 #2
complex_number = 1 + 3j #3
#4
base = int(input("Enter triangle base: "))
height = int(input("Enter triangle height: "))
triangle_area = (0.5 * base * height)
#5
side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
triangle_perimeter = side_a + side_b + side_c
#6
length = int(input("Enter the legnth: "))
width = int(input("Enter the width: "))
rectangle_area = length * width
rectangle_perimeter = 2 *(length + width)
#7
pi = 3.14
radius = int(input("Enter radius: "))
circle_area = pi * (radius **2)
circle_circumference = 2 * pi * radius
#8
m = 2
x = 0
y_intercept = 2 * x - 2
x_intercept = 2 / 2
print("Slope:", m)
print("Y-intercept:", y_intercept)
print("X-intercept:", x_intercept)
#9
x1, y1 = 2, 6
x2, y2 = 6, 10
print(slope = ((10-2) / (6-2)))
print(distance = (((x2 - x1)**2 + (y2 - y1)**2)**0.5))
#10
slope_8 = 2
slope_9 = 2
print(slope_8 == slope_9)
print(slope_9 > slope_8)
print(slope_8 != slope_9)
print(slope_8 > slope_9)
print(slope_9 >= slope_8)
print(slope_8 >= slope_9)
print(slope_9 <= slope_8)
print(slope_8 <= slope_9)
#11
for x in range(-6, 1):
    y = x**2 + 6*x + 9
    print("x =", x, "y =", y)
#12
python_length = len("python")
dragon_length = len("dragon")
print(python_length != dragon_length)
#13
print("on" in "python" and "on" in "dragon")
#14
print("jargon" in "I hope this course is not full of jargon")
#15
print(not("on" in "python" and "on" in "dragon"))
#16
Python_Length1 = len("python")
python_float = float(Python_Length1)
python_string = str(Python_Length1)
#17
Even_number = int(input("Enter number: "))
Even_check = Even_number % 2
print(f"Is number even? {Even_check == 0}")
#18
Division = 7 // 3 
Integer = int(2.7)
print(f"Are number's equal? {Division == Integer}")
#19
string = type("10")
integer1 = type(10)
print(f"Are type's equal? {string == integer1}")
#20
Grav = int("9.8")
print(f"Are they equal? {Grav == 10}")
#21
Hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour: "))
print(f"Your weekly earning is {Hours * rate_per_hour}")
#22
Years = int(input("Enter number of years you have lived: "))
print(f"You have lived for {31536000 * Years} seconds")
#23
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)





