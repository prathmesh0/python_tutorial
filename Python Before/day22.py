l = [3,5,6, "Harry", True, 44,2,2,2,11]
print(l)
print(type(l))
print(l[0])
print(l[1])
print(l[2])

colors = ["red", "yellow", "blue", "black"]
print(colors)
print(colors[-3]) #Negative Index

if "red" in colors:
    print("Yess")
else:
    print("No")
    
if "haq"in "harray":
    print("true")
else:
    print("false")
    
    
print(l)
print(l[:])
print(l[1:-4])
print(l[1:8])
print(l[1:8:2])


lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2 == 0]
print(lst)
