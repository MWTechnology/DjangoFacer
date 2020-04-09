СЕЙЧАС РУКОВОДСТВУЮСЬ ДАННОЙ ДОКУМЕНТАЦИЕЙ
https://django.fun/tutorials/autentifikaciya-v-django-polnyj-primer-vhoda-vyhoda-i-smeny-parolya/

#pip install Django
#pip install mysqlclient
#django-admin startproject project_DjangoFace

###################################################################################################
#установщик Mysql https://yadi.sk/d/CazfUwT0RIrnkw # просто установи и запомни пароль!            #
#потом перейди в MySQL 8.0 Command Line Client                                                    #
#введи пароль                                                                                     #
#и вот эту строчку                                                                                #
#CREATE DATABASE Mysqldb; #  Mysqldb название БД                                                  #
#SHOW DATABASES; # Это вводить не надо                                                            #
#                                                                                                 #
#для просмотра БД можешь использовать Valentina Studio вот ссылка https://yadi.sk/d/OOlvg8sa6Mas6g#
###################################################################################################

меняем инфу в settings БД

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysqldb',
        'USER': 'root',
        'PASSWORD': '12345678',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

pip install django-crispy-forms

#Затем откройте файл settings.py и добавьте приложение в установленные приложения:

INSTALLED_APPS = [
    # [...]
    'crispy_forms'
]

#Затем добавьте следующий параметр, который устанавливает Bootstrap 4 в качестве структуры стилей по умолчанию для django-crispy-forms:

CRISPY_TEMPLATE_PACK = 'bootstrap4'

Создадим приложение
python manage.py startapp accounts

Предыдущая команда создаст приложение Django с файловой структурой по умолчанию. Чтобы сделать это приложение частью вашего проекта, вам нужно открыть файл settings.py и добавить его в INSTALLED_APPS:

INSTALLED_APPS = [
# [...]
'accounts'
]



#Добавляем регистрацию https://django-registration.readthedocs.io/en/3.1/install.html

pip install django-registration  - делал регистрацию 


машинное обучение хенрик бринк

https://github.com/pinax/django-user-accounts    --   Это через что я делал сброс пароля 
https://github.com/pinax/pinax-templates/blob/master/pinax/templates/templates/account/password_reset_sent.html  - где брал шаблоны



###########################################################################################################
#################################Начинаю делать основную страницу##########################################
###########################################################################################################


pip install pillow==7.1.0 __ устанавливаем для работы с изображением