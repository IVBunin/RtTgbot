'''
одна единственная функция лол

'''
from os import mkdir
from os import path
from openpyexcel import load_workbook

def serch_in_db( address: str, option : int):
    try:
        if not(path.isdir("/data/")):
            mkdir("/data/")
        wbask = load_workbook(filename="C:\\Users\\Александр\\Documents\\GitHub\\RtTgbot\\data\\Заявки.xlsx")
        wbask = wbask["Лист1"]
        wbsell = load_workbook(filename= "C:\\Users\\Александр\\Documents\\GitHub\\RtTgbot\\data\\Продажи.xlsx")
        wbsell = wbsell['Лист1']
        answer = []
        print(wbsell.max_row)
        match (option):
            case (0):
                # тут мы ищем в базе адрес и возвращаем тариф
                for i in range(1, wbsell.max_row +1):
                    if address == wbsell["E" + str(i)].value:
                        answer.append(wbsell["F" + str(i)].value)
                    elif i == wbsell.max_row:   
                        return  answer # колонка с тарифом
            case (1):
                # тут мы выводим список тарифов
                return 'Void'
        # end match   
    except Exception as e:
       print(e) 

a = serch_in_db('Черниговка с.,Боровикова,241,68', 0)
print(str(a))