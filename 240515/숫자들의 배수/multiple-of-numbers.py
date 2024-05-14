n = int(input())
count = 0
i = 1
while True:
    multiple = n * i
    print(multiple, end=" ")
    i += 1
    if multiple % 5 == 0:
        count += 1
        if count == 2:
            break