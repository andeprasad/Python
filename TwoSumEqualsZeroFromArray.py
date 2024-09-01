# arr = [-1, 0, 1, 2, -1, -4]
arr = [1, 0, -1, 2, -1, -4, -2]

sumZero = []

# for i in arr:
for i in range(len(arr)):
    for j in range(i, len(arr)):
    # for j in arr:
        print(i, " " , j, arr[i], " ", arr[j])
        if arr[i] != arr[j]:
            if (arr[i] + arr[j] == 0):
                if arr[i] < arr[j]:
                    l = [arr[i], arr[j]]
                else:
                    l = [arr[j], arr[i]]
                if l not in sumZero:
                    sumZero.append(l)
                    dummy = j
                    dummyValue = arr[j]
                    arr.remove(dummyValue)
                    arr.insert(dummy, 0)

print(arr)
sumZero.sort()
print(sumZero) 