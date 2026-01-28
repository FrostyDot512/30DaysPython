print("{} {} {} {}".format("Thirty", "Days", "Of", "Python") ) #1
print("{} {} {}".format("Coding", "For", "All") ) #2
Company = "Coding For All" #3
print(Company) #4
print(len(Company)) #5
print(Company.upper()) #6
print(Company.lower()) #7
#8
print(Company.capitalize())
print(Company.title())
print(Company.swapcase())
print(Company.strip("Coding")) #9
#10
print(Company.index("Coding")) 
print(Company.find("Coding"))
print(Company.replace("Coding", "Python")) #11
#12
Python_Variable = "Python for Everyone"
print(Python_Variable.replace("Everyone", "All"))
#13
MyVariable = "Coding For All"
print(MyVariable.split())
#14
Another_Variable = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(Another_Variable.split(", "))
#15
Variable = "Coding For All"
print(Variable[0]) #Answer is C
#16
Var = "Coding For All"
print(Var[-1]) #Answer is "l"
#17
AnotherVariable_1 = "Coding For All"
print(AnotherVariable_1[10]) #Answer is a space
#18
PyForE = "Python For Everyone"
#19
CodForA = "Coding For All"
#20
Coding = "Coding For All"
print(Coding.find("C"))
#21
Coding_1 = "Coding For All"
print(Coding_1.find("F"))
#22
Coding_2 = "Coding For All People"
print(Coding_2.rfind("I")) 
#23
MyString = "You cannot end a sentence with because because because is a conjunction"
substring = "because"
print(MyString.find("because"))
print(MyString.index(substring))
#24
MyString1 = "You cannot end a sentence with because because because is a conjunction"
Substring1 = "because"
print(MyString1.rfind("because"))
print(MyString1.rindex(Substring1))
#25
sentence = "You cannot end a sentence with because because because is a conjunction"
start = sentence.find("because because because")
end = start + len("because because because")
phrase = sentence[start:end]
print(phrase)
#26 and 27 already done
#28
print(Coding_1.startswith("Coding"))
#29
print(Coding_1.endswith("coding"))
#30
MyCode = '   Coding For All      ' 
print(MyCode.strip(" "))
#31
Days = "30DaysOfPython"
Thirty = "thirty_days_of_python"
print(Days.isidentifier())
print(Thirty.isidentifier())
#32
Libaries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = ", ".join(Libaries)
print(result)
#33
print("I am enjoying this challenge.\nI just wonder what is next.")
#34
MyInfo = "Name\t\tAge\tCounty\tCity"
Info = "Asabeneh\t250\tFinland\tHelsinki"
print(MyInfo)
print(Info)
#35
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters sqaure".format(radius, area))
#36
a = 8
b = 6
print("{} + {} = {}".format(a, b, a+b))
print(f"{a} - {b} = {a-b}")
print("{} * {} = {}".format(a, b, a * b))
print(f"{a} / {b} = {a / b}")
print("{} % {} = {}".format(a, b, a % b))
print(f"{a} // {b} = {a // b}")
print("{} ** {} = {}".format(a, b, a ** b))





