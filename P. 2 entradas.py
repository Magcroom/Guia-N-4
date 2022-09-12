from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausem, sleep_us as pausau
F = pin(13,pin.OUT)
A = pin(16,pin.IN, pin.PULL_DOWN)
B = pin(18,pin.IN, pin.PULL_DOWN)
 
 
while True:
    print ("Digite 1 para continuar con los resultados de las ecuaciones indicadas")
    numero = int (input("Digite 0 si quiere cerrar el programa: "))
    if numero == 1:
        print("oprima los botones para solicitar la operacion que necesita")
        pausa(2)
        Sumas = (A.value()  and C.value())
        print("A AND B")
        print (Sumas)
        Mult = (not(B.value()))
        print("NOT B")
        print (Mult)
        NotS = ( not(A.value()))
        print("NOT A")
        print (NotS)
        Opera = (not(A.value() and B.value()))
        print("NOT (A AND B)")
        print (Opera)
        pausa(5)
    else:
        print("Hasta pronto")
        break
