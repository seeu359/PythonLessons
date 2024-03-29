### Введение в Django

Django — популярный веб-фреймворк на Python, который предназначен для быстрой разработки сайтов. Он сочетает в себе большие возможности сложных фреймворков и простоту написания кода с минимум конфигурирования.
Существует 2 вида фреймворков:
1. Микро-фреймворки - FastAPI, Flask. Они предлагают только самый необходимый функционал из коробки, такой как: управление маршрутизацией, работа с сессиями, куками и так далее.
2. Фреймворки - в Python это Django. Django предлагает огромный набор функционала из коробки - это и встроенная админка, шаблонизатор, ORM(object relational mapping) и много всего другого. Django является самым популярным
фреймворком для веб-разработки на Python.

C тобой мы будем рассматривать следующие темы:

1. Ресурсная (REST-like) маршрутизация. Создание CRUD, валидация данных
2. Шаблонизатор Django. Макеты
3. Управление приложением из командной строки
4. ORM. Создание сущностей. Связи

Для комфортного взаимодействия и для понимания того, что мы делаем, тебе самостоятельно придется пройти 2 курса:
1. Курс по базам данных. БД - хлеб backend-разработчика, без них не обходится ни одно приложение, которое отдает пользователю хоть какую-то информацию, будь то список друзей на странице в социальной сети, либо товар в интернет-магазине.
Без этого нам просто никуда, по этому ОЧЕНЬ НАДЕЮСЬ на твою самостоятельно, само собой я всегда готов помочь и ответить на твои вопросы. Вот курс: https://itempuniversity.com/course/view.php?id=533
2. Далее идет протокол HTTP - основной протокол, по которому происходит передача всей информации в интернете. Ты должен понимать, как он работает хотя бы на базовом уровне, чтобы понимать, что происходит: https://ru.hexlet.io/courses/http_protocol.
К сожалению, практика доступна только по подписке, но мы обойдемся и без нее. Твоя задача максимально внимательно все прочитать и постараться понять.


### Создание проекта на Django

Чтобы начать разбираться с Django, нужно для начала создать на нем проект и запустить.

Проекты на Django создаются из командной строки. 

    # Перейди в директорию проекта и выполните команду
    django-admin startproject <project name> .


Эта команда создаст Django-проект в нашей директории и установит все зависимости, которые необходимы для работы Django. Некоторые уточнения:

* Точка в команде означает, что генерируемое содержимое проекта будет расположено в текущей директории. У нас уже есть директория проекта, поэтому нам не нужен лишний уровень вложенности

После установки пакета нам станет доступна команда django-admin — команда для работы с Django-проектами

Проверим версию текущей установки Django. Для этого выполним команду в директории проекта:

    # Версия должна быть не ниже 4
    django-admin version

    4.1.2

### Структура проекта

Современные фреймворки используют, чтобы разрабатывать сайты любых размеров. Это хорошо, так как есть много возможностей. Но с другой стороны в этом легко потеряться из-за большого количества функций, особенно если это ваш первый фреймворк.

Помимо большого числа понятий самого Django, внутри него встроена поддержка шаблонизатора, работа со статикой, разные виды кеширования, тестирование, логирование и многое другое.

Это не значит, что придется использовать сразу всё. Но нужно понимать хотя бы основы каждой функции — на уровне понимания структуры проекта.

Ниже приведена таблица файлов с описанием их содержимого. В этом описании будут встречаться названия, с которыми вы, возможно, не знакомы. Позже мы их разберем.


| Файл            | Описание                                                                                           |
|-----------------|----------------------------------------------------------------------------------------------------|
| manage.py       | Скрипт, который используется в процессе разработки для выполнения различных действий над проектом  | 
| wsgi и asgi.py  | Точки входа в WSGI- и ASGI-приложения |
| settings.py | Модуль, который содержи все настройки проекта |
 | urls.py | Модуль, который описывает правила маршрутизации запросов |

### Запуск проекта 
Django управляется утилитой скриптом manage.py, который находится в корне проекта. Он включает в себя десятки команд, которые упрощают процесс разработки. Одна из них — запуск сайта в режиме разработки:

    python manage.py runserver
    
    Watching for file changes with StatReloader
    Performing system checks...
    
    System check identified no issues (0 silenced).

    You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.
    October 25, 2022 - 23:17:39
    Django version 4.1.2, using settings 'hexlet_django_blog.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.


