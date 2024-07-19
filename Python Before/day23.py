#methods of the list

l = [1,2,90,6,7,1]
print(l)
l.append(8)
print(l)
# l.sort()
# print(l)
# l.sort(reverse= True)
# print(l)
# l.reverse()
print(l.count(1))

# m  = l.copy()
# m[0] = 0
# print(l)
# print(m)

l.insert(1,  88)
print(l)

m =  [900, 1000,1100]
k = l+m
l.extend(m)
print(l)
print(k)