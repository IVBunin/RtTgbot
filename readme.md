# Чат бот для ПАО "Ростелеком"


## Структура директории
>bot
data  
+--+sheets  
+---+Директория для таблица баз данны
+--+base  
+---+Директория для json файла регистрации  
+--+logs  
+---+Директория для логов работы  
+-+[config.py](###configpy)  
+-+[GPT.py](#GPTpy)     
+-+[main.py](#mainpy)   
+-+[readexcel.py](#readexcelpy)  
+-+[registration.py](#registrationpy)    
 

## Список используемых библиотек  
| Название бибиотеки | Версия |
| ----------- | ----------- |
| certifi          |  2023.11.17|
|charset-normalizer |3.3.2|
|et-xmlfile         |1.1.0|
|idna               |3.6|
|jdcal             | 1.4.1|
|numpy              |1.26.3|
|openpyexcel        |2.5.14|
|pip                |23.2.1|
|pyTelegramBotAPI  | 4.15.3|
|requests           |2.31.0|
|setuptools         |65.5.0|
|telebot           |0.0.5|
|urllib3           | 2.1.0 |



## Модули
### <a id="configpy">Config.py</a>  
Конфигурационный файл в котором храняться глобальные неизменяемые константы
> token - токен телеграм бота  
> master_password - пароль используемый для отладочных действий  
> _LOCAL_PATH_ - путь для коректного чтения и сохранения файлов 
### <a id="GPTpy">GPT.py</a>  
Модуль для интеграции ChatGPT3.5 
>
### <a id="readexcelpy">Readexcell.py</a>  
Модуль для чтения базы данных из таблиц  
> 
### <a id="registrationpy">Registration.py</a>
Модуль для регистрации пользователей и записи их в JSON файл 

#### reg_init(base_name :str)  
Создаеь json файл с указалным названием.  
Принимает на вход строку 

#### clear_reg(password :str , base_name :str, clear_all = False) 
Функция для удаления базы регистрации.
Принимает на вход  
- пароль
- название базы
- параметр clear_all (по умолчанию False)  
При указании параметра clear_all = True очищается вся директория base

#### register_user( base_name :str, user_name :str, chat_id:str)  
Функция для удаления базы регистрации.
Принимает на вход  
- название базы
- имя пользователя
- chat id пользователя

Добавляет нового пользователя в базу 

#### get_from_reg( base_name :str, type_ :str, request :str):  
Функция для получения информации из json файла  
Принимает на вход    
- название базы
- параметр поиска
- запрос
>параметр поиска - то что мы хотим найти  
запрос - то по чему мы будем искать 


#### get_keys( base_name :str):  
Функция для получения всех имен из базы  
Принимает на вход    
- название базы
 

### <a id="mainpy">main.py</a>  
