'''
Instructions:
- Change motor and sensor ports to match the robot.
- If the robot turns the wrong way, change the sign of the turn speed (+ to - and vice versa).
- If the robot drives too fast or too slow, change the speed.
- Double check that the reflected value used in the code is good
'''

#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port

left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
left_color_sensor = ColorSensor(Port.S1)
right_color_sensor = ColorSensor(Port.S4)

black_reflection = 50  # Change this if this is not black.

while True:
    if left_color_sensor.reflection() > black_reflection and right_color_sensor.reflection() > black_reflection:
        # Change both motor speeds to -100 if it drives backwards.
        left_motor.run(100)
        right_motor.run(100)
    elif left_color_sensor.reflection() < black_reflection:
        # Invert signs if it turns the wrong way.
        left_motor.run(-100)
        right_motor.run(100)
    elif right_color_sensor.reflection() < black_reflection:
        # Invert signs if it turns the wrong way.
        left_motor.run(100)
        right_motor.run(-100)
