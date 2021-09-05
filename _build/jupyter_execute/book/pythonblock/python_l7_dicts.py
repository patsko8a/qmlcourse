#!/usr/bin/env python
# coding: utf-8

# # Словари
# 
# ## Описание лекции
# 
# В этой лекции мы расскажем про:
# - то, что такое `dict`;
# - методы и примеры использования;
# - хранение изменяемых и неизменяемых типов;
# - хэширование.
# 
# ## Что такое `dict`
# `dict` (от английского _"dictionary"_, словарь) -- еще один тип данных в Python. Словари хранят пары `ключ`: `значение`. То есть в списках можно достать элемент, если указать его позицию в виде целого числа, а в словарях -- тот самый `ключ`. Обратите внимание, `dict` -- **неупорядоченный** тип данных, поэтому достать элемент по номеру не получится, но отображение содержимого будет **в порядке добавления** элементов. **Уникальность** ключей должна поддерживаться, чтобы всегда можно было быстро найти одно единственно верное `значение`.
# 
# В некоторых языках программирования можно встретить ассоциативные массивы -- полную аналогию `dict`. Также вспомним  базы данных: в таблице можно установить первичный ключ, который уникально идентифицирует запись, как и `ключ` соответствует `значению` в словаре.
# 
# ### Создание словаря
# 
# Использовать словарь стоит, когда нужно сохранять объекты с какими-то ключами и обращаться к объектам по известным ключам. Один из способов определения словаря: указание пар `ключ`: `значение` через **запятую** внутри фигурных скобок `{}`. Напоминает `set`, правда? `{}` позволяет создать **пустой** словарь, но не пустое множество.
# 
# Например, вы решили упростить себе жизнь и больше не запоминать дни рождения коллег. Вместо этого, лучше хранить их в одном месте:

# In[1]:


# локально попробуйте поменять значение переменной dates
dates = {"Кунг Фьюри": "1968-09-09", "Наташа Романова": "1985-03-15"}  


# В примере `dates` имеет две пары значений. В первой паре строка `"Кунг Фьюри"` является _ключом_, а `"1968-09-09"` -- его _значением_.
# 
# ### Получение значения по ключу
# 
# Чтобы получить значение по ключу, необходимо обратиться к переменной, содержащей словарь, и указать ключ в квадратных скобках `[]`:

# In[2]:


dates["Кунг Фьюри"]


# Если указать неверный ключ в `[]`, Python будет ругаться, выбросит исключение `KeyError` и перестанет выполнять код. Чуть ниже посмотрим, как можно избежать таких ситуаций.

# In[3]:


# пока этого ключа нет в словаре, будет ошибка при обращении
# поэтому используем перехват ошибок
try:
    print(dates["Капитан Ямайка"])

except KeyError as e:
    print(f"Ключа действительно нет: {e}")


# ### Изменение и добавление значений
# 
# Синтаксис изменения значения по ключу и добавления нового ключа со значением одинаковый: в `[]` нужно указать ключ, поставить `=` и указать значение, которое теперь будет соответствовать ключу.

# In[4]:


# этот ключ уже был в примере
dates["Кунг Фьюри"] = "1960-09-09"

# а такого не было
dates["Капитан Ямайка"] = "1930-10-04"


# Если ключ уже был в словаре, значение по нему изменится на новое, а **старое будет удалено**. Указание нового ключа со значением добавляет пару в словарь.
# 
# ## Основные методы словаря
# 
# ### Проверка вхождения и get()
# Помните, ранее говорили, что обращение к несуществующему ключу приводит к ошибке? Пришло время посмотреть пару способов борьбы!
# 
# Можно проверить, есть ли интересующий ключ среди множества ключей словаря. Это делается при помощи бинарного оператора `in`. Слева должен быть указан ключ, справа -- переменная со словарем:

# In[5]:


# еще способ создания: пары можно передавать как аргументы dict через =
marks = dict(линал=100, английский=92)

# False
print("матан" in marks)

# True
print("линал" in marks)


# В коде проверку можно использовать в условной конструкции `if`, чтобы принимать решение в зависимости от наличия ключа:

# In[6]:


if "матан" in marks:
    print(marks["матан"])

else:
    print("Нет оценки по матану :(")


