arr = []

input_str = input().split()
for num_str in input_str:
    num = int(num_str)
    if num == 0:
        break
    arr.append(num)

for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end=" ")