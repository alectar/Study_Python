#! python3
#!/usr/bin/env python

-------------------

# How can you get a list of Python modules installed in your computer?
>>>help()
>>>modules

# How to find and install module?
>>> sudo pip search MODULE_NAME
>>> sudo pip install MODULE_NAME

-------------------

Function consist of
1) input
2) body
3) output


>>> import math    #  "math" - module

#--------------------------

>>> Z=23
>>> print('Creating %s...' % (Z))
Creating 23...

------> Strings<-------

c = 'Here'
>>> c
'Here'
>>> dir(c)
[........ , 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(c.capitalize)   - methods



counting from 0th element

>>> c = "Hi there!"
>>> type(c[0])
<type 'str'>
>>> c[0]
'H'
>>> c[:5]
'Hi th'
>>> c[0:5]
'Hi th'
>>> c[1:-3]
'i the'
>>> c[:-3]
'Hi the'
>>> c[-3]
'r'

---------->Lists<-----------

>>> myPets = ['Zophie', 'Pooka', 'Fat-tail']
>>> myPets[1]
'Pooka'
>>> del myPets[1] - function
>>> myPets.insert(2, "Ardo") - method
>>> myPets.append("Grenada")
>>> myPets.remove("Grenada")
>>> myPets.sort()           #for example:  sort(reverce=True)




---------->Tuples<----------
>>> t = ('Hello', 34.0, 4)
>>> type(t)
<type 'tuple'>

>>> print('Python is fun'[-3:])
fun


--------->Dictionaries<---------
>>> d = {"Name":"Jack", "Surname":"Reachers"}
>>> d["Surname"]
'Reachers'
>>> dir(d)
>>> help(d.keys)

>>> type(d)
<type 'dict'>

>>> money={"saving_account":200, "checking_account":100, "under_bed":[500,10,100]}
>>> money["under_bed"][1]
10







-------------------------------------
-----------Conditionals--------------
-------------------------------------


import random
SecretNumber = random.randint(1, 20)
print ("I've thought about number.. Try to guess it!")

for Guesses in range(1, 8):
    print ("Your choice:")
    guess = int(input())

    if guess < SecretNumber:
        print("Little more, i think")
#    elif guess > SecretNumber:
#        print("Too much")
    else:
        break
if guess == SecretNumber:
    print("Hey buddy, bingo! The number is " + str(SecretNumber) + "!")
    print("Number of attempts:" + str(Guesses) + "...")
else:
    print('No Way! Too much attempts..' + str(Guesses))


----------------------------
-----------loops------------
----------------------------


print('My name is')
i = 0
while i < 5:
 print('Jimmy five times (' + str(i) + ')')
 i = i + 1




for i in range(12,16):
    print(i)


-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# FILE OPERATIONS

# createing and writing to file:

>>> f=open("example1.txt",'w')
>>> f.write("Line 1\n")
>>> f.write("Line 2\n")
>>> f.write("Line 3\n")
>>> f=open("example1.txt",'r')
>>> c=f.readlines()
>>> print(c)
['Line 1\n', 'Line 2\n', 'Line 3\n']
>>> f.close()
...
>>> f=open("example1.txt",'a')
>>> f.write("Line 4\n")
>>> f=open("example1.txt",'r')
>>> c=f.readlines()
>>> print(c)
['Line 1\n', 'Line 2\n', 'Line 3\n', 'Line 4\n']


#------------------------------------
# example

#THIS_CODE.py:
f = open("example.txt",'r')
c =  f.readlines()
print(c)

>>> python THIS_CODE.py
['1 line\n', '2 line \n', '3 line\n']
>>> c = [i,rstrip("\n") for i in c]
...............SyntaxError: invalid syntax.........
>>> print(c01)


#--------------------------------------

import datetime
#
# this script creates an empty file
filename=datetime.datetime.now()
# creating file:
def create_file():
 with open(filename.strftime("%Y-%m-%d-%H-%M") + ".txt","w") as file:
  file.write(str(c1)+str(c2)+str(c3))
#
f1=open("file1.txt",'r')  #have to be created
c1=f1.readlines()
f2=open("file2.txt",'r')
c2=f2.readlines()
f3=open("file3.txt",'r')
c3=f3.readlines()
create_file()

# or the same...

import glob2
import datetime
#
filenames=glob2.glob("*.txt")
#
with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
    for filename in filenames:
        with open(filename,"r") as f:
            file.write(f.read()+"\n")


#--------------------------------------

>>> import os
>>> os.path.join('usr','local','bin')
'usr/local/bin'


# test.py file:
import sys
print "This is the name of the script: ", sys.argv[0]    #sys.argv - list, 0 - filename here.
print "Number of arguments: ", len(sys.argv)
print "The arguments are: " , str(sys.argv)

'''           output:
$ python test.py
This is the name of the script:  test.py
Number of arguments:  1
The arguments are:  ['test.py']

'''
#--------------------------------------

webbrowser.open('https://www.google.com/maps/place/')



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DICTIONARY CREATING

>>> r=['ISR2811','ISR2821','ASA5520','ASR9002']
>>> routers={k: [] for k in r}
>>> routers
{'ASR9002': [], 'ISR2811': [], 'ASA5520': [], 'ISR2821': []}
>>> routers['ASR9002'].append('Almaty_ro1')
>>> routers
{'ASR9002': ['Almaty_ro1'], 'ISR2811': [], 'ASA5520': [], 'ISR2821': []}

TUPLE CREATING (from list)

>>> list_keys = ['hostname', 'location', 'vendor', 'model', 'IOS', 'IP']
>>> tuple_keys = tuple(list_keys)
>>> tuple_keys
('hostname', 'location', 'vendor', 'model', 'IOS', 'IP')


>>> vlans = [10, 20, 30, 40]
>>> ','.join([str(vl) for vl in vlans])
'10,20,30,40'


>>> id(a)
4400936168

int(a, 2) - строка "а" будет воспринята, как двоичное число

>>> bin( 255 )
'0b11111111'


>>>import math
>>>math.factorial( 3 )
6




-------------------------
---------Methods---------
-------------------------

-=-=-=- Strings -=-=-=-

>>> string1 = 'interface FastEthernet1/0'
>>> string1[1]
'n'

>>>string1.upper()
'FASTETHERNET'

>>>string1.lower()
'fastethernet'

>>>string2.capitalize()
'Tunnel 0'

>>>string1 = 'Hello, hello, hello, hello'
>>>string1.count( 'hello' )
3

>>>string1 = 'interface FastEthernet0/1'
>>>string1.find( 'Fast' ) #на какой позиции первый символ подстроки
10

>>>string1 = 'FastEthernet0/1'
>>>string1.startswith( 'Fast' )
True
>>>string1.endswith( '0/1' )
True


>>>string1.replace( 'Fast','Gigabit')

>>>string1.strip('[]')

>>>commands = '10,20,30,100-200'
>>>commands.split( ',' )
['10', '20', '30', '100-200']

-=-=-=-=-Форматирование строк-=-=-=-=-=-

%s  - строка или любой другой объект в котором есть строковое представление
%d  - integer
%f  - float

vlan, mac, intf = ['100','aabb.cc80.7000','Gi0/1']
In [ 4 ]: print( "%15s %15s %15s"  % (vlan, mac, intf))
     100  aabb.cc80 .7000      Gi0/ 1

>>>'{:08b}' .format(10)
'00001010'

>>> print("{:08}{:>14}".format(255,'word'))
00000255          word

-=-=-=- Lists -=-=-=-

>>> i=['1','2','3','4','5']
>>> i.reverse()
>>> i
['5', '4', '3', '2', '1']
>>> print(i[0])
5
>>>',' .join(i[: -1 ])
'5,4,3,2'

>>> i.append( '300' )
>>> i
['5', '4', '3', '2', '1', '300']

>>> ii=['200','100']
>>> i.extend(ii)
>>> i
['5', '4', '3', '2', '1', '300', '200', '100']

>>> i.remove( '2' )
>>> i
['5', '4', '3', '1', '300', '200', '100']

>>>i.index('3')
2

>>>i.insert(3,'2')
>>> i
['5', '4', '3', '2', '1', '300', '200', '100']

-=-=-=- Dict -=-=-=-

>>>d.clear()

>>> d = {'a':'one','b':"two"}
>>> print(d.get('b'))
two

>>> d.keys()
['a', 'b']

>>> d.values()
['one', 'two']

>>> d.items()
[('a', 'one'), ('b', 'two')]

>>> del(d['a'])
>>>d
{'b': 'two'}

-=-=-=- Set -=-=-=-

>>> set1 = { 10 , 20 , 30 , 40 }
>>> set1.add(50)
>>> set1
set([40, 10, 20, 50, 30])

>>> set1.discard(50)
>>> set1
set([40, 10, 20, 30])

>>> set2 = {10,55,75}
>>> set1 & set2 # .intersection method
set([10])

-=-=-=-=- Проверка -=-=-=-

>>> "a" .isdigit()
False

>>> vlans = ['10','20','30','40','100-200']
>>> [int(vlan) for vlan in vlans if vlan.isdigit()]
[10, 20, 30, 40]

>>> "a".isalpha()
True

>>> "a10" .isalnum()
True

-=-=-=-=-=-=-=-=-=-=-

'Передача аргументов и ввод/вывод данных'



from  sys import argv
interface, vlan = argv[1:]

someshit=input('Wtf man?\n')
print( 'Your answer was \n {}' .format(someshit))

weight=input('Enter weight: ')
template = ['shit,shit,shit',
   '{} kilo of shit, and',
   'one more piece of shit']
print('\n'.join(template).format(weight))



-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

'Работа с файлами'



f = open( 'r1.txt', 'r' ) - открытие файла на чтение,


read()  - считывает содержимое файла в строку
readline()  - считывает файл построчно
readlines()  - считывает строки файла и создает список из строк
''''''
print(f.read())

или метод 'line'

for line in f:
    print(line)
------или-------
f.read().split('\n')

f.seek(0) - перевод курсора на строку 0

f.write('\nhostname r2') - запись строки в файл,

f.close()

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-



   T R Y




try :
    f = open( 'r1.txt' , 'r')
    print(f.read())
    except  IOError:
    print( 'No such file' )
    finally :
    f.close()
!

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

'''открытие файлов с'''
   W I T H




with open('r1.txt', 'r') as f:
    for line in f:
        print(line.rstrip())
!

'''---or---'''

with open('r1.txt', 'r') as f:
    print(f.read())
!


with open( 'r1.txt' ) as src, open( 'result.txt' ,'w') as dest:
    for line in src:
        if line.startswith( 'service' ):
            dest.write(line)
!



-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


'''функция на примере INT/ADDRESS/MASK'''


def config_interface (intf_name, ip_address, cidr_mask) :
    interface =  'interface {}'
    no_shut =  'no shutdown'
    ip_addr =  'ip address {} {}'
    result = []
    result.append(interface.format(intf_name))
    result.append(no_shut)
    mask_bits = int(cidr_mask.split( '/' )[ -1 ])
    bin_mask =  '1' *mask_bits +  '0' *( 32-mask_bits)
    dec_mask = [str(int(bin_mask[i : i+8],  2 ))  for  i  in  range( 0 , 25 , 8 )]
    dec_mask_str =  '.' .join(dec_mask)
    result.append(ip_addr.format(ip_address, dec_mask_str))
    return  result

config_interface( 'Fa0/1' , '192.168.11.23' , '/28' )

# или так передать аргументы:

interfaces_info = [[ 'Fa0/1' ,  '10.0.1.1' ,  '/24' ],
[ 'Fa0/2' ,  '10.0.2.1' ,  '/23' ],
[ 'Fa0/3' ,  '10.0.3.1' ,  '/24' ],
[ 'Fa0/4' ,  '10.0.4.1' ,  '/24' ],
[ 'Lo0' ,  '10.0.0.1' ,  '/32' ]]
for info in interfaces_info:
    print(config_interface(*info))

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


''' стандартные функции '''

 Built-in Functions
abs()       dict()      help()          min()       setattr()
all()       dir()       hex()           next()      slice()
any()       divmod()    id()            object()    sorted()
ascii()     enumerate() input()         oct()       staticmethod()
bin()       eval()      int()           open()      str()
bool()      exec()      isinstance()    ord()       sum()
bytearray() filter()    issubclass()    pow()       super()
bytes()     float()     iter()          print()     tuple()
callable()  format()    len()           property()  type()
chr()       frozenset() list()          range()     vars()
classmethod()getattr()  locals()        repr()      zip()
compile()   globals()   map()           reversed()  __import__()
complex()   hasattr()   max()           round()
delattr()   hash()      memoryview()    set()

# HOW TO FIND PATH FOR MODULE?

>>> import shutil
>>> shutil.__file__
'/usr/lib/python2.7/shutil.pyc'

-=-=-=-=-=-=-=-=-=-

print(*items, sep=' ', end='\n', file=sys.stdout, flush=False)


range(stop)
range(start, stop[step])


list_of_words = [ 'one' ,  'two' ,  'list' ,  '' ,  'dict' ]
sorted(list_of_words) # отсортирует в СПИСОК
sorted(list_of_words, reverse= True ) # отсортирует и реверснет
sorted(list_of_words, key=len) # отсортирует по ключу len


# enumerate - получение порядкового номера элемента в цикле
>>> list1 = [ 'str1' ,  'str2' ,  'str3' ]
>>> for position, string  in  enumerate(list1, 100): # с позиции 100
>>>    print(position, string)


# zip -возвращает итератор с кортежами, в котором n-ый кортеж состоит из n-ых
#элементов последовательностей, которые были переданы как аргументы
>>> a = [ 1 , 2 , 3 ]
>>> b = [ 100 , 200 , 300 ]
>>> list(zip(a,b))
( 1 ,  100 ), ( 2 ,  200 ), ( 3 ,  300 )]
>>> dict(zip(a,b))
{1: 100, 2: 200, 3: 300}

# all() возвращает True, если все элементы истина (или объект пустой)
>>> all( i.isdigit()  for  i  in  IP.split( '.' ))


# any() возвращает True, если хотя бы один элемент истина (или объект
пустой).
>>> any( i.isdigit()  for  i  in '10.1.1.a' .split( '.' ))


-=-=-=-=-=-=-=-=-=-=-=-=-=-
