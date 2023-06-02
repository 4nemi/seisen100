N = int(input())
A = [None] * N
B = [None] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

t_ab = 0
for i in range(N):
    t_ab += abs(A[i]-B[i])

A.sort()
B.sort()

if N%2 == 0:
    middle_a = (A[N//2]+A[N//2-1]) // 2
    middle_b = (B[N//2]+B[N//2-1]) // 2
else:
    middle_a = A[N//2]
    middle_b = B[N//2]

ans = t_ab
for i in range(N):
    ans += abs(middle_a-A[i]) + abs(middle_b-B[i])
print(ans)
