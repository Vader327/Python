file = open(r"C:/Users/Saaheer/Desktop/Programming/test.txt", "r")
text = file.read()

words=[]
letters=[]
nos=[]
chars=[]
rep_chars=[]
filters=[]
palindromes=[]

for word in text.split():
    words.append(word)
    
    for letter in word:
        chars.append(letter)

for char in chars:
    if not char.isnumeric():
        letters.append(char)
    elif char.isnumeric():
        nos.append(char)
        
for char in chars:
    if char not in filters:
        filters.append(char)

    elif char in filters:
        filters.remove(char)
        rep_chars.append(char)

for word in words:
    rev = word[::-1]
    if word==rev and len(word)>2:
        palindromes.append(word)

print("Longest Word: " + max(words))
print("Number of Alphabets: " + str(len(letters)))
print("Number of Numbers: " + str(len(nos)))
print("Repeating Characters: " + str(rep_chars))
print("Palindromes: " + str(palindromes))
