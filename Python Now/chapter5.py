#dictonary = Key value pair
# undordered, Mutable, indexed, cannot contains duplicate keys

marks = {
    "pop":100,
    "Mangesh":66,
    "Pooja": 89,
    "Sham":40
}

print(marks, type(marks))
print(marks["Pooja"])
print(len(marks))

#methods of dictionary
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"pop": 99, "Renuka":100})
print(marks)
print(marks.get("pop")) #Prints None if Pop  does not exist
print(marks["pop"]) #Give an error if Pop  does not exist


#sets - sets cannot contains duplicates and we cannot access set using index
s = {1, 2, 4,5,4,3,2,3,"pop"}
e = set()# Used to create an empty set
print(type(s))
print(s)

#methods of set
s.add(555)
print(s)
print(len(s))
s.remove(2)
print(s)

s1 = {1,45,6, 78}
s2 = {7,8,1,78}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1-s2)
print({1,6}.issubset(s1))