chislo=int(input("Введите число:"))
ss=int(input("Введите систему счисления:"))
if not(ss!=2) or (ss!=8):
   quit()
   chislo2=''
while chislo>0:
    chislo2=str(chislo%ss)+chislo2
    chislo//=ss
print(chislo2)
   