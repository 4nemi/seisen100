S = input()

ans = 0
acgt = 0
for s in S:
    if s in ['A', 'C', 'G', 'T']:
        acgt += 1
        if ans < acgt:
            ans = acgt
    else:
        acgt = 0

print(ans)