numbers = list(map(int, input().split()))

if any(num >= 250 for num in numbers):
    numbers = numbers[:-1]

total = sum(numbers)
average = total / len(numbers)

print(total, round(average, 1))