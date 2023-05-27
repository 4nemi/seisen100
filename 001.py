def main(n, x):
    ans = 0
    for i in range(1, n-1):
        for j in range(i+1, n):
            k = x-i-j
            if 1 <= k <= n and i< j < k:
                ans += 1 
    return ans

while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    print(main(n, x))

