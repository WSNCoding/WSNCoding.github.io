from os import *
ip= "10.111.242.248"
dataSize=1024
repeat=30
system("ping -n "+str(repeat)+" -l "+str(dataSize)+" "+ip)
