n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

#bit全探索
ans = []
for i in range(2**n):
    total = 0
    for j in range(n):
        if (i >> j) & 1:
            total += A[j]
    if total in m:
        ans.append(total)

for i in m:
    if i in ans:
        print('yes')
    else:
        print('no')