a1, a2 = map(int, input().split())

sequence = [a1, a2]

for i in range(2, 10):
    next_term = sequence[-1] + 2 * sequence[-2]
    sequence.append(next_term)

print(*sequence)