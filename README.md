# Smart city

## backend

### Установка и запуск

>  **Необходим Python версии 3.0 и выше**

Настройка директории и установка зависимостей (windows)

```console  
$ python -m venv env

$ env/scripts/activate

$ New-Item -ItemType directory -Path './generated_qr'

$ New-Item -ItemType file -Path './modules/config.py'

$ pip install requirements.txt
```

Содержимое config.py
```python
email_val = 'email'
password = 'password'
host_val = 'localhost'
db_login = 'database_login'
db_pass = 'database_password'
db_host = 'database_host'
db_name = 'database_name'

```

Запуск 
```console  
$ python app.py   
```