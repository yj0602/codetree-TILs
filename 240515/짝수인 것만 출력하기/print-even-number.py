n = int(input())
elements = list(map(int, input().split()))
even_numbers = []

for elem in elements:
    if elem % 2 == 0:
        even_numbers.append(elem)

for num in even_numbers:
    print(num, end=" ")