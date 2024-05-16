a, b, c, d = map(int, input().split())

start_time = a * 60 + b
end_time = c * 60 + d

elapsed_time = end_time - start_time

print(elapsed_time)