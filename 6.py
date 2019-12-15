# https://euler.jakumo.org/problems/view/6.html

def sum_numder_v_kv():
    number = 0
    for x in range(1, 101):
        number += x
    return number * number


def sum_kvadratov():
    number = 0
    for x in range(1, 101):
        number += x * x
    return number


razniza = sum_numder_v_kv() - sum_kvadratov()
print(razniza)
