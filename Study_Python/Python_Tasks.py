Tasks

3.1 Replace Fast -> Gigabit in:
NAT =  "ip nat inside source list ACL interface FastEthernet0/1 overload"
>>> _string1 = 'NAT = ip nat inside source list ACL interface FastEthernet0/1 overload'
>>> _string2 = _string1.replace('Fast','Gigabit')
>>> _string2
'NAT = ip nat inside source list ACL interface GigabitEthernet0/1 overload'

3.2 Преобразовать строку MAC из формата XXXX:XXXX:XXXX в формат
XXXX.XXXX.XXXX
>>> _MAC1 = 'a277:ff3a:2487'
>>> _MAC2 = _MAC1.replace(':','.')
>>> _MAC2
'a277.ff3a.2487'

3.3 Получить из строки CONFIG список VLANов вида: ['1', '3', '10', '20', '30', '100']
>>> CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
>>> _config = (CONFIG.split())[-1].split(',')
“””сначала делим строку по пробелам, затем берем посл. Индекс и его тоже сплитуем по разделителю <запятая>”””
>>> _config
['1', '3', '10', '20', '30', '100']

3.4 Из строк command1 и command2 получить список VLANов, которые есть и в команде command1 и в команде command2.
>>> command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
>>> command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
>>> command3 = list(set((command1.split())[-1].split(',')) & set((command2.split())[-1].split(',')))
>>> command3
['1', '3', '100']

3.5 Список VLANS это список VLANов, собранных со всех устройств сети, поэтому в
списке есть повторяющиеся номера VLAN.
Из списка нужно получить уникальный список VLANов, отсортированный по
возрастанию номеров.
>>> VLANS = [ 10 , 20 , 30 , 1 , 2 , 100 , 10 , 30 , 3 , 4 , 10 ]
>>> vlan1 = sorted(list(set(VLANS)))
>>> vlan1
[1, 2, 3, 4, 10, 20, 30, 100]




3.6 Преобразовать в
Protocol:   OSPF
Prefix:       10.0.24.0/24
AD/Metric:   110/41
Next-Hop:   10.0.13.3
Last update:  3d18h
Outbound Interface: FastEthernet0/0

>>> ospf_route = 'O       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
list1 = (ospf_route.split())
print("%-20s %-15s" % ('Protocol:',((list1[0])+'SPF') ))
print("%-20s %-15s" % ('Prefix:',(list1[1])))
print("%-20s %-15s" % ('AD/Metric:',(list1[2]).strip('[]')))
print("%-20s %-15s" % ('Next-Hop:',(list1[4]).strip(',')))
print("%-20s %-15s" % ('Last update:',(list1[5]).strip(',')))
print("%-20s %-15s" % ('Outbound Interface:',(list1[6])))

3.7 Преобразовать MAC-адрес в двоичную строку (без двоеточий).
>>> MAC = 'AAAA:BBBB:CCCC'
mac1=bin(int((MAC.replace(':','')),16)).strip('0b')

>>> dict1 = dict ([ ('Protocol:',list1[0]) , ('Prefix:',list1[1]) , ('AD/Metric:',list1[2]) , ('Next-Hop:',list1[4]) , ('Last update:',list1[5]) ])
>>>>>> mac1
'1010101010101010101110111011101111001100110011'
!!!!! срезаны нули в конце!!!

3.8 Преобразовать IP-адрес (переменная IP) в двоичный формат и вывести вывод
столбцами на стандартный поток вывода, таким образом:
первой строкой должны идти десятичные значения байтов
второй строкой двоичные значения
Вывод должен быть упорядочен также, как в примере:
столбцами ширина столбца 10 символов

IP = '192.168.3.1'
ip1,ip2,ip3,ip4 = (IP.split('.'))
print("%15s %15s %15s %15s" % (ip1,ip2,ip3,ip4))
            192             168               3               1
