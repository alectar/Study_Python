#! python3
import shutil

f=open("/home/tarnad/Documents/Study/___Dev/example01.txt",'a')
f.write("erergw werg eg Line 1\n")
f.write(" wegw weg  rgw Line 2\n")
f.write(" weg wgwerge eg wgwg Line 3\n")
shutil.copy2("/home/tarnad/Documents/Study/___Dev/example01.txt",  "/home/tarnad/Documents/Life/example01.txt")
#c=f.readlines()
#print(c)
f.close()
