# https://euler.jakumo.org/problems/view/3.html


def Prime_number(number):
    stop_number = 0
    ii = 1
    while stop_number != 1:
        ii += 1
        if number % ii == 0:
            if number == ii:
                stop_number = 1
                return number
            else:
                stop_number = 1


def number_dividers(desired_number):
    stop = 0
    i = 1
    while stop != 1:
        i += 1
        if desired_number % i == 0:
            list_n.append(i)
        if i == desired_number:
            stop = 1
            return list_n


desired_number = 13195
list_n = []
list_number = []
number_dividers(desired_number)

for numb in list_n:
    number = Prime_number(numb)
    if number:
        list_number.append(number)
print(list_number[-1])


