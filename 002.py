N = int(input())

def count_div(n):
    cnt = 1
    for i in range(1, N//2+1):
        if n % i == 0:
            cnt += 1
    return cnt 

ans = 0
for n in range(1, N+1, 2):
    if count_div(n) == 8:
        ans += 1

print(ans)