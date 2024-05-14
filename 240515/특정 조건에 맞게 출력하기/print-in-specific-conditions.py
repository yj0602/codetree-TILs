numbers = list(map(int, input().split()))
output = []

for number in numbers:
    if number == 0:
        break
    elif number % 2 != 0:
        output.append(number + 3)
    else:
        output.append(number // 2)

print(*output)