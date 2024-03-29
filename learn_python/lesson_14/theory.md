Повторение:

1. Что такое словари? Как всегда, дай краткую характеристику.
2. Defaultdict - что это? Чем отличается от обычного словаря?
3. Как добавить значение в словарь по ключу?
4. Как проверить наличие ключа в словаре?
5. Как безопасно извлечь ключ из словаря?
6. С помощью какой функции можно проверить, относится ли объект к определенному типу данных?


### Множества

Ключи словаря хранятся в нем в единственном экземпляре.  Добавление нового значения по существующему ключу 
заменяет старое значение. Хранение в единственном экземпляре полезно и в тех случаях, когда нам нужно хранить не столько значения по ключам, 
сколько именно сами ключи.

Например, нужно хранить список городов, которые посетил каждый пользователь. При повторном 
посещении города дублировать запись не требуется. Это позволяет сэкономить память и упростить поиск информации. 
Также нам может понадобиться узнать, какие города посетили и Вася и Маша, а какие — только Маша или только Вася.

По сути, это хранения перечня элементов в неких наборах и сопоставления этих наборов между собой. В математике для решения такого рода задач служат множества. 
В свою очередь, Python предоставляет одноименную структуру данных — set.

Итак, множества в Python — это неупорядоченные последовательности ключей, каждый из которых в множестве представлен ровно один раз. То есть элементы в множестве уникальны.
Можно найти некоторое сходство со словарями:
1. Как и словари, множества последовательность неупорядоченная. 
2. Как и у словаря, у множества нельзя получить ключ по индексу - это противоречит и семантике словарей, и, 
самое главное, той структуре данных, на которой основаны словари и множества(хеш-таблица).

### Создание множеств

Множество можно создать с помощью соответствующего литерала:

    s = {1, 2, 3, 2, 1}
    s  # {1, 2, 3}
    type(s


Литералы множества записываются в фигурных скобках, как и литералы словаря - еще одно сходство. Только в отличие от словаря, множества имеют только одиночные элементы без пар, как в списках.
**Примеры**

### Проверка вхождения элемента в множество

При необходимости проверить, присутствует ли ключ в множестве, можно использовать уже известный нам оператор `in`.

Проверка вхождение в множество с помощью `in` выполняется очень быстро. Так же быстро, как и в словаре. Это опять же связано с той структурой данных,
на которой основаны множества и словари.

**Пример**

`Практика 1.`

### Изменение множеств

Множества в Python, как и словари, изменяемые. Добавлять и удалять элементы из множества можно с помощью методов `add`, `discard` и `remove`:

**Примеры**

### Копирование и очистка множеств

Множества изменяемы, поэтому требуется сделать копию перед изменением оригинала. Как и словари, множества не поддерживают операцию получения среза. 
Для копирования приходится использовать метод `copy`, создающий поверхностную копию множества:

**Примеры**

Очистить множество можно с помощью метода `clear`

**Практика 2**
