A, B, C, X, Y = map(int, input().split())

min_money = 10**18

money = 0
m1 = A + B
m2 = 2 * C
money = min(m1, m2) * min(X, Y)
X, Y = max(0, X-Y), max(0, Y-X)

if X > 0:
    m1 = A
    m2 = 2 * C
    money += min(m1, m2) * X
elif Y > 0:
    m1 = B
    m2 = 2 * C
    money += min(m1, m2) * Y

print(money)