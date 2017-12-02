#!/usr/bin/env	python3.6

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
