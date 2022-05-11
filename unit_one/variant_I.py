#todo: I вариант (алгоритм сортировки вставками)
# Реализовать на Python алгоритм сортировки вставками представленный в псевдокоде
# в учебнике “Introduction to Algorithms”  на стр. 57 - 63.
#
# Задача.
# Перепишите процедуру INSERTION_SORT и отсортируйте последовательность
A = [31, 4, 59, 26, 41, 58, 1, -20, 100, -7]
# по убыванию.

def insertion_sort(a):
    for j in range(1, len(a)):
        key = a.pop(j)
        i = j - 1
        while (i >= 0) and (a[i] <= key):
            i -= 1
        a.insert(i + 1, key)
    print(a)
insertion_sort(A)
