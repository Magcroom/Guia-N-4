from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausem, sleep_us as pausau
F = pin(13,pin.OUT)
A = pin(16,pin.IN, pin.PULL_DOWN)
B = pin(18,pin.IN, pin.PULL_DOWN)
C = pin(19,pin.IN, pin.PULL_DOWN)
D = pin(21,pin.IN, pin.PULL_DOWN)


while True:
  H=((A.value()*B.value())*((not(C.value()*D.value())))+D.value()+C.value())
  
  if H == 1:
    F.value(0)
    pausa(2)
    F.value(1)
    pausa(2)
    F.value(0)
  elif H == 2:
    F.value(1)
  elif D.value():
    F.value(1)
