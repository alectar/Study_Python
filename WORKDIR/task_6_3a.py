# -*- coding: utf-8 -*-
'''
Задание 6.3a

Сделать копию скрипта задания 6.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

import re
with open ('CAM_table.txt', 'r') as file02, open ('BUFFER.txt', 'w') as buff:
    for line in file02:
        MAC = re.search('\w\w\w\w.\w\w\w\w.\w\w\w\w', str(line))
        if MAC:
            List1 = line.lstrip( ).split("    ")
            del List1[2]
            line2 = (List1[0] + '    ' + List1[1] + '    ' + List1[2])
            buff.write(line2)
            #print(line2.rstrip())

with open('BUFFER.txt') as buff:
    for line in buff:
        if line.startswith('100'):
            print(line.rstrip())

with open('BUFFER.txt') as buff:
    for line in buff:
        if line.startswith('200'):
            print(line.rstrip())

with open('BUFFER.txt') as buff:
    for line in buff:
        if line.startswith('300'):
            print(line.rstrip())

with open('BUFFER.txt') as buff:
    for line in buff:
        if line.startswith('500'):
            print(line.rstrip())


# не смог решить лучше
