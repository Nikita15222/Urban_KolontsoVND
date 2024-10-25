n = int(input())
numbers = []

for i in range(1, n):
    if i <= (n/2):
        for k in range(2, n):
            if (n % (i+k) == 0) and i != k:
                numbers.append(sorted((i, k)))
numbers = set(numbers)
print(numbers)





# вариант № 1 исключения из списка симметричной пары через множество и вывод всех возможных паролей от 3 до 20:

# n = int(input())
# for k in range(3, n+1):
#     string = ''
#     seen_pairs = set()  # Множество для хранения уже добавленных пар
#     for i in range(1, k):
#         for j in range(i + 1, k):
#             if k % (i + j) == 0:
#                 pair = (i, j) if i < j else (j, i)  # Упорядочиваем пару, чтобы не было симметрии
#                 if pair not in seen_pairs:
#                     string += str(i) + str(j)
#                     seen_pairs.add(pair)  # Добавляем пару в множество, чтобы не дублировать
#     # print(k, '-', string) - если нужно перебрать все пороли от 3 до 20
# print(string)




#Вариант № 2
# n = int(input())
# numbers = []
#
# for i in range(1, n):
#     if i <= (n/2):
#         for k in range(2, n):
#             if (n % (i+k) == 0) and i != k:
#                 numbers.append(tuple(sorted((i, k))))
# numbers = sorted(set(numbers))
# new_numbers = ''
#
# for i in numbers:
#     new_numbers += str(i[0])+str(i[1])
#
#
# print(new_numbers)
