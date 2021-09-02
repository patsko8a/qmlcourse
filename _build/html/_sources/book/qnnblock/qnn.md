---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(qnn)=

# Квантовые нейронные сети

## Описание лекции

В этой лекции мы пройдёмся по расширению идеи нейронных сетей на квантовые компьютеры - мы уже прошли и вариационные квантовые схемы (**VQC**), и комбинацию квантовых и классических градиентов в них в соответствующем блоке. Всё что осталось это объединить всё изученное в общую картину и заняться обучением этих самых квантовых нейронных сетей.

## Введение

Как уже было упомянуто в лекции по **VQC**, на данный момент квантовые вычислители ещё недостаточно развиты для того, чтобы в одиночку решать большие проблемы, имеющие практическое значение для индустрии - это в особенной степени актуально среди нейронных сетей, которые и в классическом сценарии требуют значительных вычислительных ресурсов. Именно поэтому на данный момент наиболее популярна категория гибридных вариационных алгоритмов, которые обучают квантовую параметрическую схему (**QNN**) при помощи классической оптимизации, например, **VQ Eigensolvers** и **Quantum Approximate Optimization Algorithms**. В общем и целом идея гибридных алгоритмов заключается в оптимизации над некоторым классом параметрических вычислений для минимизации энергии волновой функции (**VQE**/**QAOA**, экстракции нелокальной информации (**QNN Classifiers**) или генерации квантового распределения данных (**Generative Models**).


## Hybrid Quantum-Classical Networks
В идеале этот подход подразумевал бы, что при помощи классического оптимизатора мы обучаем некоторую параметрическую схему на квантовом вычислителе, однако в текущих реалиях _NISQ_ этот подход является невозможным, поэтому большая часть параметрической схемы остаётся на классических вычислителях. В данном блоке мы поговорим о подходе, связанном с **QNN Classifiers**, которые следуют вышеупомянутому принципу и обучаются градиентным спуском практически так же, как и обычные классические сети, позволяя градиенту протекать между квантовой и классической частью сети.


```{figure} /_static/qnnblock/qnntfq.png
:name: qnn
:height: 400px

Схема обучения гибридной нейронной сети
```

На изображении гибридной сети процедура практически идентична классическому обучению сетей, в котором добавляется процесс кодирования классических данных в квантовые оператор, и процесс измерения квантового состояния для того, чтобы передать уже классическую информацию для дальнейших вычислений на классическом устройстве, как это было описано в лекции по **VQC**.

## Ansatz

Зачастую в литературе по **VQC**, особенно когда речь идёт о нейронных сетях, упоминается такая вещь как __ansatz__ - по своей сути это заранее подготовленные участки параметрической схемы, которые могут быть использованы как составные блоки сети. Если проводить параллели с классическим машинным обучением, то в рамках библиотеки PennyLane эти схемы называются __templates__ и могут представлять из себя, например, свёрточный слой или эмбеддинг, но и более общие элементы квантовой схемы вроде подготовки состояний или перестановок между кубитами.


```{figure} /_static/qnnblock/cnnansatz.png
:name: ansatz
:height: 400px

Ansatz, соответствующий свёрточному слою нейронной сети в PennyLane
```

## Loss

Функция потерь работает таким же образом, как и в полностью классических сетях, так как оптимизация происходит на классическом железе - единственное, что отличается, это объединение квантовых и классических градиентов. Градиент по нашей квантовой схеме получается при помощи замера состояния, которое может варьироваться из-за вероятностой природы кубита, поэтому несколько замеров позволяют аппроксимировать ожидаемый градиент при помощи методов вроде finite differences или parameter shift, после чего остаётся только совместить его с классическим.

```{figure} /_static/qnnblock/qnngrads.png
:name: grads
:height: 400px

Распространение градиентов от функции потерь в гибридной схеме.
```

## Network Itself

В конечном итоге мы имеем следующую последовательность действий для того, чтобы собрать гибридную нейронную сеть:

- Трансформировать данные из классических в квантовые операторы;
- Отправить эти данные для вычисления на квантовой схеме;
- Просэмплировать и замерить результат квантовой схемы;
- Отправить результаты для вычисления на классической схеме;
- Оценить ошибку, рассчитать градиенты и обновить параметры.

Именно эти 5 шагов мы увидим в следующем примере обучения гибридной нейронной сети.

## Worked Example



## Что мы узнали из лекции

- В ближайшие годы полностью квантовые нейронные сети не смогут решать задачи целиком, поэтому будут использоваться в качестве составляющей гибридного квантово-классического решения.
- Обучение подобных сетей практически идентично обучению классических сетей за исключением нескольких трюков, необходимых для работы с параметрами квантовых схем.