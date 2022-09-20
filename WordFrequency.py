infile = ('sometext.txt', 'r')
print(type(infile))

dict = {}



for record in infile:
    dict['word'] = {record[1] : "Fido", "cat": "Sox"}

print('Word,', 'Frequency')

for k,v in dict.items:
    print(k,v)

