import json
import time

import websocket

PI_IP = ""  # Replace with IP address of Pi

ws = websocket.create_connection(f"ws://{PI_IP}:9090", timeout=5)


def move(linear=0.0, angular=0.0):
    """
    function creates and sends a move command to the opened websocket

    @linear: The linear speed that should be used for the move command
    @angular: The angular speed that should be used for the move command
    """
    message = {
        "op": "publish",
        "topic": "/cmd_vel",
        "type": "geometry_msgs/Twist",
        "msg": {
            "linear": {"x": linear, "y": 0, "z": 0},
            "angular": {"x": 0, "y": 0, "z": angular},
        },
    }

    ws.send(json.dumps(message))


def drive_for(linear, angular, duration):
    """
    function moves the robot for a set duration of time based on the given
    linear and angular velocities.
    The movement is completed at 10 Hz to ensure safety of robot in case the
    movement command is too fast.

    @linear: The linear speed that should be used for the move command
    @angular: The angular speed that should be used for the move command
    @duration: The amount of time this movement should be completed for
    """
    end = time.monotonic() + duration

    while time.monotonic() < end:
        move(linear, angular)
        time.sleep(0.1)


def main():
    try:
        print("Moving Forward")
        drive_for(0.05, 0.0, 1.0)
        drive_for(0.0, 0.0, 0.5)

        print("Rotating")
        drive_for(0.0, 0.3, 1.0)

    finally:
        # Send multiple stop commands to ensure robot is fully stopped before
        #   closing socket connection.
        for _ in range(5):
            move(0.0, 0.0)
            time.sleep(0.1)
        ws.close()


if __name__ == "__main__":
    main()
