intentos =0
maximos = 3
import random
print("*****************")
print("adivina el numero")
print("*****************")
num2 =input("da me tu nombre  ")
print("tienes 3 intentos")
while intentos < maximos:
    num = int(input("coloca un numero del 1 al 10  "))
    mi = random.randint(1 , 10)
    if num == mi: 
        print("ganastes")
        print(num2)
        print(random.randint(1, 10)) 
    else:
        intentos += 1
        print(f"te que dan :{maximos - intentos} intentos")
        print("perdiste")
        print(num2)
        print("el numero era" ,mi)
    

if intentos == maximos:
    print("ups lo siento se te acabaron los intentos")
