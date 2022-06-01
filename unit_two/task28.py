#todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07
#
# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.

from datetime import datetime

def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


@counter
def render(text):
    text.upper()

render("hello world")
render("it is a beautiful day")
print('render' + ', ' + str(render.count) + ', ' + str(datetime.now()))

@counter
def show(text):
    text.replace(' ', '_')

show("hello")
show("world")
show("it is")
show("a beautiful")
show("day")
print('show' + ', ' + str(show.count) + ', ' + str(datetime.now()))

file = open('debug.log', 'a')
file.write('render' + ', ' + str(render.count) + ', ' + str(datetime.now()) + '\n')
file.write('show' + ', ' + str(show.count) + ', ' + str(datetime.now()) + '\n')
file.close()
