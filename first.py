import os
import sys

#os.fdisk -l | grep Диск
f = input("введите название диска:")






os.system('df -h|grep ' + f)
