fib = 0
fib_2 = 1
stop = 0
sum_fi = 0

while stop != 1:
    sum_fib = fib + fib_2
    fib = fib_2
    fib_2 = sum_fib
    if fib_2 > 55:
        stop = 1
    else:
        if sum_fib % 2 == 0:
            sum_fi += sum_fib
print(sum_fi)
