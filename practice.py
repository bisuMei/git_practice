# def binary_search(lst, item):
#     low = 0
#     high = len(lst) - 1
#
#     while low <= high:
#         mid = (low + high)
#         guess = lst[mid]
#         if guess == item:
#             return mid
#         if guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None
#
# lst_ = [1, 3, 5, 7, 9]
#
# print(binary_search(lst_, 3))


# def find_smallest(lst_):
#     smallest = lst_[0]
#     smallest_idx = 0
#     for i in range(1, len(lst_)):
#         if lst_[i] < smallest:
#             smallest = lst_[i]
#             smallest_idx = i
#     return smallest_idx
#
# def selection_sort(lst_):
#     new_lst = []
#     for i in range(len(lst_)):
#         smallest = find_smallest(lst_)
#         new_lst.append(lst_.pop(smallest))
#     return new_lst
#
# print(selection_sort([5, 3, 2, 10 , 6]))


# def sum_(lst_):
#     if lst_ == []:
#         return 0
#     else:
#         return lst_[0] + sum_(lst[1:])

# def quicksort(lst):
#     if len(lst) < 2:
#         return lst
#     else:
#         base = lst[0]
#         less = [i for i in lst if i < base]
#         great = [i for i in lst if i > base]
#     return quicksort(less) + [base] + quicksort(great)
#
# print(quicksort([2, 5, 8, 7, 4, 1]))

a = {}
a["start"] = {}
a["start"]["a"] = 6

print(a)
print("as")



