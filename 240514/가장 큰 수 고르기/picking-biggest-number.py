arr = list(map(int,input().split()))
max_val = 0
for elem in arr:
    if elem > max_val:
        max_val = elem
print(max_val)