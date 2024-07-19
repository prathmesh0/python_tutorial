def average(a,b):
    print("The average is ", (a+b)/2)
    
average(4,6)

#default argument
def average1(a = 9,b = 0):
    print("The average is ", (a+b)/2)
    
average1(1)

#Keyword Argument
average1(b =  9, a =21)

#Required argument
def average2(a, b, c = 4):
    print("The average is ", (a+b+c)/3)

average2(2,3)

#variable length argument
def average3(*numbers):
    sum = 0;
    for i in numbers:
     sum += i
    return sum / len(numbers)

c = average3(5,6)
print(c)


def name(**name):
    print(type(name))
    print("Hello", name["fname"], name["mname"], name["lname"])
    
name(mname = "Shivaji", lname = "Parab", fname = "Prathmesh")