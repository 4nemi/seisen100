N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

ans = 0
for m1 in range(M-1):
    for m2 in range(m1, M):
        score = 0
        for i in range(N):
            score += max(A[i][m1], A[i][m2])
        if ans < score:
            ans = score
print(ans)

