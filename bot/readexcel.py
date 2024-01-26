from os import mkdir
from os import path
from openpyexcel import load_workbook
from numpy import unique
from registration import *
def serch_in_db( address: str, option : int):
    try:
        if not(path.isdir("data/")):
            mkdir("data/")
        wbask = load_workbook(filename="data/sheets/Заявки.xlsx")
        wbask = wbask["Лист1"]
        wbsell = load_workbook(filename= "data/sheets/Продажи.xlsx")
        wbsell = wbsell['Лист1']
        answer =[]
        match (option):
            case (0):
                # тут мы ищем в базе адрес и возвращаем тариф
                for i in range(1, wbsell.max_row+1):
                    if address == wbsell["E" + str(i)].value:
                        if wbsell["F"+str(i)].value != None:
                            answer.append(wbsell["F" + str(i)].value)
                            answer.append("\n")
                    elif i == wbsell.max_row : return answer # колонка с тарифом
            case (1):
                # тут мы выводим список тарифов
                answer = set()
                for i in range(1, wbsell.max_row+1):
                    if wbsell["C" + str(i)].value != None:
                        answer.add(wbsell["C" + str(i)].value)                
                return list(answer)
            case (2):
                # тут мы выводим список тарифов
                answer = set()
                for i in range(1, wbsell.max_row+1):
                    if wbsell["C" + str(i)].value != None:
                        answer.add(wbsell["R" + str(i)].value)                
                return list(answer)
  
        # end match   
    except Exception as e:
        print(e)
        return e
def allinfo(pc : int):
    try:
        if not(path.isdir("data/")):
            mkdir("data/")
        wbask = load_workbook(filename="data/sheets/Заявки.xlsx")
        wbask = wbask["Лист1"]
        wbsell = load_workbook(filename= "data/sheets/Продажи.xlsx")
        wbsell = wbsell['Лист1']
        class info:
            def __init__(self) -> None:
                self.data
                self.month
                self.service
                self.pc
                self.address
                self.tarif
                self.tech
                self.sales_channel
                self.agent
                self.fact
                self.start_obp
                self.end_obp
                self.obp
                self.dealer
                self.operator
                self.company
                self.num
                self.agent1
                self.managerb2c
                self.supervisor
                self.sales_channel1
                self.sc
                self.city
                self.bti
                self.direction
                self.company1
                pass
            def display_info(self):
                print(f"Дата установки :{self.data}	Месяц:{self.month}	Услуга{self.service}	ЛС или SN	Адрес	Наименование	Технология или модель	Канал продаж	Агент	Факт	Дата выставления ОБП	Дата закрытия ОБП	ОБП	Агент/Дилер	Оператор	Компания	Номер заявки на доставку	Агент.1	Менеджер B2C	Cупервайзер БТИ	Канал продаж.1	СЦ	Город	Наставник БТИ	Направление	Компания.1")
            pass
        num = info()
        num.data
    except Exception as e:
        print(e)
        return e
    


