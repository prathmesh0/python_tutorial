#String in Python -  Immutable

name = "pratham"
father = 'shivaji'
surename = '''Parab
and family'''
print(name, father, surename)

#slicing
name = "prathmesh"
shortname = name[0:3] #start from 0and exclude 3
print(shortname)
print(name[1])
print(name[-4:-1])
print(name[5:8])
print(name[:4])
print(name[1:])

# #slicing with skipping
a = "0123456789"
print(a[1:8:3])

#functions in String

city = "Mumbai"
print(len(city))
print(city.endswith("ai"))
print(city.startswith("mum"))

s  = "hello world"
print(s.find("ello"))
print(s.capitalize())
print(s.lower())
print(s.upper())
n = "199r3"
print(n.isdigit())


#escape sequence ->(\n, \t, \"\" )

p = "Pop is not \na bad boy \\ which means\t he is \"good\" boy"
print(p)


# practice set 3 - //fstring
user = input("Enter your name : ")
print(f"Good afternoon {user}")

letter = '''Dear name,
You are selected!
Date'''
            
print(letter.replace("name", "pop").replace("Date", "18/3/2023"))

sentence =  " Hello my name is   Pop"
print(sentence.find("  "))
print(sentence.replace("  ", " "))
print(sentence)# strings are immutable which means you cannot change them by running functions on them

newLetter = "Dear Prap,\n\tThis Python course is nice.\nThanks!"
print(newLetter)
