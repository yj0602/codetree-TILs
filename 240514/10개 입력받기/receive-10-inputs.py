lst = []
n_input = input().split()
for num_str in n_input:
    num = int(num_str)
    if num == 0:
        break
    lst.append(num)

total = sum(lst)
average = total / len(lst) if lst else 0
print(total, round(average, 1))