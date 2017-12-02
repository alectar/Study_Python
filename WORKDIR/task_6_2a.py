# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''


# it works:
ignore = ['duplex', 'alias', 'Current configuration']
with open('config_sw1.txt','r') as ssss:
    for line in ssss:
        if (ignore[0]  in line) or (ignore[1]  in line) or (ignore[2]  in line):
            pass
        else:
            if line.startswith('!') == False:
                print(line.rstrip())
