integer = list(map(int, input().split()))

numbers = []

for num in integer:
    if num == 999 or num == -999:
        break
    numbers.append(num)

max_val = max(numbers)
min_val = min(numbers)

print(max_val, min_val)