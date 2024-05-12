time = input().split(":")
h = int(time[0])
m = int(time[1])

print("{:2d}:{:02d}".format((h + 1) % 24, m))