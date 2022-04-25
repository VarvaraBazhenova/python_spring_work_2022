#todo: Выведите все строки данного файла в обратном порядке.
# Для этого считайте список всех строк при помощи метода readlines().

# Содержимое файла import_this.txt
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
#
# выходные данные
# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.

file = open("import_this.txt", "r", encoding="utf-8")
rev_lst = file.readlines()[::-1]
rev_str = ""
for i in rev_lst:
    rev_str += i
res_str = rev_str.replace('.', '.\n', 1)
print(res_str)
