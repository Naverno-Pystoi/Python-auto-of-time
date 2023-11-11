from datetime import datetime, timedelta, timezone
import os
import time
import platform
import glob

os.system('cls')
if os.name == 'nt':
    print('Система Windows')
print('ID Программы:', os.getpid())

q = input('\nВыберете функцию :\n 1 - АвтоВремя\n 2 - О системе \n 3 - Удаление временных файлов \n ---> ')

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
elif q == '2':
    os.system('cls')
    print('Ращрядность :' , platform.machine())
    print('Версия системы: ', platform.version())
    print('Версия платформы :' , platform.platform())
    print('Краткая сводка :', platform.uname())
    print('Операционная система :' ,platform.system())
    print('Процессор :' ,platform.processor())
    print('Имя компьютера :', platform.node())
    print('ОС системы :', platform.system())
    input()
elif q == '3':
    files = glob.glob("C:/Users/New/AppData/Local/Temp")
    for f in files:
        os.remove(f)