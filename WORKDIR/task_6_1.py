# -*- coding: utf-8 -*-
'''
Задание 6.1

Аналогично заданию 3.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''


#!/usr/bin/env	python3.6

#with open('ospf.txt', 'r')  as file:
#	print(file.read())

with open('ospf.txt', 'r')  as file:
	for line in file:
	    print(line.rstrip())
