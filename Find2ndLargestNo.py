arr = [4, 3, 10, 6, 5, 7, 19, 1]

largest = arr[0]
smallest = arr[0]
secondlargest = arr[0]

for i in arr:
    if i >= largest:
        largest = i
    if i < smallest:
        smallest = i

for i in arr:
    if i < largest and i > secondlargest:
        secondlargest = i

print("Largest is : ", largest)
print("Smallest is : ", smallest)
print("Second Largest is : ", secondlargest)