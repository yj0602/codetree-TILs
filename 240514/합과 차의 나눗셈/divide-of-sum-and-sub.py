a, b = map(int, input().split())

if a != b:
    c = (a + b) / (a - b)
    print(round(c, 2))
else:
    print("Error: a and b cannot be equal.")