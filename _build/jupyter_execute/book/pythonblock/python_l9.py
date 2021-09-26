#!/usr/bin/env python
# coding: utf-8

# (python_l9=)
# 
# # Функции
# 
# ## Описание лекции
# 
# В этой лекции мы расскажем про:
# - функции и их смысл;
# - локальность переменных;
# - параметры и аргументы;
# - декораторы.
# 
# ## Что такое "функция" в Python
# В общем случае функцией можно назвать набор связанных инструкций, которые выполняют определенную задачу. Функции во всех языках программирования помогают:
# - структурировать код и улучшить читаемость
# - переиспользовать код и не изобретать велосипед
# - уменьшать количество мест, в которых можно ошибиться при копировании и вставке кода
# 
# В Python функции можно разделить на три типа:
# - встроенные ([список built-in функций](https://docs.python.org/3/library/functions.html))
# - именованные (определенные пользователем при помощи `def`)
# - анонимные (`lambda`-функции)
# 
# **Все** функции являются объектами типа `function`.
# 
# На самом деле, вы уже использовали встроенные функции, например:
# - `print()` для вывода данных на экран
# - `str()` для создания объектов строкового типа
# - `type()` для определения типа объекта
# 
# Ими можно пользоваться как черным ящиком, который принимает что-то на вход и творит свою магию. О том, что готовые функции ожидают получить, написано в документации вместе с описанием принципа работы.
# 
# ```{tip}
# После разбора лекции советую открыть [документацию `print()`](https://docs.python.org/3/library/functions.html#print), например, и разобраться с подробностями работы`
# ```
# 
# Очевидно, стандартные функции дают лишь базовый инструментарий. Реализовать более сложную логику можно самостоятельно.
# 
# **Пример**:
# 
# Представим, что необходимо находить количество корней квадратного уравнения - это легко можно реализовать на Python!

# In[1]:


def count_roots(a, b, c):

    d = b**2 - 4 * a * c
    if d == 0:
        return 'один'

    elif d < 0:
        return 'нет корней'

    else:
        return 'два'


# ## Именованные функции
# ### Определение
# Определение функции позволяет **создать объект** функции. После определения к функции можно будет обратиться по заданному имени и получить результат ее работы.
# 
# В Python существует особый синтаксис определения именованных функций:
# 1. в начале - ключевое слово `def`
# 2. название функции
# 
#     Существуют правила и рекомендации по именованию функций:
#     - **правила**:
#       - название не может начинаться с числа
#       - можно использовать нижнее подчеркивание `_`, цифры и буквы
#     - **рекомендации**:
#       - `snake_case`: в названии только буквы нижнего регистра, слова разделяются `_`
# 
# 3. круглые скобки и, опционально, параметры внутри _(о них ниже)_
# 4. двоеточие, переход на новую строку
# 4. тело функции, выделенное отступом - набор инструкций, который "выполняет работу"
# 
# Код в Python организован в блоки и именно отступы дают понять, где у блоков начало и конец. Все тело функции должно располагаться минимум в одном отступе от начала строк.
# 
# ```python
# def название_функции(позиционные, *доп_позиционные, именованные, **доп_именованные_параметры):
#     инструкция 0
#     инструкция 1
#     ....
#     инструкция N
# ```
# 
# Давайте напишем простейшую функцию, которая будет печатать две фразы:

# In[2]:


# первым делом - def
# далее - имя функции "print_theme"
# после - круглые скобки, сейчас пустые. Потом : и переход на новую строку
def print_theme():

    # тело функции из двух вызовов print(), оба с единообразным отступом
    print('Лекция про функции!')
    print('Тело кончилось')


# ### Вызов
# После определения функции появляется возможность к ней обращаться (вызывать). Делается это просто: указывается имя функции, круглые скобки и, опционально, аргументы в них.

# In[3]:


# выше была определена print_theme, ее и вызовем
print_theme()


# ### Возвращаемое значение
# Функция может не только производить какие-то действия, но возвращать наружу результат своей работы. Для этого используется ключевое слово `return`:

# In[4]:


# определим функцию, которая принимает на вход x
def add_two(x):

    # переменная result - сумма x и 2
    result = x + 2

    # "наружу" возвращается полученное значение
    return result


