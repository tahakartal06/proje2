import os
print("Aktif dizin giriniz: ",os.getcwd())

yer = os.getcwd()
yer += "/proje2"
os.chdir(yer)
open("taha.dt","w")