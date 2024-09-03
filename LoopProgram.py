# n = 3
# output should be as below - 
# 0
# 1
# 4
# -> The list of non-negative integers that are less than n=3 is [0, 1, 2]. 
# Print the square of each number on a separate line.

n = int(input("Enter any Number : "))
for i in range(n):
    print(i * i)
