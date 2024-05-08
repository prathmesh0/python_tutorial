#String Operation
#Strings are Immutable
a = "prathmesh"
print(len(a))
print(a.upper())
print(a.lower())

b = "!!pop!!!!!!"
print(b.rstrip("!"))

print(a.replace("prathmesh", "parab"))

c = "Hello I am Prathmesh"
print(c.split(" "))

blogHeading = "introduction to Python"
print(blogHeading.capitalize())

str1 = "Welcome to the console!!!"
print(len(str1))
print(len(str1.center(50)))

print(a.count("a"))

print(str1.endswith("!!!"))
print(str1.endswith("to", 4,10))

str2 = "He's name is Dan. he is an honest man."
print(str2.find("is"))
# print(str2.index("ishh"))

str1 = "welcometothejun0gle"
print(str1.isalnum())

str1 = "hell oImPop"
print(str1.isalpha())

str1 = "heman"
print(str1.islower())

str1 = "We wish you happy birthday\n"
print(str1.isprintable())

str1 = "      " # space using space key
print(str1.isspace())

str1 = "        " # space using tab key
print(str1.isspace())

str1 = "World Health Organization"
print(str1.istitle())

str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language"
print(str1.swapcase())

str1 = "His name is Dan. Dan is good boy."
print(str1.title())
