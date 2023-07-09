R, C = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(R)]

front = []
back = []

for c in range(C):
    f = 0
    b = 0
    for r in range(R):
        if a[r][c] == 1:
            f += 1
        else:
            b += 1
    front.append(f)
    back.append(b)  

ans = 0
for i in range(2**R):
    temp_front = front.copy()
    temp_back = back.copy()
    for j in range(R):
        if (i >> j) & 1:
            for c in range(C):
                if a[j][c] == 1:
                    temp_front[c] -= 1
                    temp_back[c] += 1
                else:
                    temp_front[c] += 1
                    temp_back[c] -= 1

    cnt = 0
    for i in range(C):
        cnt += max(temp_front[i], temp_back[i])
    ans = max(ans, cnt)

print(ans)