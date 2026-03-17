import json
# Level 1
# Number 1
obama = open(r"C:\Users\AISHA\Desktop\adam details\Anwaar Batala\30Days of Python\TextFiles\obama_speech.txt", "r")
word_counter = 0
line_counter = 0
for line in obama:
    words = line.split()
    word_counter += len(words)
    line_counter += 1
print(f"Total words in Obama's speech: {word_counter}")
print(f"Total lines in Obama's speech: {line_counter}")
obama.close()

# Number 2
michelle = open(r"C:\Users\AISHA\Desktop\adam details\Anwaar Batala\30Days of Python\TextFiles\michelle_obama_speech.txt", "r")
wordS_counter = 0
lineS_counter = 0
for line in michelle:
    words = line.split()
    wordS_counter += len(words)
    lineS_counter += 1  
print(f"Total words in Michelle's speech: {wordS_counter}")
print(f"Total lines in Michelle's speech: {lineS_counter}")
michelle.close()

# Number 3
melina_trump = open(r"C:\Users\AISHA\Desktop\adam details\Anwaar Batala\30Days of Python\TextFiles\melina_trump_speech.txt", "r")
wordT_counter = 0
lineT_counter = 0   
for line in melina_trump:
    words = line.split()
    wordT_counter += len(words)
    lineT_counter += 1
print(f"Total words in Melina Trump's speech: {wordT_counter}")
print(f"Total lines in Melina Trump's speech: {lineT_counter}")
melina_trump.close()

# Level 1
# Number 2
countries_json = open(r"C:\Users\AISHA\Desktop\adam details\Anwaar Batala\30Days of Python\TextFiles\countries_data.json", "r")
countries_dct = json.loads(countries_json)
print(countries_dct)
countries_json.close()


