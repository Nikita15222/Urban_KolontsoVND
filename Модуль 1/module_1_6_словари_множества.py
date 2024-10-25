#Задание 1-----------------------------------------------------------
print('1. Работа со словорями:')
my_dict = {'Nikita': 1994, 'Alena': 1997}
print('Dict:', my_dict)
print('Existing value:', my_dict['Nikita'])
print('Not existing value:', my_dict.get('Alina','Не найдено'))
# my_dict_2 = {} #создан новый словарь для добавления старого (расширение кругозора)
# for key, value in my_dict.items():
    # my_dict_2[key] = value
# my_dict_2.update({'Natali': 1989, 'Irina': 1973})
my_dict.update({'Natali': 1989, 'Irina': 1973})
print('Dict:', my_dict)
a = my_dict.pop('Nikita')
print('Deleted value:', a)
print('Modified dictionary: ', my_dict)

#Задание 2-----------------------------------------------------------
print('2. Работа с множествами')
my_set ={1, 2, 3, '1',6.54, True, (1,2)}
print('Set: ',my_set)
my_set.update({7,8})
my_set.remove((1,2))
print('Modified set: ',my_set)