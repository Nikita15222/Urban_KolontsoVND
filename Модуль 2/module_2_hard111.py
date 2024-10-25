# result = ''.join(str(item) for item in numbers) - возможность исключать значений из списка
n = int(input())
numbers = ''

for i in range(1, n//2+1):
    for k in range(i+1, n):
        if (n % (i+k) == 0):
            numbers += str(i)+str(k)

# вариант исключения из списка симметричной пары 2 (не работает  не удаляется лишняя симметрия):
# for i in range(0, len(numbers), 2):
#     for k in range(i + 2, len(numbers), 2):
#         if str(numbers[i]) + str(numbers[i + 1]) == str(numbers[k]+1) + str(numbers[k]):
#                 numbers.remove(numbers[k])
#                 numbers.remove(numbers[k])
#                 break
print(numbers)
# print(f"{n} - число из первой вставки, \n{''.join(str(item) for item in numbers)} - нужный пароль")





# вариант исключения из списка симметричной пары 3 (не работает  не удаляется лишняя симметрия):
# for i in range(0, len(numbers), 2):
#     for k in range(i + 2, len(numbers), 2):
#         # Проверяем, есть ли симметричная пара
#         if numbers[i] == numbers[k+1] and numbers[i+1] == numbers[k]:
#             # Удаляем симметричную пару
#             numbers.pop(k)
#             numbers.pop(k)  # Удаляем дважды, так как после первого удаления индексы смещаются
#             break
# # print(f"{n} - число из первой вставки, \n{numbers} - нужный пароль") - для удобства проверки пар
# print(f"{n} - число из первой вставки, \n{''.join(str(item) for item in numbers)} - нужный пароль")




# вариант исключения из списка симметричной пары 4 (не работает):
# result = []
# for i in range(0, len(numbers), 2):
#     if (str(numbers[i+1])+str(numbers[i+1])) not in result:
#         result.append(str(numbers[i]) + str(numbers[i+1]))
#
# # print(f"{n} - число из первой вставки, \n{result} - нужный пароль") - для удобства проверки пар
# print(f"{n} - число из первой вставки, \n{''.join(str(item) for item in result)} - нужный пароль")







# вариант № 5 исключения из списка симметричной пары через множество и вывод всех возможных паролей от 3 до 20(работает):
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