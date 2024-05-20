def final_position(n, movements):
    x, y = 0, 0
    
    direction_deltas = {
        'N': (0, 1),  
        'E': (1, 0),  
        'S': (0, -1), 
        'W': (-1, 0)
    }

    for direction, distance in movements:
        dx, dy = direction_deltas[direction]
        x += dx * distance
        y += dy * distance
    
    return x, y


N = int(input())
movements = [input().split() for _ in range(N)]
movements = [(direction, int(distance)) for direction, distance in movements]

final_x, final_y = final_position(N, movements)

print(final_x, final_y)