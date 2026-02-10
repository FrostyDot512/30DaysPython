#Level 1

#1
for i in range(11):
    print(i)

count = 0
while count < 11:
    print(count)
    count += 1

#2
for m in range(10, -1, -1):
    print(m)

myNum = 10
while myNum > -1:
    print(myNum)
    myNum -= 1

#3
tri = 1
while tri < 8:
    print(("#")* tri) 
    tri += 1

#4
#they are 8 #
#done 8 times
condition = False
while condition != True:
    for i in range(1, 9):
        print(("# ")* 8)
    if i == 8:
        condition = True
 
#5
count = 0
for me in range(11):
    print(f"{me} x {count} = {me * count}")
    count += 1
#6
myList = ['Python', 'Numpy','Pandas','Django', 'Flask']
for lst in myList:
    print(lst)

#7

for evenNum in range(0, 102, 2):
    print(evenNum)

#8
for i in range(101):
    if i % 2 != 0:
        print(i)

#Level 2

#1
sum_total = 0
for i in range(101):
    sum_total += i
print(f"The sum of all numbers is {sum_total}.")

#2
sum_evens = 0
sum_odds = 0

for i in range(101):
    if i % 2 == 0:
        sum_evens += i
    else:
        sum_odds += i

print(f"The sum of all evens is {sum_evens}.")
print(f"The sum of all odds is {sum_odds}.")

#Level 3
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]
#1
"""
for counts in countries:
    if counts == "land":
        print(counts)
"""
#2
fruitslst = ['banana', 'orange', 'mango', 'lemon']
cond = True
while cond:
    fruitslst.reverse()
    print(fruitslst)
    cond = False

#3
from countries_data import countries_data

all_languages = []
for country in countries_data:
    all_languages.extend(country['languages'])

# Get unique languages
unique_languages = set(all_languages)
print(f"Total number of languages: {len(unique_languages)}")

#4
from countries_data import countries_data

language_count = {}
for country in countries_data:
    for language in country['languages']:
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1

# Sort and get top 10
sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
print("Top 10 most spoken languages:")
for i in range(10):
    print(f"{i+1}. {sorted_languages[i][0]}: {sorted_languages[i][1]} countries")

    #5
    from countries_data import countries_data

# Sort by population
sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)

print("Top 10 most populated countries:")
for i in range(10):
    country = sorted_countries[i]
    print(f"{i+1}. {country['name']}: {country['population']:,}")
