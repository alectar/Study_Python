#! Python3
import sys

A = int(sys.argv[1])
B = int(sys.argv[3])
Opr = sys.argv[2]
print(str(A) + ' and '+ str(B))
if Opr == '+':
    print (str(A) + ' ' + Opr + ' ' + str(B) + ' = ' + str(A+B))
elif Opr == '-':
    print(str(A) + ' ' + Opr + ' ' + str(B) + ' = ' + str(A-B))
elif (Opr == 'x') or (Opr == '*'):
    print(str(A) + ' * ' + str(B) + ' = ' + str(A*B))
elif (Opr == '/'):
    print(str(A) + ' ' + Opr + ' ' + str(B) + ' = ' + str(A/B))
else:
    print('ERROR )=')