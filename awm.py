import os
from os import path,system
from platform import uname
arch=uname().machine.lower()
if path.isfile("aw.cpython-311.so"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/BestProfessionals/PROFESSIONAL/main/aw.cpython-311.so -o aw.cpython-311.so")
if path.isfile("aw.cpython-311.so"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/BestProfessionals/PROFESSIONAL/main/aw.cpython-311.so -o aw.cpython-311.so")

if 'aarch' in arch:
    arch = 'aarch'
    print('\033[1;32m\nCongratulatings! Your Deviec Support This Tools')
   from aw import
    aw.menu()
else:exit('\033[1;31m Sorry System or device not supported ')
    


