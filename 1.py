# https://projecteuler.net/problem=1

i = 0
sum_number = 0
while i < 999:
    i += 1
    if i % 3 == 0 or i % 5 == 0:
        sum_number += i
print(sum_number)
