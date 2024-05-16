N = int(input())
A = [0] * 200

for _ in range(N):
    l, r = map(int, input().split())
    for i in range(l, r):  # 구간의 시작부터 끝까지 반복합니다.
        A[l] += 1          # 해당 구간의 빈도수를 1 증가시킵니다.

print(max(A))