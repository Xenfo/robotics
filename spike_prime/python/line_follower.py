from spike import ColorSensor, MotorPair, PrimeHub

hub = PrimeHub()
color_sensor = ColorSensor("E")
movement_motors = MotorPair("C", "D")

hub.motion_sensor.reset_yaw_angle()

class State():
    right = 1
    left = 2

def condition(threshold, state):
    if state == State.left:
        return yaw < threshold

    return yaw > threshold

def switch_state(state):
    if state == State.left:
        return State.right

    return State.left

state = State.left

while True:
    reflected_light = color_sensor.get_reflected_light()

    if reflected_light <= 60:
        hub.motion_sensor.reset_yaw_angle()
        movement_motors.start(speed=-50)
    else:
        threshold, (left, right) = 90, (-30, 30)
        if state == State.right:
            threshold, (left, right) = -90, (30, -30)

        yaw = hub.motion_sensor.get_yaw_angle()
        while condition(threshold, state) and reflected_light >= 60:
            reflected_light = color_sensor.get_reflected_light()
            movement_motors.start_tank(left, right)
            yaw = hub.motion_sensor.get_yaw_angle()
        state = switch_state(state)
