n = int(input())
arr = list(map(int,input().split()))

min_sum = float('inf')

for i in range(n):
    home = 0
    for j in range(n):
        home += abs(i-j)*arr[j]
    if home < min_sum:
        min_sum = home

print(min_sum)