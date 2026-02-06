#1
dog = dict()
print(dog)
#2
dog['Name'] = 'Henry'
dog['Color'] = 'Brown'
dog['Breed'] = 'German Sherpad'
dog['Legs'] = 4
dog['Age'] = 5
#3
student_dictionary ={
    'first_name':'Noah',
    'last_name': 'Olweny',
    'gender':'Male',
    'Age':20,
    'marital status':'Married',
    'skills':['Python', 'Java', 'C++'],
    'country':'Burkina Faso',
    'city':'New York',
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
#4
print(len(student_dictionary))
#5
skils = student_dictionary['skills']
print(isinstance(skils, list)) #isinstance checks data type
print(type(skils))
#6
student_dictionary['skills'].extend(['HTML', 'CSS', 'React'])
print(student_dictionary)
#7
keys = student_dictionary.keys()
my_keys_lst = list(keys)
print(my_keys_lst)
#8
pairs = student_dictionary.values()
my_pair_lst = list(pairs)
print(my_pair_lst)
#9
print(student_dictionary.items())
#10
student_dictionary.pop('skills')
print(student_dictionary)
#11
del student_dictionary