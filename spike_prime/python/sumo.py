import time
from spike import ColorSensor, DistanceSensor, MotorPair, PrimeHub

hub = PrimeHub()
color_sensor = ColorSensor("E")
movement_motors = MotorPair("C", "D")
distance_sensor = DistanceSensor("B")

hub.motion_sensor.reset_yaw_angle()

has_reached_edge = False

def get_away_from_edge():
    time_end = time.time() + 3
    while time.time() < time_end:
        movement_motors.start(speed=50)

    yaw = hub.motion_sensor.get_yaw_angle()
    while yaw < 175 and yaw > -175:
        movement_motors.start_tank(-20, 30)
        yaw = hub.motion_sensor.get_yaw_angle()

    time_end = time.time() + 3
    while time.time() < time_end:
        movement_motors.start(speed=-50)

while True:
    reflected_light = color_sensor.get_reflected_light()
    
    if not reflected_light <= 40 and not has_reached_edge:
        movement_motors.start(speed=-30)
    elif reflected_light <= 40 and not has_reached_edge:
        has_reached_edge = True

        get_away_from_edge()

    if has_reached_edge:
        distance = distance_sensor.get_distance_cm()

        if (not distance == None and distance <= 80) and not reflected_light <= 40:
            movement_motors.start(speed=-100)
        elif reflected_light <= 40:
            get_away_from_edge()
        else:
            movement_motors.start_tank(-10, 20)
