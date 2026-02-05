#Level 1
#1
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
#2
it_companies.add("Twitter")
print(it_companies)
#3
myCompanies = {"HP", 'Samsung', 'Lenovo', 'Dell'}
it_companies.update(myCompanies)
print(it_companies)
#4
it_companies.remove('Oracle')
print(it_companies)
#5
#If the item not in set and you use remove() it will raise an error
#However if you use discard() no error will occur 

#Level 2
#1
A.intersection(B)
#2
A.issubset(B)
#3
A.isdisjoint(B)
#4
A | B
B | A
#5
A.symmetric_difference(B)
#6
del A
del B

#Level 3
#1
age_set = set(age)
age_set_length = len(age_set)
age_lst_length = len(age)
print(f"Is {age_set_length > age_lst_length}")
#2
"""
String is text only stores characters (letters, numbers, symbols)
Ordered, immutable, allows duplicates and written with qoutes
List stores multple items of any type Ordered, mutable, allows duplicates uses sqaure brackets
Tuple think of locked list, same as list cannot be changed, ordered, allows duplicates uses ()
Set uses unique items only stores items with no duplicates, Un ordered mutable, no duplicates and uses {}
"""
#3
sentence = "I am a teacher and I love to inspire and teach people."

words = sentence.lower().replace('.', '').split()

unique_words = set(words)

print(unique_words)
print(len(unique_words))
