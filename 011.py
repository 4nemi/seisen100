N, M = map(int, input().split())
s = [None] * M
k = [None] * M
for i in range(M):
    inputs = list(map(int, input().split()))
    k[i], s[i] = inputs[0], inputs[1:]
p = list(map(int, input().split()))

ans = 0
for i in range(2**N):
    light = 0
    for m in range(M):
        cnt = 0
        for j in range(k[m]):
            if (i >> s[m][j]-1) & 1:
                cnt += 1
        
        if cnt % 2 == p[m]:
            light += 1
    
    if light == M:
        ans += 1


print(ans)