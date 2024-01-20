'''
одна единственная функция лол

'''

def serch_in_db( address: str, option : int):
    try:
        match (option):
            case (0):
                # тут мы ищем в базе адрес и возвращаем тариф
                return option_list
            case (1):
                # тут мы выводим список тарифов
                return option_list_common
        # end match   
    except:
        return 1