# На самом деле, любая функция что-то возвращает:
# - указанное значение при наличии `return`
# - `None`, когда return отсутствует
# 
# Возвращение результата означает, что его можно использовать вне функции, например, присвоить полученное значение переменной. Давайте посмотрим, что возвращает `print_theme()` и `add_two()`:

# In[5]:


# Присвоим результат выполнения функции переменной и посмотрим, что в ней
from_print_theme = print_theme()
print(from_print_theme)


# Как видите, несмотря на отсутствие `return` в коде функции, она действительно возвращает `None`.
# 
# Теперь посмотрим на `add_two()`, где возвращаемое значение задано нами:

# In[6]:


# add_two при вызове ожидает получить число: сложим 2 и 2
from_add_two = add_two(2)
print(from_add_two)


# ## Пространства имен и области видимости
# Чуть выше была определена `add_two()`, внутри которой инициализировалась переменная `result`. Можно ли получить значение, обратившись к ней вне функции? Нет:

# In[7]:


# ошибочка!
# тут магическая конструкция try - except, которая "ловит" исключения и не
# дает коду перестать работать из-за ошибки
try:
    print(result)
except NameError as ne:
    print(ne)


# Почему так происходит? Функции обладают своим пространством имен: переменные, которые определены внутри, не видны извне. Однако, функция может получать доступ к переменным, которые определены снаружи. Давайте опишем чуть более формально.
# 
# В Python объектам можно давать имя и по этому имени обращаться, эти названия организованы в пространства имен или неймспейсы _(от английского 'namespace')_. Инициализация переменной добавляет в неймспейс название объекта. Неймспейс - набор имен определенных на текущий момент объектов. Представьте себе `dict`, где ключом является строка, а значением - ссылка на объект. Область видимости определяет, переменные из каких пространств имен сейчас доступны. Разберем, как и где Python ищет объекты, к которым обращаются.
# 
# Неймспейсы и области видимости можно разделить на несколько типов:
# - локальные (**L**ocal) - локальные переменные функции, данная область существует до тех пор, пока функция не завершит работу после вызова
#  - локальные пространства могут быть вложены друг в друга, в таком случае область уровня N (**E**nclosing) содержит "более глубокую" N + 1.
# Поиск имени, вызванного на уровне N, начинается с локального неймспейса этого уровня и продвигается "наружу", то есть на уровни выше
# - глобальные (**G**lobal) - все объекты, определенные на уровне скрипта
# - встроенные (**B**uilt-in) - неймспейс содержит все встроенные объекты (функции, исключения и т.д.), поиск в нем осуществляется последним
# ```{figure} /_static/pythonblock/functions_l9/legb.png
# :name: legb
# :width: 500px
# ```
# 
# 
# Если имя не было разрешено даже на уровне Built-in, будет выброшено исключение `NameError`.

# In[8]:


z = 'name'

def foo():
    # в foo не определена своя z, но она успешно найдется в глобальной области
    print(z)
    a = 10
    b = -5

    def bar():
        # bar успешно напечатает a, при этом значение будет найдено в
        # неймспейсе foo
        # как думаете, где находится print?
        # в built-in, то есть самой "внешней" области
        print(a)

        # создадим переменную b внутри bar
        b = 20

        # будет напечатано 20, так как поиск увенчается успехом в локальном
        # неймспейсе
        print(b)

    bar()

    # если тут раскомментировать следующую строку, будет ошибка: foo не знает
    # ничего про внутренности bar
    # print(b)

foo()


# ```{tip}
# Хотим заметить, что нужно быть аккуратными при использовании вложенных функций и следить за тем, где и какие переменные определены и меняются. В рамках курса вообще не советуем так делать, чтобы не запутаться. Единственное исключение - декораторы, описанные ниже.
# ```
# 
# ## Параметры
# Наша функция `add_two()` или, например, `type()` ожидают, что на вход будут переданы какие-то аргументы для успешной работы, а вот `print()` можно вызвать и с ними, и с пустыми скобками. В начале лекции был представлен скелет функции, сейчас разберем, что же находится в скобках.
# 
# Для начала немного формализма:
# - при определении функции в скобках пишутся параметры, которые функция может принять
# - при вызове функции в скобках указываются аргументы, которые задают значения параметров внутри функции
# 
# То есть имеется отображение: аргументы, с которыми вызывается функция -> значения параметров.
# 
# Переменные с названиями параметров могут быть использованы внутри тела функции, как будто их значения известны.
# 
# ### Позиционные параметры
# Позиционные параметры выглядят как перечисленные внутри скобок названия переменных, используемых внутри функции:

