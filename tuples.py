#1
empty_tuple = tuple()
#2
brothers = ('Ama', 'Adam', 'Aziz', 'Henry')
Sisters = ('Aisha', 'Rukia', 'Susan', 'Alina')
#3
siblings = brothers + Sisters
print(siblings)
#4
print(f"I have {len(siblings)} siblings")
#5
family_members = list(siblings)
family_members.insert(0, "Abassa")
family_members.insert(1, "Sophia")
print(family_members)

#Level 2
#1
unpacked_Parent = family_members[0:2]
print(f"Unpacked Parents: {unpacked_Parent}")
unpacked_siblings = family_members[2:]
print(f"Unpacked Siblings: {unpacked_siblings}")
#2
fruits = ('apple', 'banana', 'orange', 'kiwi')
vegetables = ('carrot', 'cabbage', 'tomato', 'onion')
animal_products = ('milk', 'yoghurt', 'cheese', 'butter')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
#3
food_stuff_lst = list(food_stuff_tp)
print(food_stuff_lst)
#4
middle_item = len(food_stuff_lst) //2
print(food_stuff_lst[middle_item])
#5
print(food_stuff_lst[0:3])
print(food_stuff_lst[-3:])
#6
del food_stuff_tp
#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)