Эта команда запускает встроенный в Django веб-сервер, который работает в однопоточном режиме и сам перезапускается, если что-то менять в коде. Кроме того, этот сервер никогда и ничего не кэширует — это важно при редактировании шаблонов и статических файлов (JS, CSS).

Чтобы увидеть сайт, открой браузер и загрузи http://127.0.0.1:8000. Ты увидишь приветственную страницу фреймворка.

Чтобы остановить сервер, переключись на терминал, в котором он запущен, и наберите `CTRL+C`. Эта страница нужна только для проверки того, что все работает.



### Запрос-ответ

Как и любой серверный веб-фреймворк, Django построен вокруг HTTP. Он принимает запросы, на основе которых формирует и отдает HTTP-ответы. Django берет на себя всю грязную работу: разбор запроса, выбор правильного обработчика, отправку ответа клиенту. Программисту остается выполнить только самый необходимый минимум для добавления новых страниц на сайте.

### Первая страница на Django

В этот минимум входят три вещи:

1. Маршрут. Определяет адрес конкретной страницы или набора страниц на сайте. Маршрут связывает эти адреса с конкретным обработчиком, который будет вызван при запросе этих страниц
2. Контроллер. Слой кода, в котором расположены обработчики страниц сайта. Они анализируют запрос и формируют ответ, который фреймворк отправляет пользователю
3. Шаблон. Специальный файл, который используется, чтобы формировать HTTP-ответ


### Маршрут
Маршруты любого проекта на Django хранятся в файле urls.py. В нашем случае он находится по пути <project_name>/urls.py. Этот файл предназначен для описания маршрутов нашего сайта.

В этом файле находится переменная urlpatterns — список маршрутов нашего сайта. Изначально этот файл содержит только один маршрут, который соответствует разделу администратора admin/:

Функция `path(route, view)` задает правило для обработки маршрута. Первым параметром она принимает адрес запрашиваемой страницы или паттерн, который описывает группу страниц. В коде выше это адрес раздела администратора.

Вторым параметром передается обработчик или встраиваемый `urls.py` другого приложения. Обработчики запросов в Django называют view — на жаргоне джангистов «вьюха».

Заменим стартовую страницу на собственную. Нам понадобится view и шаблон — template.

Для этого в файл urls.py добавим импорт вьюхи:

    from <project_name> import views

Далее добавим в список urlpatterns новое правило обработки адреса главной страницы:

    urlpatterns = [
        path('', views.index), # <- добавляем эту строчку
        path('admin/', admin.site.urls),
    ]

Мы добавили правило, которое назначает обработчиком главной страницы или пустого пути вьюху views.index.

### Контроллер
Теперь создадим файл `<project_name/views.py` и запишем в него следующий код:

    from django.shortcuts import render

    def index(request):
        return render(request, 'index.html', context={
        'who': 'World',
    })

Здесь мы используем функцию render. Она формирует HTML на основе указанного шаблона и использует при рендеринге (составлении страницы) данные из словаря context.

### Шаблон

Теперь нам потребуется шаблон. Создадим директорию `<project_name>/templates` и файл `index.html` в ней. В файл запишем следующее:

    <h1>Hello, {{ who }}!</h1>


Остается сделать небольшую настройку Django. Сначала нужно указать Django название директории, в котором будут 
находиться шаблоны. Для этого в модуле `<project_name>/settings.py>` находим список `TEMPLATES`. Там в списке `DIRS` задаем значение `BASE_DIR / 'templates'`:

Теперь нам нужно в конец списка `INSTALLED_APPS` добавить строку `<project_name>`. Так Django будет знать, что шаблоны и код у нас находятся в данном пакете:

    INSTALLED_APPS = [
        ...
        '<project_name>', # <- добавляем эту строчку
    ]


Теперь создадим новую страницу `/about`. Для этого добавим маршрут, вью и шаблон

Код шаблона:

    <h1>О блоге</h1>
    <p>Эксперименты с Django на Хекслете</p>