# Теперь о методе `get()`: при помощи него тоже можно получать значения из словаря по ключу. `KeyError` никогда не появится: если ключа нет, по умолчанию возвращается `None`:

# In[7]:


empty_dict = {}  

# None
print(empty_dict.get("ключ"))


# Вторым аргументом метода `get()` можно указать значение, которое должно возвращаться вместо None, когда ключ не был найден:

# In[8]:


# теперь будет возвращено значение -1
print(empty_dict.get("ключ", -1))


# ### Что такое "длина словаря"?
# Функция `len()` для словаря будет возвращать количество пар `ключ`: `значение`, которое в нем содержится:

# In[9]:


# empty_dict -- пустой словарь, поэтому длина равна 0
print(len(empty_dict))

# а вот словарь marks уже содержит две пары, поэтому длина 2
print(len(marks))


# ### Удаление из словаря
# Есть несколько способов очистки в словаре: можно убирать по ключу, а можно сразу удалить все!
# 
# Сначала рассмотрим первое:
# 1. при помощи инструкции del (от английского _"delete"_) можно удалить пару `ключ`: `значение` (_замечу, что удаление ключа эквивалентно удалению пары `ключ`: `значение`, так как мы теряем возможность найти то самое `значение`_), в общем виде:
# 
# ```python
# # таким образом из словаря "словарь" будет удален ключ "название_ключа"
# # и соответствующее ему значение
# del словарь[название_ключа]
# ```
# 
# Предположим, коллега из самого первого примера уволился и больше нет смысла хранить его день рождения:

# In[10]:


# из словаря dates удаляется ключ "Наташа Романова"
del dates["Наташа Романова"]
print(dates.get("Наташа Романова"))


# 2. `pop()` -- метод, который достает значение, хранящееся по переданному ключу, и **сразу** удаляет ключ из словаря:

# In[11]:


# еще один способ создания словаря из последовательности пар
holidays = dict([("January", [1, 2, 3, 4]), ("Feburary", [23]), ("March", [8])])

# pop() возвращает значение, соответствующее ключу, значит его можно присвоить
# переменной
january_days = holidays.pop("January")

# напечатается соответствующий массив
print(january_days)


# Для метода `pop()` есть возможность указать значение, которое будет возвращено при обращении к несуществующему ключу. Почти как `get()`, но все таки, без указания этого значения, `pop()` выбрасывает `KeyError` ☝️
# 
# 3. `popitem()` имеет схожее название, но не путайте с предыдущим методом: этот на вход не принимает `ключ`, а возвращает пару `ключ`: `значение`, которая была добавлена последней (_такое поведение гарантируется с Python **3.7**_).

# In[12]:


# в результате -- последняя добавленная пара
print(holidays.popitem())


# 4. `clear()` позволяет удалить сразу все ключи словаря, то есть полностью его очистить:

# In[13]:


# вернемся к предыдущему примеру
# словарь становится пустой
holidays.clear()

# значит, длина равна 0
print(len(holidays))


# Обратите внимание на то, как работают методы `pop()`, `popitem()` и `clear()`: как только вызываются, словарь меняет свой состав (_изменения происходят in place_).
# 
# ### Обновление и добавление ключей
# Мы уже видели, что значения в словарь можно добавлять или менять, обращаясь по ключу. Python предоставляет возможность не писать кучу присваиваний, а использовать лаконичный метод `update()`, который на вход может принимать либо
# - другой словарь
# - пары `ключ`: `значение` в какой-то последовательности (например, тьюплы по два значения в списке: первое -- ключ, второе -- значение)

# In[14]:


# создадим два словаря: в первом уже есть два ключа
quidditch_team = {"Fred Weasley": "3rd year", "George Weasley": "3rd year"}

# во втором -- один ключ
new_members = {"Harry Potter": "1st year"}

# добавим пары из new_members
# метод update() также работает in place, поэтому после выполнения данной
# строки кода, в словаре quidditch_team станет три ключа
quidditch_team.update(new_members)

print(quidditch_team["Harry Potter"])


# А что, если в `update()` передать пары, ключ которых уже был в словаре? Значения по дублирующимся ключам будут **перезаписаны** на новые:

# In[15]:


# данный ключ (то, что записано первым в тьюпле) уже есть в quidditch_team
member_update = [("Harry Potter", "2nd year")]

# значение, соответствующее "Harry Potter", будет переписано
quidditch_team.update(new_members)

