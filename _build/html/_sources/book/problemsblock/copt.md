(copt)=
# Задачи комбинаторной оптимизации

В этой лекции мы поговорим об известных задачах комбинаторной оптимизации. Мы уже касались темы задач, для которых не существует эффективных классических алгоритмов в [обзоре квантовых алгоритмов](../qcalgo/quantum_algorithms_overview.html#id2), а сегодня разберем еще больше примеров таких задач. В конце мы кратко обсудим пару способов решать такие задачи на классических компьютерах, а также в чем их принципиальные проблемы и ограничения.

Лекция будет построена так:

- задача о максимальном разрезе в графе
- задача о выделении сообществ в графе
- задача о Гамильтоновых циклах и коммивояжере
- задача о рюкзаке
- метод ветвей и границ
- метод имитации отжига

Какого-то кода, или больших страшных формул из квантовой механики тут не будет, так что можно немного передохнуть, расслабиться и насладиться чтением. Для тех, кто хорошо знаком с задачами целочисленной оптимизации в этой лекции точно не будет ничего нового и ее можно будет пропускать, ну или пролистать по диагонали.

## Задача о максимальном разрезе в графе

Мы уже немного говорили об этой задаче в лекции про модель Изинга из-за их очень большого сходства. Но давайте еще раз вспомним, что это за модель такая. Ну и сразу рассмотрим ее максимально общий случай. Итак, у нас есть граф на множестве вершин $V$, связанных множеством ребер $E$. Каждое ребро имеет две инцедентных вершины $u,v$, в общем случае порядок $u,v$ важен, тогда мы говорим о направленном (directed) графе. Каждому ребру можно также сопоставить действительное число $w$, тогда у нас будет так называемый взвешенный граф. Наша цель разбить сообщество вершин $V$ на два непересекающихся сообщества $V_1, V_2$. Давайте сформулируем нашу функцию стоимости:

$$
C = \sum_{u,v,w \in E} w (\mathbf{1}(u \in V_1, v \in V_2) + \mathbf{1}(u \in V_2, v \in V_1))
$$

То есть в общем случае это просто сумма всех весов ребер между двумя сообществами. В общем случае эта задача является $NP$-полной. В теории к этой задаче можно также свести любую другую $NP$-полную задачу за полиномиальное время.

```{figure} /_static/problemsblock/ising/Max-cut.png
:width: 400px
:name: MaxCut

Иллюстрация задачи о максимальном разрезе в графе
```

## Задача о выделении сообществ в графах

Задача о выделении сообщества в графах это уже более практическая и понятная задача. Она находит применение во многих областях, но одно из самых очевидных применений -- это социология (в том числе анализ социальных сетей), когда мы хотим, анализируя контакты людей, выделить из них сообщества для дальнейшего анализа. Эта задача также является $NP$-трудной, так как существует экспоненциально много способов разбить вершины на множества. Хотя для этой задачи и известны относительно быстрые приближенные алгоритмы, нам очень трудно понять, насколько хорошее решение они дают для действительно больших графов.

```{note}
Для работы с графами мы будем пользоваться библиотекой `NetworkX`. Она написана на чистом `Python` и плохо подходит для работы с большими графами, зато имеет простой интерфейс и легко устанавливается на любую систему. Ее можно установить из репозитория `PyPI`, используя команду `pip install networkx`. Подробнее о пакетах `Python` можно почитать в [одной из вводных лекций](python_l1) про этот язык программирования.
```

Одним из первых известных наборов данных для задачи выделения сообществ является "Клуб каратэ Захари" (Zachary’s Karate Club) {cite}`zachary1977`. Для этого набора данных точно известно, к какому из двух сообществ принадлежит каждая из вершин. В этом клубе карате был внутренний конфликт, и одна часть людей была в группе одного из инструкторов (Mr. Hi), а другая в группе администратора (Officer).

```{code-cell} ipython3
import networkx as nx
import matplotlib.pyplot as plt

zachary = nx.generators.social.karate_club_graph()
nx.draw(
    zachary,
    node_color=[
        {"Officer": "r", "Mr. Hi": "b"}.get(dt["club"]) for _, dt
        in zachary.nodes(data=True)
    ],
)
plt.show()
```

Задачу о выделении сообществ в тривиальном случае разбиения графа на два подмножества можно свести к знакомой нам задаче о максимальном разрезе. Правда, в отличии от задачи о максимальном разрезе, в случае с сообществами мы хотим, что число ребер между ними было минимальным. Но это можно сделать просто поменяв пару символов в выражении для стоимости:

$$
C = \sum_{u,v,w \in E} w (\mathbf{1}(u \in V_1, v \in V_1) + \mathbf{1}(u \in V_2, v \in V_2))
$$

Но на самом деле мы только что свели более простую задачу о минимальном разрезе с неотрицательными весами к более сложной задаче Max-Cut. А еще выбранная нами метрика (количество ребер) не самый лучший вариант для этой задачи. Гораздо лучше подойдет модулярность (modularity), предложенная физиком Марком Ньюманом {cite}`newman_modularity`:

$$
Q(C) = \frac{1}{2 |E|}\sum_{e \in E} B_{e_{src}, e_{dst}}\delta (c_{e_{src}}, c_{e_{dst}})
$$

Тут $B$ -- это матрица модулярности (modularity matrix). Ее элементы определяются через степени $d_i$ соответствующих вершин графа (степень вершины -- это число ребер, связанных с данной вершиной) и матрицу смежности $A$ графа:

$$
B_{ij} = A_{ij} - \frac{d_i d_j}{2 |E|}
$$

Условно, модулярность это разница между числом ребер внутри сообществ в нашем графе и числом ребер внутри сообществ в графе с таким же числом ребер, но сгенерированным случайным образом. Это довольно сложное понятие, которое выходит за рамки нашего курса, но все равно потребуется нам, чтобы показать, что задачи оптимизации модулярности может быть сформулирована как задача Изинга.

```{note}
Это интересно, но одним из первых алгоритмов для решения задачи о выделении сообществ в графах был алгоритм имитации отжига, который изначально был создан именно для решения проблемы гамильтонианов типа Изинга. Причина заключается в том, что модулярность очень схожа по виду с выражением энергии для магнетиков.
```

Мы тут пока описали лишь простой случай модулярности для не взвешенного и ненаправленного графа. Но даже в таком случае для задачи точной оптимизации модулярности не известно полиномиального алгоритма решения. Поэтому обычно применяют приближенные или жадные алгоритмы и они вроде даже неплохо работают. Но мы почти не знаем насколько действительно далеко они от самых оптимальных решений, особенно для больших графов.

## Задача о Гамильтоновых циклах

Перед тем, как мы перейдем к интересной и важной задаче поиска Гамильтоновыз циклов мы вспомним задачу о мостах Кеннингсберга (Калининграда). Ведь именно гуляя по этому городу и пытаясь решить эту задачу Леонард Эйльер изобрел теорию графов. Суть задачи в том, что надо обойти все острова города, пройдя по каждому мосту лишь один раз и вернуться на тот остров, откуда мы начала. Эйлер, создав математический аппарат теории графов сумел доказать, что это невозможно, ну а дальше завертелось и вот мы с вами тут :)

