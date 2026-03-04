#Level 1
countries = ['Estonia', 'Findland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#1
#The difference between the 3 reduce unlike the other 2 returns a single value
#Filter function only works if the filtering criteria has been dealt with and
#map function only takes a function and iterable as paramaters and returns 

#2
#Laters

#3
#Laters

#4
for i in countries:
    print(i)
#5
for name in names:
    print(name)
#6
for nums in numbers:
    print(nums)

#Level 2

#1
def upper_Case(country):
    return country.upper()

UppeR_CASE_Country = map(upper_Case, countries)
print(list(UppeR_CASE_Country))

#2
def sqaure(number):
    return number ** 2

Sqaured = map(sqaure, numbers)
print(list(Sqaured))

#3
def upper_Case_name(name):
    return name.upper()

UppeR_CASE_name = map(upper_Case_name, names)
print(list(UppeR_CASE_name))

#4
def Land(count):
    if "land" in count:
        return True
    return False

Land_Review = filter(Land, countries)
print(list(Land_Review))

#5
def Land_Count(word):
    if len(word) == 6:
        return True
    return False

Word_Review = filter(Land_Count, countries)
print(list(Word_Review))

#6
def Land_CountAgain(wordAgain):
    if len(wordAgain) >= 6:
        return True
    return False

Again = filter(Land_CountAgain, countries)
print(list(Again))
    
#7
def starting_with_E(letter):
    if letter[0] == 'E':
        return True
    return False

Testing = filter(starting_with_E, countries)
print(list(Testing))