print(quidditch_team["Harry Potter"])


# ## Доступ к ключам и значениям
# В Python можно без проблем доставать отдельно ключи или значения или  итерироваться по элементам словарей в цикле `for`. Осталось разобраться, как это работает.
# 
# ### Ключи
# По умолчанию, в конструкциях вида
# ```python
# # после in указано название переменной, хранящей словарь
# for key in dict_var:
#     ...
# ```
# 
# переменные цикла (тут -- `key`) будут принимать значения из множества **ключей** словаря. Аналогично можно использовать метод `keys()` (_позволяет достать все ключи_), который явно говорит, что ваш цикл идет по ключам, например:

# In[16]:


# словарь в качестве ключей хранит имена игроков
for player in quidditch_team:

    # на каждой итерации будет напечатан ключ и значение
    print(player, quidditch_team[player])


# ### Значения
# При помощи метода `values()` можно получить все значения, хранящиеся по всем ключам словаря:

# In[17]:


# можно создать переменную со всеми значениями словаря
school_years = quidditch_team.values()


# Приведем пример с циклом:

# In[18]:


# словарь в качестве значений хранит годы обучения
for year in quidditch_team.values():

    # на каждой итерации будет год обучения игрока
    print(year)


# Напрямую по значению получить ключ нельзя.
# 
# ### Все и сразу
# Существует метод `items()`, который достает пары `ключ`: `значение` в виде последовательности тьюплов 👏 Его же часто удобно использовать в циклах, чтобы не тащить длинную запись в виде названия словаря и квадратных скобок с ключом при обращении к значению:

# In[19]:


# сразу две переменные: первая последовательно будет ключами,
# вторая -- значениями
for player, year in quidditch_team.items():

    # items() избавляет от необходимости обращаться quidditch_team[player],
    # чтобы получить значение. Оно уже в year
    print(f"Player {player} is in {year}")


# ## Сортировка
# Функции `reversed()` (с Python **3.8**) и `sorted()` доступны и для словарей. По умолчанию ключи словаря поддерживают порядок, в котором были добавлены, но можно отсортировать их в нужном направлении (_в зависимости от типа_):

# In[20]:


# вспомним про рабочие дни
week = {7: "weekend", 6: "weekend", 1: "workday"}

# в sorted_week окажутся ключи, отсортированные в порядке возрастания
sorted_week = sorted(week)
print(f"Порядок возрастания: {sorted_week}")

# а тут -- наоборот
reverse_sorted_week = reversed(week)
print(f"Наоборот: {reverse_sorted_week}")


# Не забудьте, когда в функции передается просто название переменной со словарем, работа идет только над множеством ключей.
# 
# Можно ли отсортировать словарь по значениям? Да, можно попробовать самостоятельно разобраться с аргументами функции [`sorted()`](https://docs.python.org/3/howto/sorting.html) 😉
# 
# ## Что можно хранить
# Теперь добавим немного технических подробностей: возможно, вы уже заметили самостоятельно, что `dict` может принимать в качестве ключа не всякое значение. На самом деле только **хэшируемые** объекты _(можно вызвать функцию `hash()` и получить значение)_ могут быть ключами словаря, на значения это ограничение не распространяется. В `dict` и `set` значение хэша от объекта используется для поиска внутри структуры.
# 
# Ключом словаря нельзя сделать объект **изменяемого** типа, например, `list`, `set` или **сам `dict`**, так как значение их хэша может измениться со временем. Неизменяемый тьюпл может быть ключом только если не содержит внутри изменяемые объекты.
# 
# ### Изменяемость и неизменяемость
# _В англоязычной литературе изменяемые типы называют **mutable**, а неизменяемые -- **immutable**, [почитать документацию](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types)_
# 
# В Python все -- объект. Когда пользователь присваивает значение переменной, она начинает ассоциироваться с ячейкой памяти, где лежит это значение. Переменная знает адрес, откуда можно получить значение. `id()` и `hex()` показывают адрес в памяти компьютера. _`id()` - адрес в десятичном виде, а `hex()` поможет перевести в _шестнадцатеричный_.
# 
# По адресу лежит так называемое **внутреннее состояние** переменной:
# - **неизменяемые** типы не позволяют менять внутреннее состояние, значение переменной может поменяться только вместе с адресом
# 
# - **изменяемые** типы позволяют менять внутреннее состояние переменной при сохранении адреса (возвращаемое `id()` значение не меняется, но _значение_ переменной каким-то образом преобразовывается). Изменение по ссылке называется изменением _in place_
# 
# #### Неизменяемые типы
# Из стандартных неизменяемыми являются:
# - `int`
# - `float`
# - `bool`
# - `str`
# - `tuple`
# 
# Давайте сразу рассмотрим пример:

