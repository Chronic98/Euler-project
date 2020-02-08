# https://projecteuler.net/problem=7
from time import process_time

n = 1
lst = [2]
stop = 1
r = 3
k = 3
while stop == 1:
    for i in range(r, n+1, 2):
        k += 2
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j*j-1 > i:
                lst.append(i)
                if len(lst) > 9999:
                    stop = 0
                break
            if i % j == 0:
                break
        else:
            lst.append(i)
            if len(lst) > 9999:
                stop = 0
                break
    r = n + 2
    n = k + 100
print(lst[-1])
print(process_time())
