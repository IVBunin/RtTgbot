from shutil import rmtree
from os import mkdir
from os import path
from os import remove
from config import master_password
import config
import json
from time import sleep


# создание файла базы
def base_init(base_name :str):
    try:
        if not(path.isdir("data/base/")):
            mkdir("data/base/")
        data = {"items": {}}
        base = open(f"data/base/{base_name}.json", "w")
        json.dump(data, base)
        base.close
        return 0
    except Exception as e:
        return e


#удаление файла базы 
def clear_base(password :str , base_name :str, clear_all = False):
    try:
        if password == config.master_password:
            match(clear_all):
                case(False):
                    remove(f"data/base/{base_name + ".json"}")
                    return 0
                case (True):
                    rmtree(f"data/base/")
                    return 1 
    except Exception as e:
        return e


# получение из базы имени или чат id  
# нужно указать что хотим получить и по чему будем искать

#регистрация пользователя
def register_user( base_name :str, user_name :str, chat_id:str):
    try:
        base = open(f"data/base/{base_name}.json", "r")
        data = json.load(base)
        base.close
        base = open(f"data/base/{base_name}.json", "w")
        data["items"][user_name] = chat_id
        json.dump(data, base)
        base.close
        return 0
    except Exception as e :
        return e


def test(clear):
    print(base_init("new"))
    print(register_user("new","first", "123456"))
    print(register_user("new","second", "123456"))
    print(register_user("new","third", "123456"))
    print(register_user("new","forth", "123456"))
    sleep(10)  # import time
    if clear == True:
        print(clear_base("qwerty123", "new"))

test(False)