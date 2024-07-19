#variable -> Integer, floating point ,  string , boolean
#Rules for defining variables
a = 1
b = 2
name = "Pop"
c = 89.3
d = False
e = None
print(e)
print(d)
print(c)
print(name)
print(a+b)

# Arithmetic Operator - +,-,*./
# Assignment Operator - =, +=, 
# Comparision Operator - ==, < , >, <=, >= != 
# Logical Operator - and, or, not
d = 5==5
print(d)

#type of variable
m = 42
print(type(m))
n = 89.4
print(type(n))
o = int(n)
print(str(n))
print(o)

#input
a = int(input("Enter number 1 : "))
b = int(input("Enter number 2 : "))
print("Number 1 is : ", a)
print("Number 2 is : ", b)
print("sum = ", a+b)


#practice set 2
x = int(input("Enter 1st number : "))
y = int(input("Enter 2nd number : "))

print("Sum of 2 number : ", x+y)
print("remainder : ", x%y)
print(type(x))
if x>y:
    print("x is grater than y")
else:
    print("y is grater than x")

print("Average of two number: ", (x+y)/2 )
print("Square of tht x is :", x*x) # x**2
print("Square of tht x is :", x**2) 

    


