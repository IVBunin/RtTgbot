from openpyexcel import load_workbook
from registration import *
import config as cfg

def serch_in_db( address: str): # функция тарифов по адресу
    try:
        wbsell = load_workbook(filename= cfg._LOCAL_PATH_ + "/sheets/Продажи.xlsx")
        wbsell = wbsell['Лист1']
        answer =[]
        for i in range(1, wbsell.max_row+1): # тут мы ищем в базе адрес и возвращаем тариф
            if address == wbsell["E" + str(i)].value:
                if wbsell["F"+str(i)].value != None:
                    answer.append(wbsell["F" + str(i)].value)
                    answer.append("\n")
            elif i == wbsell.max_row : return answer
    except Exception as e:
        print(e)
        return e
    
def all_options():
    try:
        wbsell = load_workbook(filename= cfg._LOCAL_PATH_ + "/sheets/Продажи.xlsx")
        wbsell = wbsell['Лист1']
        answer = set()
        for i in range(1, wbsell.max_row+1):
            if wbsell["C" + str(i)].value != None:
                answer.add(wbsell["C" + str(i)].value)                
        return list(answer)  
    except Exception as e:
        print(e)
        return e
    
def find_all_people(): # Запись всех людей в список
    try:
        wbsell = load_workbook(filename= cfg._LOCAL_PATH_ + "/sheets/Продажи.xlsx")
        wbsell = wbsell['Лист1']
        answer = set()
        for i in range(1, wbsell.max_row+1):
            if wbsell["C" + str(i)].value != None:
                answer.add(wbsell["R" + str(i)].value)                
        return list(answer)
    except Exception as e:
        print(e)
        return e

def ask_answer(fio : str): #Вывод информации по заявке
    try:
        wbask = load_workbook(filename=cfg._LOCAL_PATH_ + "/sheets/Заявки.xlsx")
        wbask = wbask["Лист1"]
        answer = []
        for i in range(1, wbask.max_row+10):
                if fio == wbask["A" + str(i)].value:
                    answer.append(wbask["E" + str(i)].value + "\n")
                    answer.append("Статус - " + str(wbask["I" + str(i)].value) + "\n")
                    answer.append("Услуги в заявке - " + str(wbask["F" + str(i)].value) + "\n")
                    answer.append("Дата - " + str(wbask["J" + str(i)].value)[:10] + "\n")
                    answer.append("\n")
                elif i == wbask.max_row : return answer 
        
    except Exception as e:
            print(e)
            return e

def allinfo(pc : int): #Ужас нерабочий
    try:
        wbask = load_workbook(filename= cfg._LOCAL_PATH_ + "/sheets/Заявки.xlsx")
        wbask = wbask["Лист1"]
        wbsell = load_workbook(filename= cfg._LOCAL_PATH_ + "/sheets/Продажи.xlsx")
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
    