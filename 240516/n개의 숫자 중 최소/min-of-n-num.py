import sys

n = int(input())
integer = list(map(int, input().split()))

min_val = sys.maxsize
num = 0 

for elem in integer:
    if elem < min_val:
        min_val = elem 
        num = 1
    elif elem == min_val:
        num += 1

print(min_val, num)