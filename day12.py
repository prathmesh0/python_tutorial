#string slicing and operations on the string

names = "prathmesh parab"
print(len(names))
print(names[0:9])

fruit = "mango"
mangoLen = len(fruit)
print(mangoLen)
print(fruit[0:4]) #including 0 but not 4
print(fruit[:4])
print(fruit[1:4])
print(fruit[:])
print(fruit[0: -3])
print(fruit[0:len(fruit) - 3])
print(fruit[-1:len(fruit) - 3]) # len()-1 : len()-3 = 4-2
print(fruit[-3:-1]) # 2:4

#Quiz 
nm = "Harry"
print(nm[-4:-2])
#loop through a string
alphabet ="ABCDE"
for i in alphabet:
    print(i)

