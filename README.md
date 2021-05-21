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
```

Запуск 
```console  
$ python app.py   
```