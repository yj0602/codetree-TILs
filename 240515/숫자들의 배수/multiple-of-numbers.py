number = int(input())
multiples = []

for i in range(1, 11):
    multiple = number * i
    multiples.append(multiple)
    print(multiple, end=" ")

    if multiple % 5 == 0:
        if multiples.count(multiple) == 2:
            break