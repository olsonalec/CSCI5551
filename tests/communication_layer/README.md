# Communication Layer Test Script

The `test.py` python file in this folder is meant to allow users to test if the communication layer is working as expected via web sockets and `ros-bridge`.

<!-- ## ros-bridge

First check if `ros-bridge` is properly setup on the robot:

`rospack find rosbridge_server`
If the package exists start a WebSocket server:

`roslaunch rosbridge_server rosbridge_websocket.launch`

This will create a WebSocket server on the robot with the default port being `9090`. -->

## Setting up virtual environment
1. Create a virtual environment.
    ```
    # On Ubuntu, assuming you already have uv installed
    uv venv
    source .venv/bin/activate
    ```
2. Install the `websocket-client` package, which is necessary for `tests/communication_layer/test.py` to run.
    ```
    uv pip install websocket-client
    ```

## Test Script
**Must be connected to the Pi's Wi-Fi for these steps**
1. In two separate terminal, ssh into the Raspberry Pi.
2. In one of the terminals, run the following commands:
    ```
    sudo systemctl stop magni-base
    rosnode list
    ```
3. If `/teleop_twist_joy` or `/motor_node` show up, run `rosnode cleanup`.
4. Run:
    ```
    export TURTLEBOT3_MODEL=burger
    roslaunch turtlebot3_bringup turtlebot3_robot.launch
    ```
5. In the second terminal, run:
    ```
    roslaunch rosbridge_server rosbridge_websocket.launch unregister_timeout:=3600      # the timeout keeps the connection alive between multiple runs of test.py
    ```
6. In a third terminal that is *not* sshed into the Pi, run the `test.py` script (after editing the `PI_IP` variable accordingly)
7. The robot should move forward for one second and then turn for one second. If movement is not visible then try increasing speeds or duration in python file.
