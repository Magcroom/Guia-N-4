from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausem, sleep_us as pausau
MOTOR = pin(13,pin.OUT)
A = pin(16,pin.IN, pin.PULL_DOWN)
B = pin(18,pin.IN, pin.PULL_DOWN)
C = pin(19,pin.IN, pin.PULL_DOWN)
LAMP = pin(12,pin.OUT)

while True:
  H = (A.value()+B.value()+C.value())
  
  if  H == 3 :
      MOTOR.value(1)
      pausem(500)
      MOTOR.value(0)
  elif H == 2 :
      LAMP.value(1)
      MOTOR.value(1)
      pausem(500)
      LAMP.value(0)
      MOTOR.value(0)
  elif H == 1 :
      LAMP.value(1)
      pausem(500)
      LAMP.value(0)
      