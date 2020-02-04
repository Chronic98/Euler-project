import math

# for c in range(250, 500):
#     for b in range(200, 400):
#         for a in range(100, 201):
#             if (a + b + c == 1000) and (a < b < c) and (math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2)):
#                 print(a *b * c)

# или
stop = 0
list_number_sqrt = []
# создаю список из целых квадратов чисел до 200000
for i in range(1, 200000):
    if math.sqrt(i) == int(math.sqrt(i)):
        list_number_sqrt.append(int(math.sqrt(i)))

print(len(list_number_sqrt))
# так как С самое большое, значит начинать быстрее будет с конца, так же и с В
for c in list_number_sqrt[::-1]:
    if stop == 1:
        break
    for b in list_number_sqrt[::-1]:
        for a in list_number_sqrt:
            if (a + b + c == 1000) and (a < b < c) and (math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2)):
                print(a * b * c)
                stop = 1
                break
