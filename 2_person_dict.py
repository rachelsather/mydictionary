person = {} #name of the dictionairy; brackets mean it is empty
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"] #list; access elements by index
person["pets"] = {"dog": "Fido", "cat": "Sox"} #another dictionairy; access elements by key

print(person)

print(type(person['children'])) #type shows that belongs to the class 'list'

print(person['children'][1]) #number shows value at that location in the list

print(person['pets']['cat']) #'cat' key shows value at that location in the key

for i in person ['children']: # i is anything in the list
    print (i) #prints every name in the list

for i in person['pets']: # i represents the keys; does not include pet names
    print(person['pets'][i])



