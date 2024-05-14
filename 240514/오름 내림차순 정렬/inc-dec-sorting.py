n = int(input())
arr = list(map(int, input().split()))

arr.sort()
for i in arr:
    print(i, end=' ')

print()

arr.sort(reverse=True)
for x in arr:
    print(x, end=' ')