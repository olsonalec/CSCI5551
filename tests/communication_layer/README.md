# Communication Layer Test Script

The `test.py` python file in this folder is meant to allow users to test if the communication layer is working as expected via web sockets and `ros-bridge`.

## ros-bridge

First check if `ros-bridge` is properly setup on the robot:

`rospack find rosbridge_server`
If the package exists start a WebSocket server:

`roslaunch rosbridge_server rosbridge_websocket.launch`

This will create a WebSocket server on the robot with the default port being `9090`.

## Test Script

Run the `test.py` python script, you should expect the robot to move forward for one second and then turn for one second.
If movement is not visible then try increasing speeds or duration in python file.
