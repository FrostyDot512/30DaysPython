#1
empty_list = []
empty_list = list()
#2
mylist = ['Frosty', 23, True, 4.3, 1+3j, 'Rocket League']
#3
print(len(mylist))
#4
first = mylist[0]
middle = mylist[len(mylist)//2] #Get length and divide by 2 quick mathss
last = mylist[-1]

print(first)
print(middle)
print(last)
#5
mixed_data_types = ['Frosty', 18, '182cm', False, '102 Icelandic lane']
#6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#7
print(f"Comapanies: {it_companies}")
#8
print(f"Number: {len(it_companies)}")
#9
first1 = it_companies[0]
middle2 = it_companies[len(it_companies)//2] 
last3 = it_companies[-1]

print(first1)
print(middle2)
print(last3)
#10
it_companies[4] = "HP"
print(it_companies)
#11
it_companies.append("Lenovo")
print(it_companies)
#12
Mylength = len(it_companies) // 2
it_companies.insert(Mylength, "Samsung")
print(it_companies)
#13
it_companies[0] = it_companies[0].upper()
print(it_companies)
#14
result = "# ".join(it_companies)
print(result)
#15
print("Google" in it_companies)
#16
it_companies.sort()
print(it_companies)
#17
it_companies.sort(reverse=True)
print(it_companies)
#18
Mycompanies = it_companies[0:3]
print(Mycompanies)
#19
mine = it_companies[-3:]
print(mine)
#20
#wait
#21
del it_companies[0]
print(it_companies)
#22
del it_companies[Mylength]
print(it_companies)
#23
del it_companies[-1]
print(it_companies)
#24
it_companies.clear()
print(it_companies)
#25
del it_companies
#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined = front_end + back_end
front_end.extend(back_end)
print(front_end)
#27
full_stack = joined
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)