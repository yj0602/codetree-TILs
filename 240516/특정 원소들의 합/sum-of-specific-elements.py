grid = []
for _ in range(4):
    row = list(map(int, input().split()))
    grid.append(row)

total_sum = 0
for i in range(4):
    for j in range(4):
        if (i == 0 and j <= 0) or (i == 1 and j <= 1) or (i == 2 and j <= 2) or (i == 3 and j <= 3):
            total_sum += grid[i][j]

print(total_sum)