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

# Problem set5
words = {
    "Madad":  "help",
    "Kela":"Banana",
    "billi":"cat"
}
word = input("Enter the word you want meaning of: ")
print(words[word])


s = set()
n = int(input("How many numbers you want to enter : ")) 

for _ in  range(n):
    num = int(input("Enter a number : "))
    s.add(num)

print(s)

st = set()
st.add(18)
st.add("18")
st.add(18.0)
print(len(s))
print(st)

m = {}
print(type(m))

for _ in range(4):
    name = input("Enter friends name : ")
    language = input("Enter friends language : ")
    m.update({name:language})
    
print(m)


x = {5,3,21,"Harry", [3,4]}# wrong list cannot insert in the set and we cannot change the value of set



