N = int(input())
S = str(input())

cnt = 0
for v in range(1000):
    if v < 10:
        v = '0'+'0'+str(v)
    elif v < 100:
        v = '0'+str(v)
    else:
        v = str(v)

    x = 0
    for i in range(N):
        if x == 0 and S[i] == v[0]:
            x += 1
        elif x == 1 and S[i] == v[1]:
            x += 1
        elif x == 2 and S[i] == v[2]:
            x += 1
        
    if x == 3:
        cnt += 1
        

print(cnt)