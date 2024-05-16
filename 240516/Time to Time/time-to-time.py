a, b, c, d = map(int, input(). split())
elapsed_time = 0

while True:
    if a == c and b == d:
        break
    elapsed_time += 1
    c += 1

    if c == 60:
        a += 1
        c = 0

print(elapsed_time)