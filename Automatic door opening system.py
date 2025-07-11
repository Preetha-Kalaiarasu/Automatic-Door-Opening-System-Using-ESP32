from machine import Pin, ADC, PWM 
import time 
ldr_pin = ADC(Pin(34)) 
servo_pin = PWM(Pin(13), freq=100) 
def read_ldr(): 
 return ldr_pin.read() 
def control_servo(angle): 
 duty = (angle / 180) * 1023 
 servo_pin.duty(int(duty)) 
def open_door(): 
 print("Door opened") 
 control_servo(90) 
 time.sleep(5) 
def close_door(): 
 print("Door closed") 
 control_servo(0) 
def check_ldr(): 
 door_opened = False 
 while True: 
 ldr_value = read_ldr() 
 print("LDR Value:", ldr_value) 
 if ldr_value > 1000 and not door_opened: 
 open_door() 
 door_opened = True 
 elif ldr_value <= 1000 and door_opened: 
 close_door() 
 door_opened = False 
 time.sleep(1) 
check_ldr()