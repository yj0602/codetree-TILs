n = int(input())
numbers = list(map(int, input().split()))

for num in reversed(numbers):
    if num % 2 == 0:
        print(num, end=' ')