arr = [1, 3, 2, 7, 5, 2 , 4, 7, 6, 6]
dup = []
dummy = []

for i in arr:
    if i in dummy:
        dup.append(i)
    else:
        dummy.append(i)

print("The elements which are Duplicate from the List is : ", dup)