from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausem, sleep_us as pausau
F = pin(13,pin.OUT)
A = pin(16,pin.IN, pin.PULL_DOWN)
B = pin(18,pin.IN, pin.PULL_DOWN)
C = pin(19,pin.IN, pin.PULL_DOWN)
D = pin(21,pin.IN, pin.PULL_DOWN)
 
while True:
  H = C.value() + A.value() + B.value() + D.value()
  if H == 0:
    F.value(1)
  else:
      F.value(0)
   