from shutil import rmtree
from os import mkdir
from os import path
from os import remove
from config import master_password
import config
import json



# создание файла базы
def reg_init(base_name :str):
    try:
        if not(path.isdir("bot/data/base/")):
            mkdir("bot/data/base/")
        data = {"items": {}}
        base = open(f"bot/data/base/{base_name}.json", "w")
        json.dump(data, base)
        base.close
        return 0
    except Exception as e:
        return e


#удаление файла базы 
def clear_reg(password :str , base_name :str, clear_all = False):
    try:
        if password == config.master_password:
            match(clear_all):
                case(False):
                    remove(f'bot/data/base/{base_name + ".json"}')
                    return 0
                case (True):
                    rmtree(f"bot/data/base/")
                    return 1 
    except Exception as e:
        return e


#регистрация пользователя
def register_user( base_name :str, user_name :str, chat_id:str):
    try:
        base = open(f"bot/data/base/{base_name}.json", "r")
        data = json.load(base)
        base.close
        base = open(f"bot/data/base/{base_name}.json", "w")
        data["items"][user_name] = chat_id
        json.dump(data, base)
        base.close
        return 0
    except Exception as e :
        return e


# получение из базы имени или чат id  
# нужно указать имя базы тип по которому ищем *имя или чат айди* и сам предмет
def get_from_reg( base_name :str, type_ :str, request :str):
    try:

        base = open(f"bot/data/base/{base_name}.json", "r")
        data = json.load(base)
        
        match (type_):
            case ("name"):
                return data["items"][request]

            case ("chat_id"):
                for key,value in data["items"].items():
                    if request == value:
                        return key

    except Exception as e :
        return e



def get_keys( base_name :str):
    try:
        base = open(f"bot/data/base/{base_name}.json", "r")
        data = json.load(base)
        keys = []
        keys = list(data["items"].keys())
        return  keys
    except Exception as e :
        return e


def debug(base_name):
    base = open(f"bot/data/base/{base_name}.json", "r")
    data = json.load(base)




