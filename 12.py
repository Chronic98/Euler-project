# https://euler.jakumo.org/problems/view/12.html
i = n = D = 0
while D < 500:
    i += 1
    n += i
    if n % (2*3*5*7) != 0:
        continue
    d = 2
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            d += 2
        if j * j == n:
            d -= 1
    D = max(D, d)
print(i, n, D)