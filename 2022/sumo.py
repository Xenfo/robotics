from spike import DistanceSensor, MotorPair

movement_motors = MotorPair("C", "D")
distance_sensor = DistanceSensor("B")

while True:
    distance = distance_sensor.get_distance_cm()
    if not distance == None and distance <= 80:
        movement_motors.start(speed=100)
    else:
        movement_motors.start_tank(-10, 20)
