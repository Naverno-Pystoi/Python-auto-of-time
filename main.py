from datetime import datetime, timedelta, timezone
import os
import time


if os.name == 'nt':
    print('Система Windows')
print('ID Программы:', os.getpid())

q = input('\nВыберете функцию :\n 1 - АвтоВремя\n')

def NowTime():
    while True:
        delta = timedelta(hours=0, minutes=0)
        t = datetime.now(timezone.utc).astimezone() + delta

        nowtime = t.strftime("%H:%M:%S")
        nowdate = t.strftime("%d.%m.%Y")
        print('Время на данный момент:', nowtime, '|', nowdate)
        time.sleep(1)
        clear_console()
        
def clear_console():
    os.system('cls')

if q == '1':
    clear_console()
    NowTime()
    print("'Напишите 'выйти' шо бы завершить цикл'")
