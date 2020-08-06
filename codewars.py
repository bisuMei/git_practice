# import calendar

# def frequency_sort(lst):
#     new_lst = []
#     dict_ = {}
#     final = []
#     for i in lst:
#         dict_[i] = dict_.get(i, 0) + 1
#     while dict_:
#         max_ = max(dict_, key=lambda x: dict_[x])
#         val = dict_.get(max_)
#         new_lst.append(max_)
#         final.extend(new_lst * val)
#         dict_.pop(max_)
#         new_lst.clear()
#     return final
#
# print(frequency_sort([4, 2, 6, 2, 2, 6, 6, 4, 6]))


# def split_list(lst):
#     length = len(lst)
#     final = []
#     if length % 2 == 0:
#         lst_1 = lst[:length//2]
#         lst_2 = lst[length//2:]
#     else:
#         lst_1 = lst[:length // 2 + 1]
#         lst_2 = lst[(length // 2) + 1 :]
#     final.append(lst_1)
#     final.append(lst_2)
#     return final
#
# print(split_list([1, 2, 3, 4, 5, 6]))


# all_the_same([1, 1, 1]) == True


# def all_the_same(lst):
#     if len(lst) == 0:
#         return True
#     i_0 = lst[0]
#     for i in lst:
#         if i_0 != i:
#             return False
#     return True
#
# print(all_the_same([]))


# def date_time(str_):
#     lst = str_.split()
#     d_ = lst[0].split(".")
#     t_ = lst[1].split(":")
#     date_ = []
#     time_ = []
#     for i in d_:
#         d = i.lstrip('0')
#         date_.append(d)
#     month_ = calendar.month_name[int(date_[1])]
#     date_[1] = month_
#     for i in t_:
#         if i == "00":
#             t = i[1]
#             time_.append(t)
#         elif i[0] == '0':
#             t = i.replace('0', "")
#             time_.append(t)
#         else:
#             time_.append(i)
#
#     if time_[0] == "1" and time_[1] == "1":
#         final = " ".join(date_) + " year {} hour {} minute".format(time_[0], time_[1])
#     elif time_[0] == "1":
#         final = " ".join(date_) + " year {} hour {} minutes".format(time_[0], time_[1])
#     elif time_[1] == "1":
#         final = " ".join(date_) + " year {} hours {} minute".format(time_[0], time_[1])
#     else:
#         final = " ".join(date_) + " year {} hours {} minutes".format(time_[0], time_[1])
#
#     return final
#
#
# print(date_time("09.05.1945 09:30"))
