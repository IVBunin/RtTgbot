from openpyexcel import load_workbook
from registration import *
import config as cfg
import random



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
        wbask = load_workbook(filename= cfg._LOCAL_PATH_ + "/sheets/Заявки.xlsx")
        wbask = wbask['Лист1']
        answer = set()
        for i in range(1, wbsell.max_row+1):
            if wbsell["R" + str(i)].value != None:
                answer.add(wbsell["R" + str(i)].value)  
        for i in range(1, wbask.max_row+1): 
            if wbask["A" + str(i)].value != None:
                answer.add(wbask["A" + str(i)].value)             
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

def done_requests(agent_name : str): #Выполненные задачи на одного человека
    try:
        wb = load_workbook(filename=cfg._LOCAL_PATH_ + "/sheets/Заявки.xlsx")
        ws = wb["Лист1"]

        construction_total = 0
        service_connected_total = 0
        kn_total = 0
        deferred_total = 0
        refusal_total = 0
        total_requests_total = 0

        for row in ws.iter_rows(min_row=2):
            agent = row[0].value

            if agent.lower() == agent_name.lower():
                construction_total += row[12].value
                service_connected_total += row[13].value
                kn_total += row[14].value
                deferred_total += row[15].value
                refusal_total += row[16].value
                total_requests_total += row[17].value
        answer = f"Агент: {agent_name}, Стройка: {construction_total}, Услуга подключена: {service_connected_total}, КН: {kn_total}, Отложенная: {deferred_total}, Отказ: {refusal_total}, Всего: {total_requests_total}"
        return answer

    except Exception as e:
        print(e)
        return e
def peopleforalldone_requests(agent_name : str): # Вспомогательная функция для добавления сотрудников в инфографику
    try:
        wb = load_workbook(filename=cfg._LOCAL_PATH_ + "/sheets/Заявки.xlsx")
        ws = wb["Лист1"]
        total_requests_total = 0
        answer= [1,1] #инициализировал список
        for row in ws.iter_rows(min_row=2):
            agent = row[0].value
            if agent.lower() == agent_name.lower():
                total_requests_total += row[17].value
                answer[0] = f"{agent_name} - {total_requests_total}"
                answer[1] = total_requests_total
        return answer

    except Exception as e:
        print(e)
        return e

def alldone_requests(department:str): # Вывод инфографики по отделу
    try:
        wb = load_workbook(filename=cfg._LOCAL_PATH_ + "/sheets/Заявки.xlsx")
        ws = wb["Лист1"]
        answ_list = []
        total_amount = 0
        for row in ws.iter_rows(min_row=2):
            dep = row[1].value
            if dep.lower() == department.lower():
                got = peopleforalldone_requests(row[0].value)
                if got[0] not in answ_list:
                    answ_list.append(got[0])
                    answ_list.append("\n")
                    total_amount +=got[1]
        answ_list.append("Всего выполнено задач - " + str(total_amount))
        return answ_list

    except Exception as e:
        print(e)
        return e

def writetxt(path:str): #Текст в сообщение
    texttosend = []
    with open(path,'r', encoding='UTF-8') as file:
        for line in file:
            texttosend.append(line)
    return texttosend

def newstxt(): #новость в сообщение
    texttosend = []
    with open(cfg._LOCAL_NEWS_PATH_ +"новость " + str(random.randint(1,2)) + ".txt",'r', encoding='UTF-8') as file:
        for line in file:
            texttosend.append(line)
    return texttosend
