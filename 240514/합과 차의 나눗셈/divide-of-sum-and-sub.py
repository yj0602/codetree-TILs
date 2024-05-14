a, b = map(float, input().split())

if a != b:
    c = (a + b) / (a - b)
    print(f"{c:.2f}")