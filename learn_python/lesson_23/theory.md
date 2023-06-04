### Функции-генераторы 

Представь себе ситуацию - тебе нужно написать скрипт, который переносит данные таблиц одной базы данных в другую.

Скорее всего, в твоем коде будет 2 основные абстракции - одна выгружает данные из одной базы данных, а другая функция загружает эти данные в другую 
базу данных.

Все бы ничего, но представь, что ты выгружаешь данные об недействительных паспортах, а их там около 150 млн. 
Загрузив их все одной пачкой, твой скрипт во время выполнения скорее всего просто повиснет, так как данных слишком много и ты рискуешь забить всю
оперативную память, а возможно и память на жестком диске.

Было бо неплохо выгружать данные небольшим пачками. Как это сделать? Для этого в Python'е и существуют функции-генераторы.


### Ключевое слово yield

Представим, что нам нужно построить последовательность чисел, элементы которой возрастают экспоненциально. 
Если бы такие числа нужно было лишь распечатать, то код бы мог выглядеть так:

    def iterate(x0, m):
        x = x0
        while True:
            print(x)
            x *= m
    
    iterate(1, 1.1)
    
    print("impossible!")


Как только мы вызовем процедуру `iterate`, то все возрастающие числа будут выводиться бесконечно, ведь никакого 
завершения цикла мы не предусмотрели. Выполнение процедуры `iterate` никогда не завершится, поэтому и весь код 
после вызова не выполнится никогда.

А теперь представим, что нам нужна последовательность за пределами процедуры `iterate`. В этом случае мы не сможем 
сделать return вместо `print()` — это приведет к остановке процесса генерации.

В виде аргумента мы могли бы передать список, в который процедура бы добавляла элементы вместо вывода на печать. 
Однако использовать список мы не сможем, ведь процедура никогда не завершится.

Далеко не всегда можно заранее узнать, сколько итераций нужно выполнить. Чтобы справиться с описанными выше 
проблемами, понадобится новое ключевое слово `yield`:


**Пример 1**


В коде выше ключевое слово `yield` очень похоже на `return`. Оно точно так же возвращает один элемент, а не 
генераторное выражение. Еще одно сходство заключается в том, что управление переходит обратно к коду, который 
запросил элемент у итератора.

Обычно `return` останавливает выполнение тела функции раз и навсегда. В отличие от него, `yield` выполнение приостанавливает. 
Выполнение возобновляется, когда вызывающая сторона попросит новый элемент посредством `next()`. Оно продолжается, 
пока не произойдет одно из этих событий:
 
1. Встретится новый `yield`
2. Встретится `return`
3. Выполнится последняя строчка тела функции


*Пример 2*