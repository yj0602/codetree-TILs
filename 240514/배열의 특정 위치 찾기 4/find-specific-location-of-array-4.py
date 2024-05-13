lst = []
n_input = input().split()
for n_str in n_input:
    num = int(n_str)
    if num == 0:
        break
    lst.append(num)
even_number = []
total = 0
for i in range(len(lst)):
    if lst[i]%2==0:
        even_number.append(lst[i])
        total += lst[i]
print(len(even_number), total)