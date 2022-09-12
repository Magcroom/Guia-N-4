from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausem, sleep_us as pausau
F = pin(13,pin.OUT)
A = pin(16,pin.IN, pin.PULL_DOWN)
B = pin(18,pin.IN, pin.PULL_DOWN)
C = pin(19,pin.IN, pin.PULL_DOWN)
D = pin(21,pin.IN, pin.PULL_DOWN)
while True:
    print ("Digite 1 para continuar con los resultados de las ecuaciones indicadas")
    numero = int (input("Digite 0 si quiere cerrar el programa: "))
    if numero == 1:
        print("oprima los botones para solicitar la operacion que necesita")
        pausa(2)
        Sumas = (A.value() or B.value()) or (C.value() or D.value())
        print("Primera ecuacion")
        print (Sumas)
        Mult = (A.value() and B.value()) and (C.value() and D.value())
        print("Segunda ecuacion")
        print (Mult)
        NotS = (not (A.value() or B.value())) or (C.value() or D.value())
        print("Tercera ecuacion")
        print (NotS)
        Opera = (not (A.value() or B.value()) and (not (C.value() and (not D.value()))))
        print("Cuarta ecuacion")
        print (Opera)
        pausa(5)
    else:
        print("Hasta pronto")
        break