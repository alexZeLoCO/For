a=int(input("Introduzca un valor: "))
b=int(input("Introduzca un valor mayor al anterior: "))

while (b<=a):
    a = int(input("Introduzca un valor: "))
    b = int(input("Introduzca un valor mayor al anterior: "))

for i in range (1,b+1,1):
    if (i%2==0):
        print (i,"(par)")
    else:
        print (i,"(impar)")