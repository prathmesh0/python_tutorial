#list and tuple

friends = ["apples", "oranage", 90, 5.6, "Akash", "rohan"]

print(friends[0])
friends[0] = "apple" #unlike string list are mutable
print(friends[0])
print(friends[5])
print(friends[1:4])

#methods of the list
print(friends)
friends.append("pop")
print(friends)

l1 = [1,23,5,64,3,2]
print(l1.sort())
print(l1)
l1.reverse()
print(l1)
l1.insert(3, 3333)
print(l1)
print(l1.pop(2))
print(l1)
print(l1.remove(3333))
print(l1)


#tuple -> immutable
a = (1,2,4,5, False, 5, "rohan", "shivam")
print(type(a))
# b =  (1,)
# print(type(b))
print(a)
#methods

no = a.count(5)
print(no)
i = a.index(5)
print(i)
print(5 in a)

print(len(a))


# Practice set
fruits = []

f = int(input("Enter the number of fruits : "))

for _ in range(f):
    fruit = input("Enter the fruit name : ")
    fruits.append(fruit)

print(fruits)

marks = []
n = int(input("Enter the number of marks here: "))

for _ in range(n):
    num = int(input("Enter the marks : "))
    marks.append(num)

marks.sort()
print(marks)

#check that tuple type cannot be change  in python
lerri = ("Pop", 9, 55.65)
print(lerri)
# lerri[1]= "Sham"
# print(lerri)

# sum a list of 4 numbers
age = [23,55,33,22]
print(sum(age))

#count number of zeros in tuple
g = (3,0,0,2,2,0,4)
cnt = g.count(0)
print(cnt)