# In[21]:


counter = 100

# полученное вами значение адреса может отличаться
print(counter, hex(id(counter)))


# ```{figure} /_static/pythonblock/dicts_l7/Python-Immutable-Example-1.png
# :name: mutable_example1
# :width: 411px
# 
# `counter` указывает на 100
# ```
# 
# А теперь поменяем значение `counter`:

# In[22]:


counter = 200
print(counter, hex(id(counter)))


# Кажется, что раз значение переменной `counter` поменялось, то и содержимое по предыдущему адресу изменилось? Нет, на самом деле `counter` теперь указывает в другое место:
# 
# 
# ```{figure} /_static/pythonblock/dicts_l7/Python-Immutable-Example-2.png
# :name: mutable_example1
# :width: 411px
# 
# `counter` указывает на новое значение 200 с другим адресом
# ```
# 
# Из интересного: Python [заранее создает объекты](https://docs.python.org/3/c-api/long.html#c.PyLong_FromLong) для чисел от -5 до 256, поэтому для переменных со значением из этого диапазона берутся заранее готовые ссылки.

# In[23]:


# создадим две переменные с одинаковыми значениями в диапазоне от -5 до 256
a = 20
b = 20

# a и b указывают на одно и то же место в памяти
# попробуйте у себя поменять значение a и b на число больше 256 или меньше -5
id(a) == id(b)


# #### Изменяемые типы
# Стандартные изменяемые типы это:
# - `list`
# - `set`
# - `dict`
# 
# У списков есть метод `append()`, позволяющий добавить в него значение:

# In[24]:


# создадим список и напечатаем его адрес
ratings = [1, 2, 3]
print(f"Было: {hex(id(ratings))}")

ratings.append(4)
print(f"Стало: {hex(id(ratings))} - ничего не поменялось!")


# ```{figure} /_static/pythonblock/dicts_l7/Python-Mutable-Example.png
# :name: mutable_example1
# :width: 402px
# 
# Начальное состояние списка содержало три элемента
# ```
# 
# После добавления еще одного, адрес `ratings` не изменился.
# 
# ```{figure} /_static/pythonblock/dicts_l7/Python-Mutable-Example-2.png
# :name: mutable_example2
# :width: 402px
# 
# После добавления элемента поменялось лишь внутреннее состояние
# ```
# 
# 
# ## Что мы узнали из лекции
# - Новый тип данных -- **словарь**! Позволяет хранить соответствие `ключ`: `значение`;
# - Несколько способов создания `dict`, примеры:

# In[25]:


# при помощи "литерала" - фигурных скобок {}
flowers = {"roses": "red", "violets": "blue"}

# при помощи вызова dict()
#   и последовательности с парами значений
anime = dict([("Ведьмак", "Кошмар волка"),
("Призрак в доспехах", ["Призрак в доспехах", "Синдром одиночки", "Невинность"])])

#   и "="
literature = dict(poem_flowers=flowers)

print(f"""flowers = {flowers}
anime = {anime}
literature = {literature}""")


# - методы для изменения состояния или получения доступа к элементам:

# In[26]:


# доступ к элементу, если ключа нет - ошибка
print(flowers["violets"])

# при помощи get()
print(flowers.get("magnolias"))


# In[27]:


days = ["Пн", "Вт", "Ср", "Чт", "Пт"]

# создадим пустой словарь
numbered_days = {}

# будем добавлять в него элементы в цикле
for num in range(len(days)):
    numbered_days[num] = days[num]

# получим отдельно ключи и значения
# пары из tuple можно сразу получить при помощи метода items()
keys = numbered_days.keys()
values = numbered_days.values()

print(f"""Ключи: {keys}
Значения: {values}""")


# - Требование к ключу: возможность хэширования, свойство ключа внутри словаря: уникальность;
# - Разобрали изменяемые и неизменяемые типы данных.
