n=int(input("Introduzca un número entero mayor o igual que 0: "))       #SOLICITA VALOR

suma=1      #INICIALIZA SUMA
while (n<0):        #MIENTRAS N NO SEA MAYOR O IGUAL A 0
    n = int(input("Introduzca un número entero mayor o igual que 0: "))     #SOLICITA VALOR

for i in range (1,n+1,1):       #REPETIR N VECES
    suma=suma*i     #MULTIPLICAR I A SUMA

print("El sumatorio de los",n,"primeros números es igual a",suma)        #OUTPUT