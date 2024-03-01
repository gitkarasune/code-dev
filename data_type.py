#💥💫 Kara Sune...
#Data Types

firstName = "Sune"
SurName = "Kara"
print(SurName + " " + firstName + "💥💫")
print(type(firstName))
print(isinstance(firstName, str))
print(type(firstName))
bread = str("sweet")
print(type(bread))
print(type(isinstance(bread, str)))
print(type(bread) == str)

#concatenation
fullname = SurName + " " + firstName + " 💥💫"
print(fullname)
new = "Hello..."
fullname = new + " " + fullname
print(fullname)

#Casting a Number
newyear = str(2024)
print(type(newyear))
print(type(newyear) == str)
print(type(isinstance(newyear, str)))

statement = "I like Trapping songs, 6lack just released " + "last week in " + newyear

#Multi Line
Multi = '''
Hey, how are you ?                                                        

I was just checking In.   
                        All good ?
'''
print(Multi)
print(type(Multi))
print(type(isinstance(Multi, str)))
print(type(Multi)== str)

#Escaping special characters
sentence = 'I\'m back at work!\t Hey!\n\n Where\'s this at \\ located ?'
print(sentence)
print(type(isinstance(sentence, str)))

print(" ")
print(firstName)
print(firstName.upper())
print(firstName.lower())
print(Multi)
print(Multi.title())
print(Multi.replace("good", "nice"))
print(Multi)

print("******* WELCOME GIT FOR ME******************")
print(len(Multi))
print(len(Multi.strip()))
print(len(Multi.lstrip()))
print(len(Multi.rstrip()))



#Build a menu
title = "Menu".upper()
print(title.center(20, "="))
print("Muffing".ljust(16, "*") + " $2".rjust(2))
print("cheesecake".ljust(16, "*") + "$3".rjust(1))


print(firstName[1])
print(firstName[-1])
print(firstName[0:])

print(firstName.startswith("K"))
print(SurName.startswith("K"))
print(SurName.endswith("a"))

myvalue = True
x = bool(False)
print(x)
print(type(x))
print(isinstance(myvalue, bool))


price = 1000
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))


letgp = 53.3
import math
print(math.gamma)
print(math.sqrt(100))
print(round(math.sqrt(100)))

print("***************")
print(math.floor(letgp))
print(math.ceil(letgp))

print("     " + "*************")
zipcode = "10000"
zip_value =  int(zipcode)
print(zip_value)
zip_value = int("New York")
print(zip_value)