# In[9]:


# в данном случае есть два позиционных параметра
def foo(arg1, arg2):
    print(arg1, arg2)


# Данный тип характеризуется следующим:
# - позиционные параметры идут первыми после открытых скобок, все именованные строго после них
# - важен порядок: отображение аргументов в параметры будет последовательным
# - при вызове функции все аргументы, которые ожидает функция, должны быть переданы (откуда иначе Python возьмет значения? вот именно!)
# 
# Разберем пример, который суммирует два числа:

# In[10]:


# в данном случае есть два позиционных параметра
def two_var_sum(var1, var2):

    # функция возвращает вычисленное значение суммы
    return abs(var1) + var2

# порядок важен!
print(two_var_sum(-1, 2), two_var_sum(2, -1))

# можно явно задавать переменные при вызове, в таком случае порядок не играет
# роли. Указывается название параметра и значение после =
print(two_var_sum(var2=2, var1=-1))


# А что, если количество входных переменных очень большое или вы заранее не знаете, сколько аргументов будет передано при вызове? Например, вам нужно сложить не 2 числа, а 102? В Python есть специальный синтаксис со звездочками. После позиционных аргументов можно указать `list`, элементами которого станут неограниченное количество переданных позиционных аргументов.
# 
# Синтаксис: `имя_функции([поз0, ..., позN,] *поз_список): ...` - `[]` в данном случае обозначают необязательность.

# In[11]:


# тут позиционных аргументов нет (такое тоже может быть), поэтому сразу
# используется синтаксис со *: список, куда попадут все переданные позиционные
# аргументы, тут называется vars
def many_var_sum(*vars):

    # функция возвращает вычисленное значение суммы
    return sum(vars)

many_var_sum(1, 2, 3, 4, 5, 6)


# ```{tip}
# Совет: лучше передавать все в списках или векторах (о которых расскажут позже)
# ```
# 
# ### Именованные параметры
# Данные параметры имеют значения по умолчанию.  
# 
# Синтаксис: `имя_функции(все позиционные и *, им0=значение0, им1=значение1, ..., имK=значениеK, **им_словарь): ...`
# 
# характеризуются следующим:
# - в определении идут строго после позиционных параметров
# - в определении дано значение по умолчанию через `=` после имени
# - при вызове необязательно передавать - тогда будет использовано значение по умолчанию

# In[12]:


# тут есть один позиционный параметр и один именованный
def hello(name, phrase='Привет'):

    print(f'{phrase}, {name}')

# передавать значения аргументов можно как в исходном порядке, тогда
# параметру будет присвоено соответствующее значение
hello('Саша', 'Приветствую')

# так и указывая названия параметров
hello(phrase='Здорова', name='Игорь')

# если не указать значение именованного параметра, используется дефолтное
hello('Вася')


# Аналогично позиционным аргументам, если необходимо передать множество именованных параметров, используется синтаксис со звездочками. В данном случае все переданные именованные аргументы, если не определены явно, попадут в `dict`, указанный после **:

# In[13]:


def congrats(today, everyone=False, **names):
    """
    Функция может поздравляет людей
    Args:
        today (str): сегодняшняя дата
        everyone(bool): флаг, нужно ли поздравить всех
        names (dict): отображение имя: дата
    """

    if everyone:
        print('Happy Birthday!')

    else:
        for name, date in names.items():
            if date[-5:] == today[-5:]:
                print(f'Happy Birthday, {name}')

congrats('2021-09-17', Paul='2001-03-08', Lena='1997-01-31', Mark='1997-09-17')


# Что это за комментарий в кавычках внутри функции? Это один из общепринятых способов написания [docstring](https://www.python.org/dev/peps/pep-0257/) - описания деталей работы функции.
# 
# ## Анонимные функции
# Функции, определенные при помощи `def`, имеют название, по которому можно обратиться, но также существуют и анонимные или неименованные функции.  
# Такие функции могут быть определены при помощи оператора `lambda`. Он позволяет задать входные и выходные данные. Вы можете попробовать самостоятельно почитать [документацию](https://docs.python.org/3/reference/expressions.html#grammar-token-lambda-expr).
# 
# ```python
# # синтаксис анонимных функций простой
# lambda [арг0, ..., аргN]: выражение
# ```
# 
# В определении `выражение` собой то, что будет возвращено из анонимной функции:

