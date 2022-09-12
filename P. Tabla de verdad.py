from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausem, sleep_us as pausau
F = pin(13,pin.OUT)
A = pin(16,pin.IN, pin.PULL_DOWN)
B = pin(18,pin.IN, pin.PULL_DOWN)
C = pin(19,pin.IN, pin.PULL_DOWN)


while True:
  H = ((not A.value()*B.value())*C.value()+(not A.value())*B.value()*(not C.value())+A.value()*C.value())
  F.value(H)
  print(H)