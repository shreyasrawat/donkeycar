from donkeycar.parts.actuator import PulseController
from donkeycar.parts import pins
import time

pwm_pin = 'PCA9685.1:40.0'
pwm_steer = 'PCA9685.1:40.1'
pwmFreq = 60

try:
    pwm_pin = pins.pwm_pin_by_id(pwm_pin)
    pwm_steer = pins.pwm_pin_by_id(pwm_steer)
except ValueError as e:
    print(e)
    print("See pins.py for a description of pin specification strings.")
    exit(-1)
print(f'init pin {pwm_pin}')
freq = int(pwmFreq)
print(f"Using PWM freq: {freq}")
car = PulseController(pwm_pin)
steer = PulseController(pwm_steer)
#input_prompt = "Enter a PWM setting to test ('q' for quit) (0-1500): "
#print()
car.run(10)
time.sleep(1)
cnt = 0
while True:
    try:
        #val = input(input_prompt)
        #if val == 'q' or val == 'Q':
            #break
        #pmw = int(val)
        car.run(395)
        if cnt%4 == 0:
            steer.run(90)
        elif cnt%7 == 0:
            steer.run(450)
        else:
            steer.run(360)
        time.sleep(2)
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt received, exit.")
        break
    except Exception as ex:
        print(f"Oops, {ex}")
    cnt += 1

car.run(0)
steer.run(360)