print("{:>15}{:>15}{:>15}{:>15}".format('{:08b}'.format(int(ip1)) , '{:08b}'.format(int(ip2)) , '{:08b}'.format(int(ip3)) , '{:08b}'.format(int(ip4))))
       11000000       10101000       00000011       00000001


print("{:15} {:15}".format

3.9 Найти индекс последнего вхождения элемента.
Например, для списка num_list, число 10 последний раз встречается с индексом 4; в списке word_list, слово 'ruby' последний раз встречается с индексом 6.
Сделать решение общим (то есть, не привязываться к конкретному элементу в
конкретном списке) и проверить на двух списках, которые указаны и на разных элементах.

num_list = [ 10 ,  2 ,  30 ,  100 ,  10 ,  50 ,  11 ,  30 ,  15 ,  7 ]
word_list = [ 'python' ,  'ruby' ,  'perl' ,  'ruby' ,  'perl' , 'python' , 'ruby' , 'perl' ]


xxx - list, который мы цедим.

[ int(i) for i in xxx if xxx[-1]. ]





-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

4.1 Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24
'''
Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000
'''
#!/usr/bin/env python3.6

Address = input('Insert address and mask in format 192.168.0.1/24\n')
IP,mask = (Address.split('/'))
ip1,ip2,ip3,ip4 = (IP.split('.'))
print('Network:')
print("{:15}{:15}{:15}{:15}" .format(ip1,ip2,ip3,ip4))
print("{:15}{:15}{:15}{:15}".format('{:08b}'.format(int(ip1)) , '{:08b}'.format(int(ip2)) , '{:08b}'.format(int(ip3)) , '{:08b}'.format(int(ip4))))
print('\nMask:')
print('/' + mask)
mask_bin = ('1' * int(mask))
while len(mask_bin) < 32:
 mask_bin = (mask_bin + '0')
m1,m2,m3,m4 = mask_bin[0:8],mask_bin[8:16],mask_bin[16:24],mask_bin[24:32]
print("{:<15}{:<15}{:<15}{:<15}".format((int(m1,2)) , (int(m2,2)) , (int(m3,2)) , (int(m4,2))))
print("{:15}{:15}{:15}{:15}".format(m1,m2,m3,m4))



4.2

В задании создан словарь, с информацией и разных устройствах.

Вам нужно запросить у пользователя ввод имени устройства (r1, r2 или sw1).
И вывести информацию о соответствующем устройстве на стандартный поток вывода
(информация будет в виде словаря).


Пример выполнения скрипта (ключи могут быть в другом порядке), без if:'''
$ python3.6 task_4_2.py
Enter device name: r1
{'ios': '15.4', 'model': '4451', 'vendor': 'Cisco',
'location': '21 New Globe Walk', 'ip': '10.255.0.1'}
'''-----------------
#Словарь из задания смотри в задаче:
london_co = {
    '''...'''
}
------------
#!/usr/bin/env python3.6


london_co = {
    'r1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.1'
    },
    'r2' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.2'
    },
    'sw1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '3850',
    'ios': '3.6.XE',
    'ip': '10.255.0.101',
    'vlans': '10,20,30',
    'routing': True
    }
}
dev = input('Enter device name (r1,r2 or sw1): ')
print(london_co.get(dev))


-------------



import os
path = '/home/tarnad/Downloads/John_Steinbeck_Travels_With_Charlie/'
files = os.listdir(path)
i = 1

for file in files:
    number =
    os.rename(os.path.join(path, file), os.path.join(path, 'Travels' + str(i)+'.mp3'))
    i = i+1

-=-=-=-=-

'''backup
    import os
path = '/Users/myName/Desktop/directory'
files = os.listdir(path)
i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.jpg'))
    i = i+1
'''


-=-=-=-=-=-=-=-

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# makes a new list that has only the even elements of this list in it.
even = []
for n in a:
    if n % 2 == 0:
        even.append(n)
    else:
        pass

# same solution in one line:
even = [n for n in a if n % 2 == 0]
