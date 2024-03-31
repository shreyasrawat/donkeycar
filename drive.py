from donkeycar.parts.actuator import PCA9685
from time import sleep

'''
    -
    -
    - 
'''
throttle = PCA9685(0, address=64, busnum=None, frequency=60)
steering = PCA9685(1, address=64, busnum=None, frequency=60)
speed = 395
angle_straight = 360
angle_left = 90
angle_right = 450
cnt = 1
while True:
    print('Running............')
    '''
        Revers: 371(max)
        Forward: 395(min)
    '''
   #Go straight
    throttle.run(speed)
    if cnt == 4:
        steering.run(angle_right)
        sleep(1)
    steering.run(angle_straight)
    sleep(1)
    cnt +=1

   