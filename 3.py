# https://projecteuler.net/problem=3
import time


# проверка является ли число простым
def Prime_number(number):
    for ii in range(3, number+1, 2):
        if number % ii == 0:
            if number == ii:
                return number
            else:
                break


def number_dividers(desired_number):
    # может словить баг, пропустив некоторые большие делители (они как правило не являются простыми)
    desired_number_2 = desired_number * 0.000003
    for ii in range(3, int(desired_number_2), 2):
        if ii < desired_number_2:
            if desired_number % ii == 0:
                list_n.append(ii)
                if ii == desired_number:
                    return list_n


desired_number = 600851475143
list_n = []
list_number = []
number_dividers(desired_number)
print(list_n)
for numb in list_n[::-1]:
    number = Prime_number(numb)
    if number:
        list_number.append(number)
        break
print(list_number)
print(time.process_time())



