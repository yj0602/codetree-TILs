N = int(input())
A = [0] * 200

for _ in range(N):
    l, r = map(int, input().split())
    for i in range(1,r):
        A(l+OFFSET) += 1
print(max(A))