L=[10,50,99,11,33,73,91,66,22]
s=0
for i in L:
    s=s+i

print(s)
L.sort()
print("Sorted list: ",L)
L.reverse()
print("Reversed list: ",L)