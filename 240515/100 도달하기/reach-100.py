n = int(input())
lst = [1, n]

while True:
    next_number = lst[-1] + lst[-2]
    lst.append(next_number)
    if next_number >= 100:
        break

print(*lst)