first, second = map(int, input().split())

arr = [first, second]

for i in range(2, 10):
    next_number = (arr[-1] + arr[-2]) % 10
    arr.append(next_number)

for number in arr:
    print(number, end=" ")