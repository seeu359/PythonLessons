1. Что такое функции высшего порядка?
2. Что такое lambda функции? В чем отличие от обычных функций?



### Встроенные функции map, filter, reduce

Встроенные функции высшего порядка map, filter и reduce являются важными инструментами в Python для обработки коллекций 
данных. Они позволяют применять функции к элементам коллекции и получать новые значения. До введения списковых включений,
эти функции являлись ультимативным инструментом, но после все же потеряли свою прежнюю актуальность.


### filter

Первая из функций высшего порядка - `filter`

    filter(function or None, iterable) -> filter object

Возвращаемое значение filter object — это не список, но итератор. То есть это встроенный filter — ленивый. 
Он возвращает элементы по одному, если находит подходящие.

Пример работы функции filter:

**Пример 1.**

Здесь функция `is_even` проверяет, является ли число четным, и возвращает `True` или `False` в зависимости от этого. 
Функция `filter` возвращает итератор, возвращающий только те элементы коллекции numbers, для которых предикат `is_even` 
возвращает `True`.

Функция, которая передается в качестве первого аргумента в `filter`, должна принимать один аргумент и возвращать 
значение `True` или `False`. При использовании `filter` нужно убедиться, что предикат корректно определен и возвращает 
ожидаемый результат для каждого элемента коллекции.

Также стоит помнить, что `filter` возвращает ленивый итератор. И чтобы получить все элементы, необходимо явно 
преобразовать его в список или другой тип коллекции.

### map


Теперь взглянем на функцию map:

    map(func, *iterables) --> map object

**Пример 2.**

Здесь map object — тоже итератор. А аргумент *iterables принимает несколько итерируемых объектов вместо одного.

Если map передать более одного источника элементов, то функция func будет вызвана сначала для всех первых элементов, а потом для остальных. 
И так будет продолжаться, пока не закончатся элементы хотя бы в одном источнике.

Вот пример применения функции map к паре источников:

**Пример 3.**


### functools.reduce 

`reduce` - еще одна классическая функция высшего порядка, но в Python она используется совсем редко. Не зря перед использованием
ее нужно импортировать из модуля functools. Классический способ применения этой функции - аккумуляция значений в одно, например при сложении всех чисел из списка,
но для этого в Python есть прекрасная функция `sum`, которая работает быстрее, а также ее использование более явное и понятное.

Рассматривать мы ее не будем.
