#1
numbers = [-4, -3, -2, -1, 0, 2, 6]
negative_and_zero = [i for i in numbers if i <= 0]
print(negative_and_zero)

#2
#later

#3
even_numbers = [i for i in range(21) if i % 2 ==0]
print(even_numbers) #[0, 2, 4, 6, 8, 9, 10, 12, 14, 16, 18, 20]

#4
countries = [[('Findland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Olso')]]
combined_count = [[country.upper(), country[:3].upper(), capital.upper()] for sublist in countries for country, capital in sublist]
print(combined_count)

#6
names =[[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald' 'Trump')], [('Bill', 'Gates')]]
combined_names = [firstname + ' '+ lastname for sublist in names for firstname, lastname in sublist]
print(combined_names)
#Says too many values to be unpacked check later 

#7
#Solve slope
print((lambda x1, x2, y1, y2: ((y2-y1)/ (x2-x1)))(2, 4, 2, 6))
#Solve y-intercept
print((lambda y_value, gradient, x_value: y_value - gradient*x_value)(6, 4, 9))


