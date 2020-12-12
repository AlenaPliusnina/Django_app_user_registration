# Django_app_user_registration / Django приложение для регистрации пользователей

Разворачиваем проект локально:

1. Скачайте репозиторий

2. Создайт виртуальное окружение:

        python -m venv env
       
3. Активируйте виртуальное окружение: 

        source env/bin/activate
        
4. Чтобы установить все требуемые библиотеки python в новом окружении выполните команду: 

        pip install -r requirements.txt
   
   Если у вас macOS до выполнения команды pip install -r requirements.txt выполните команду:       
   
           env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install psycopg2==2.8.4      
   
   Для предотвращения появления ошибки (error: command 'gcc' failed with exit status 1.) при установке зависимостей.

5. Для работы проекта создайте файл переменных окружения (.env) и добавьте в него значение SECRET_KEY, используемое в файле settings.py
       
6. Чтбы запустить сервер введите команду: 

       python manage.py runserver

7. Для входа в администравтивную панель проекта создайте суперпользователя при помощи команды: 

       python manage.py createsuperuser