# In[14]:


lambda x: abs(x)

lambda num, div=2: 'нет' if num % div else 'да'


# В примере выше `lambda`-функции были только созданы в моменте, но не вызваны. Можно сказать, что мы их определили (как с `def`), но не воспользовались и, по сути, сразу потеряли.
# 
# Для удобства можно присвоить переменной объект функции и по этому имени к ней обращаться:

# In[15]:


# сохранили в check_div функцию
check_div = lambda num, div=2: 'нет' if num % div else 'да'

# вызов совершенно обычный
print(check_div(3), check_div(5, 5))

# если без сохранения в переменную:
print((lambda x: abs(x))(-120))


# Данные функции можно применять, когда нужна одноразовая функция или лень писать лишнюю строку с `def`.
# 
# ## Декораторы
# Полезный концепт Python - декоратор. Это функция, которая принимает на вход другую функцию и возвращает функцию. Звучит непонятно на первый взгляд. На деле декораторы помогают расширять возможности функций не меняя их кода.
# 
# Давайте сразу разберем пример:

# In[16]:


import time

# на вход декоратор принимает параметр func - оборачиваемую функцию
def time_decorator(func):

    # внутри определена функция, которая "заменит" переданную
    # wrapped будет засекать, за сколько выполняется переданная функция
    def wrapped(*args):
        start = time.time()

        # почему func нет среди аргументов wrapped?
        # все аргументы, которые примет wrapped, тут передаются в func
        result = func(*args)

        end = time.time()
        print(f'Прошло {end - start} секунд')

        return result

    # возвращает декоратор тоже функцию. обратите внимание, что
    # возвращаемое значение именно объект function: после имени нет круглых
    # скобок. если бы они были, возвращался бы результат выполнения wrapped,
    # так как wrapped() - вызов функции
    return wrapped


# Выше определена функция `many_var_sum()`, давайте засекать, сколько она работает:

# In[17]:


# сохраним обернутую функцию (помним, декоратор возвращает функцию) в
# переменную, обратите внимание, что на вход декоратору передается также
# объект самой функции, а не результат ее работы
many_var_sum = time_decorator(many_var_sum)

# поведение функции поменялось, а код - нет
summed = many_var_sum(10, 0, -120, 333)


# Отлично, но можно добавить так называемый **синтаксический сахар**: вместо присваивания значения над определением функции можно указать специальный символ `@`, после которого указывается название декоратора:

# In[18]:


# теперь, при вызове, stupid_power сразу будет обернута!
@time_decorator
def stupid_power(x, power=5):
    result = 1
    for p in range(power):
        result *= x
    return result

powered = stupid_power(10)


# Таким образом, использования синтаксического сахара с `@` и указанием имени декоратора над функцией аналогично вызову `stupid_power = time_decorator(stupid_power)`.
# 
# ## Что мы узнали из лекции
# - Что такое функции и зачем их применять
# - Как определить функцию (инструкция `def`)
# ```python
# def название_функции(параметры):
#     тело функции
#     <return возвращаемые_значения>
# ```
# - Отличия позиционных параметров от именованных:
#   - порядок указания - *сначала* позиционные, *потом* именованные
#   - значения по умолчанию у именованных позволяют не указывать их при вызове
# - Синтаксис со звездочками для получения заранее неизвестного числа позиционных (`*some_list`) и именованных (`**some_dict`) аргументов
#   - в `*some_list` стоит **одна** *: эта конструкция для получения неограниченного количества позиционных/неименованных аргументов
#   - в `**some_dict` **две** *: все именованные аргументы, явно не указанные среди параметров, попадут туда
# - Что может возвращать функция при помощи `return`
#   - return обозначает выход из функции и передачу "наружу" результата работы
#   - в return можно перечислять несколько возвращаемых значений через запятую
# - Что такое декораторы и как они работают, щепотку синтаксического сахара с `@`
#   - использование декоратора эквивалентно сохранению результата вызова функции-декоратора с аргументом в виде оборачиваемой функции `stupid_power = time_decorator(stupid_power)`