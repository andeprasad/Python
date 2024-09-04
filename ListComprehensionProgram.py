'''
we need to take 3 inputs for x, y and x for permutation of these 3 inputs and the 4th input is the value.
Here we need to take the sum of each permutation, and if the permutation doesn't equals to the value.
Then we need to print those values.
'''

x = int(input())
y = int(input())
z = int(input())
n = int(input())

l = []

for i in range(x+1):
    # print("I = ", i)
    for j in range(y+1):
        # print("J = ", j)
        for k in range(z+1):
            # print("k = ", k)
            a = [i, j, k]
            l.append(a)

print("All Permuation occurances : ", l)

sum = 0
anslist = []
for outer in l:
    sum = 0
    for inner in outer:
        sum = inner + sum
    # print("Sum is : ", sum)
    if sum != n:
        anslist.append(outer)
        
print("The Value which doesn't match to ", n , " : ", anslist)