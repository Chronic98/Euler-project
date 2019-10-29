# https://euler.jakumo.org/problems/view/1.html

i = 1
sum_number = 0
while i < 1000:
    i += 1
    if (i % 3 and i % 5) == 0:
        sum_number += i
print(sum_number)
