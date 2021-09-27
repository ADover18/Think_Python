import string
print(string.punctuation)
print(string.whitespace)

mydict = {}

for char in string.punctuation:
    mydict[char] = None

print(mydict)

def words_from_file(filepath):
    file = open(filepath)
    wordlist = []
    # print(wordlist)
    for line in file:
        line = line.strip()
        line = line.replace('-', ' ')
        line = line.translate(line.maketrans('', '', string.punctuation))
        line = line.replace('“', '')
        line = line.replace('”', '')
        line = line.replace('”', '')
        line = line.replace('’', '')
        line = line.replace('‘', '')
        line = line.replace('—', ' ')
        line = line.replace('  ', ' ')
        line = line.lower()
        line = line.split(" ")
        wordlist = wordlist + line
        wordlist = list(filter(None, wordlist))
    
    print(wordlist)


words_from_file('alice-in-wonderland.txt')