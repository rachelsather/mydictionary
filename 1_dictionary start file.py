import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}


'''
print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(type(phonebook)) #Type lets us know what we're dealing with (dict)

phone = phonebook ['Chris'] #key error means that key does not exist in the dictionairy
print(phone)

print(len(phonebook)) #how many elements are in the phonebook


mydictionairy = dict(m = 8, n = 9)
print(mydictionairy)


mydict = () #creates an empty dictionairy
print(mydict)


print()
print('*****  end section 1 ********')
print()





print()
print('*****  start section 2 - search dictionary ********')
print()


name = 'Chris'

if name in phonebook:
    print(phonebook[name]) #returns the value, not the key
else:
    print(name, 'not found')


print()
print('*****  end section 2 ********')
print()




print()
print('*****  start section 3 - edit/append dictionary ********')
print()


print(phonebook)
phonebook['Chris'] = '555-0123' #updates value bc Chris already exists
phonebook['Joe'] = '555-4444' #adds Joe
print(phonebook)


print()
print('*****  end section 3 ********')
print()




print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()


del phonebook['Chris']
print(phonebook)


print()
print('*****  end section 4 ********')
print()


'''

print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()


for k in phonebook: #k stands for key; can be anything
    print(k) #default option is iterating through the keys

for value in phonebook.values(): # if you want to iterate through values, call a method
    print(phonebook[k])
    print(value)

for k,v in phonebook.items(): #items methods allows us to access both key and values at the same time
    print('key:', k, '    value: ', v)

for tuple in phonebook.items(): #immutable objects - you can't change them
     print(tuple)


print()
print('*****  end section 5 ********')
print()


'''

print()
print('*****  start section 6 - using get and clear ********')
print()

phone = phonebook.get("Chris", "key not found") #Chris is case sensitive
print(phone)

#phonebook.clear()
#print(phonebook)


print()
print('*****  end section 6 ********')
print()




print()
print('*****  start section 7 - using pop method ********')
print()


remove = phonebook.pop('Chris', 'key not found') #pops it out of the dictionairy

print(remove)
print(phonebook)


print()
print('*****  end section 7 ********')
print()




print()
print('*****  start section 8 - using popitem ********')
print()


a = phonebook.popitem() #random part does not work; it just picks the last value

print(a)
print(phonebook)


print()
print('*****  end section 8 ********')
print()




print()
print('*****  start section 9 - using random and converting to list ********')
print()


list_of_keys = list(phonebook)
print(list_of_keys)
random_key = random.choice(list_of_keys) #chooses random name
print(random_key)
print(phonebook[random_key]) #chooses random number

print(phonebook[random.choice(list(phonebook))]) #same as previous block


print()
print('*****  end section 9 ********')
print()

'''