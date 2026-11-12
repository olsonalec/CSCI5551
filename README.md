# CSCI 5551: Introduction to Intelligent Robotic Systems
Fall 2026

## A Comparative Analysis of SAC, TD3, and DWA for Mapless Goal-Directed Navigation in Unknown Environments


## Instructions for Working with the TurtleBot3 Burger

### Connecting to the Pi from your laptop
1. Connect the Raspberry Pi on the robot to a power source (such as the battery that's on the robot).
2. On your laptop, connect to the Pi's Wi-Fi.
3. ssh into the Pi

### Transferring data from your laptop to the Pi
While connected to the Pi's Wi-Fi:

    ```
    scp <path-to-local-file> username@pi_ip_address:<path-to-place-the-file>      # for a single file
    scp -r <path-to-local-file> username@pi_ip_address:<path-to-place-the-file>     # for a directory
    ```