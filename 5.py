# https://projecteuler.net/problem=5
# долго
stop = 0
i = 0
while stop != 1:
    iter = 0
    i += 1
    number = 20 * i
    for x in range(1, 21):
        iter += 1
        if number % x == 0:
            if iter == 20:
                print(number)
                stop = 1
        else:
            break
