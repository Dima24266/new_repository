# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""
from tabulate import tabulate

a = ['8.8.8.8', '1.1.1.3', '192.168.1.1', '192.168.1.100']
b = []
c = []
d = {'Reachable': '', 'Unrechable': ''}
def print_ip_table(ip):
    for i in ip:
        import subprocess
        a = subprocess.run(['ping', '-c', '3', i], stdout=subprocess.DEVNULL)
        if a.returncode == 0:
            b.append(i)
        else:
            c.append(i)
    d['Reachable'] = b
    d['Unrechable'] = c
    print(tabulate(d, headers="keys"))
    
print_ip_table(a)
