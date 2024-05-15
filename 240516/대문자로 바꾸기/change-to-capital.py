lines = []

for i in range(5):
    lines.append(input().split())

lines_upper = [[word.upper() for word in line] for line in lines]

for line in lines_upper:
    print(' '.join(line[:3]))