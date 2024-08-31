# arr = [5,6,7,8,10]
# arr = [1,2,3,5]
# arr = [1]

arr = [4, 5, 6, 3, 1]

def missingElement(arr):
    arr.sort()
    number = arr[0]
    for i in arr:
        if i == number:
            number += 1
        else:
            return number
    return number

print(missingElement(arr))