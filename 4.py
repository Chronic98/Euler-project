# https://euler.jakumo.org/problems/view/4.html

palidrom = 0
for i in range(100, 1000):
    for x in range(100, 1000):
        number = i * x
        n = str(number)
        n_palidrom = n[::-1]
        if number == int(n_palidrom):
            if number > palidrom:
                palidrom = number
print(palidrom)
