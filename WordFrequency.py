infile = ('sometext.txt', 'r')
print(type(infile))

special_characters = [',','.']

with open('sometext.txt') as text:
    for line in text:
        for i in special_characters:
            line = line.replace(i,'')
        words = line.split()
        specificwords = dict((word, words.count(word))for word in set (words))

print('Word,', 'Frequency')
print(specificwords)

