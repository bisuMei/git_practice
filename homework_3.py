"""
Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел
одновременно кратных и 3 и 5 - FizzBuzz
"""

# for i in range(1, 101):
#   if not i % 15:
#     print("FizzBuzz")
#   elif not i % 3:
#     print("Fizz")
#   elif not i % 5:
#     print("Buzz")
#   else:
#     print(i)
#
fizzbuzz = [('fizz'*(not i % 3) + 'buzz'*(not i % 5) or i) for i in range(1, 101)]
print(fizzbuzz)

# """
# 1) Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
# 2) Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
# 3) Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
# 4) Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
# 5) Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента не было.
# """
#
# # 1)
# lst = ['a', 'b', 'c', 'd']
# new_lst = [list(lst[i]+chr_ for chr_ in lst[1:])for i in range(2)]
# result = new_lst[0] + new_lst[1]
# print(result)
# # # 2)
# print(result[::2])
# # # 3)
# nums = [1, 2, 3, 4]
# chr_ = "a"
# final = [str(i)+chr_ for i in nums]
# print(final)
# # # 4)
# print(final.pop(final.index("2a")))
# # # 5)
# copy_lst = final[:]
# copy_lst.append('2a')
# print(copy_lst)

# a = value if condition else value_1
# тернарный оператор

#1)
# tuple_ = tuple(['a', 'b', 'c'])
#2)
# lst_ = list(tuple_)
#3)
new_tuple = 'a', 2, 'python'
a, b, c = new_tuple
# new = (i=x for i in lst_ for x in n)
# print(list(new))

# #4)
# tup = ([1, 2, 3],)
# for i in tup[0]:
#     print(i)


"""
Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""






"""
Уникальные элементы в списке
Дан список. Выведите те его элементы, которые встречаются в списке только один раз. 
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""
dict_ = {}
lst_ = ['a', 'b', 'c', 'c', 1, 3, 3, 't']
for i in lst_:
    dict_[i] = dict_.get(i, 0) + 1
new_l = []
for key, value in dict_.items():
    if value == 1:
        new_l.append(key)



"""
Sorted list
"""

lst_ = [1, 2, 8, 0, 7, 0, 4, 10, 12, 89, 0, 0, 74]
new = [num for num in lst_ if num] + [0]*lst_.count(0)
print(new)