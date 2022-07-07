import vk_api
import datetime
import pymysql
import mysql_connect
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
vk_session = vk_api.VkApi(token='INSERT YOUR VK GROUP TOKEN HERE')
if int(datetime.datetime.now().month) < 9 and int(datetime.datetime.now().month) > 1:
    current_week = int(str(datetime.date.today()-datetime.date(int(datetime.datetime.now().year),2,1)+datetime.timedelta(days=int(datetime.date(int(datetime.datetime.now().year),2,1).isoweekday()-1))).split()[0])//7+1
elif int(datetime.datetime.now().month) == 1:
    current_week = int(str(datetime.date.today()-datetime.date(int(datetime.datetime.now().year)-1,9,1)+datetime.timedelta(days=int(datetime.date(int(datetime.datetime.now().year)-1,9,1).isoweekday()-1))).split()[0])//7+1
else:
    current_week = int(str(datetime.date.today()-datetime.date(int(datetime.datetime.now().year),9,1)+datetime.timedelta(days=int(datetime.date(int(datetime.datetime.now().year),9,1).isoweekday()-1))).split()[0])//7+1
para = [[[""]*5 for i in range(5)] for j in range(2)]
def load_para():
    con = pymysql.connect(host=mysql_connect.host,user=mysql_connect.user,password=mysql_connect.password,database=mysql_connect.database)
    cursor = con.cursor()
    cursor.execute("SELECT * FROM `para` WHERE 1 ORDER BY `id`")
    rows = cursor.fetchall()
    for row in rows:
        tip = ""
        if row[3] == "lek" and row[2] != "-":
            tip = "лек."
        if row[3] == "pr" and row[2] != "-":
            tip = "пр."
        if row[3] == "lab" and row[2] != "-":
            tip = "лаб."
        para[row[5]][int(row[4])-1][int(row[1])-1] = str(row[2])+" "+tip
        if row[6] != "0" and row[2] != "-":
            para[row[5]][int(row[4])-1][int(row[1])-1] += "\nАуд. "+row[6]
load_para()
week = ["Нижняя неделя", "Верхняя неделя"]
day = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
times = ["(9:30-11:05)", "(11:20-12:55)", "(13:10-14:45)", "(15:25-17:00)", "(17:15-18:50)"]
longpoll = VkBotLongPoll(vk_session, 211716327)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:	
        if 'пары сегодня' in str(event).lower() or 'расписание на сегодня' in str(event).lower():
            if int(datetime.datetime.today().isoweekday()) > 5:
                vk.messages.send(chat_id=event.chat_id,message='Выходной',random_id=get_random_id())
            else:
                if current_week%2==0:
                    mes = "Нижняя неделя (чётная) - №"+str(current_week)
                else:
                    mes = "Верхняя неделя (нечётная) - №"+str(current_week)
                mes += "\n" + str(day[int(datetime.datetime.today().isoweekday())-1]) + "\nРасписание на сегодня:"
                for i in range(5):
                    mes += "\n" + str(i+1) + " пара " + times[i] + ":\n" + para[current_week%2][int(datetime.datetime.today().isoweekday())-1][i]
                vk.messages.send(chat_id=event.chat_id,message=mes,random_id=get_random_id())
        if 'пары завтра' in str(event).lower() or 'расписание на завтра' in str(event).lower():
            if int((datetime.datetime.today().isoweekday()+1)%8) > 5:
                vk.messages.send(chat_id=event.chat_id,message='Выходной',random_id=get_random_id())
            else:
                if int(datetime.datetime.today().isoweekday()) != 7:
                    if current_week%2==0:
                        mes = "Нижняя неделя (чётная) - №"+str(current_week)
                    else:
                        mes = "Верхняя неделя (нечётная) - №"+str(current_week)
                else:
                    if (current_week+1)%2==0:
                        mes = "Нижняя неделя (чётная) - №"+str(current_week+1)
                    else:
                        mes = "Верхняя неделя (нечётная) - №"+str(current_week+1)
                mes += "\n" + str(day[int((datetime.datetime.today().isoweekday())%7)])
                mes += "\nРасписание на завтра:"
                for i in range(5):
                    if int(datetime.datetime.today().isoweekday()) != 7:
                        mes += "\n" + str(i+1) + " пара " + times[i] + ":\n" + para[current_week%2][int(datetime.datetime.today().isoweekday()%7)][i]
                    else:
                        mes += "\n" + str(i+1) + " пара " + times[i] + ":\n" + para[(current_week+1)%2][int(datetime.datetime.today().isoweekday()%7)][i]
                vk.messages.send(chat_id=event.chat_id,message=mes,random_id=get_random_id())
        if 'пары все' in str(event).lower() or 'расписание полное' in str(event).lower():
            mes = "Полное расписание:"
            for i in range(1,-1,-1):
                mes += "\n" + week[i]
                for j in range(5):
                    mes += "\n" + day[j]
                    for k in range(5):
                        mes += "\n" + str(k+1) + " пара " + times[k] + ":\n" + para[i][j][k]
            vk.messages.send(chat_id=event.chat_id,message=mes,random_id=get_random_id())
        if 'неделя' in str(event).lower():
            if current_week%2==0:
                vk.messages.send(chat_id=event.chat_id,message='Нижняя неделя (чётная) - №'+str(current_week),random_id=get_random_id())
            else:
                vk.messages.send(chat_id=event.chat_id,message='Верхняя неделя (нечётная) - №'+str(current_week),random_id=get_random_id())
        if 'обновить базу' in str(event).lower():
            load_para()
            vk.messages.send(chat_id=event.chat_id,message='Локальная база данных бота успешно обновлена',random_id=get_random_id())