```{figure} /_static/problemsblock/copt/bridges.png
:width: 300px

Мосты Кеннингсберга, думая о которых Эйлер изобрел теорию графов
```

Такой путь в графе, когда мы проходим по каждому ребру лишь один раз называется Эйлеров цикл. Но нам будет более интересен схожий класс циклов -- Гамильтоновы циклы. Это такие циклы, которые проходят через каждую вершину графа ровно один раз.

```{figure} /_static/problemsblock/copt/Hamilton.jpg
:width: 350px

Сер Уильям Роуэн Гамильтон, 1805 - 1865
```

Для Гамильтонова цикла мы можем ввести $N^2$ бинарных переменных $x_{i,p}$. Каждая переменная $x_{i,p}$ равна $1$, если $i$-я вершина находится на $p$-м шаге пути и $0$ если нет. Тогда легко ввести условия существования такого цикла:

$$
\begin{cases}
\sum_p x_{i,p} = 1\text{  }\forall i \\
\sum_i x_{i,p} = 1\text{  }\forall p \\
x_{i, p} = 1 \land x_{j, p + 1} = 0\text{ }\forall i,j \notin E
\end{cases}
$$

Тут первое условие говорит нам о том, что каждая вершина должна попасть в путь. Второе условие говорит о том, что каждый шаг пути содержит строго одну вершину. Ну а третий шаг это просто утверждение о том, что между вершинами соседних шагов пути должно быть ребро. На самом деле, эти три условия можно переписать в единую функцию стоимости:

$$
C = (1 - \sum_i x_{i,p})^2 + (1 - \sum_p x_{i,p})^2 + \sum_{u,v \notin E} x_{u,p} x_{v,p+1}
$$

Правда в этом случае мы должны минимизировать, а не максимизировать эту величину.

## Задача коммивояжера

Задачу коммивояжера мы (а точнее наш смартфон) решаем каждый раз, когда строим в `Google Maps` маршрут, включающий несколько точек. Зная, как формулируется задача о Гамильтоновы циклах сформулировать задачу коммивояжера очень легко.

```{figure} /_static/intro1block/intro1/Salesman.png

Иллюстрация задачи коммивояжера
```

По сути нам требуется взять все Гамильтоновы циклы и выбрать из них тот, для которого сумма весов по содержащимся в нем ребрам будет минимальной. Но надо помнить, что цикл обязательно должен быть в первую очередь Гамильтоновым, поэтому мы добавим веса слагаемых в выражении для стоимости, причем веса, отвечающие за сам цикл будут больше:


$$
C = A (1 - \sum_i x_{i,p})^2 + A (1 - \sum_p x_{i,p})^2 + A \sum_{u,v \notin E} x_{u,p} x_{v,p+1} + B \sum_{u,v,w \in E} w x_{u,p} x_{v,p+1}
$$

Тут $A,B$ это веса, которые лучше выбирать так, что $0 < Bw < A\text{ }\forall u,v,e \in E$.

## Задача о рюкзаке

_Тут будет описание_


## Метод ветвей и границ

_пусто_

## Метод имитации отжига

_пусто_

## Заключение

_что-то тут точно будет_