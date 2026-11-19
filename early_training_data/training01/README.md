# Training 1

The results from the first round of training for SAC and TD3 are compiled in this folder.
This folder includes both the raw data (in `.csv` files) and graphs that provide more information about how the agents compare against each other in key metrics such as total reward per episode, collision rate, success rate, navigation time, and path length.

About 21% of the episodes used for training contained an obstacle in the path of the robot from its starting position to the goal.
Since this percentage is quite low these trained agents are not consistently able to avoid obstacles that block the path.

New training is being done with training episodes that block the robots path nearly 100% of the time.

In this first round of training the TD3 agent did seem to perform better with a slightly higher success rate and a much lower collision rate.
However, the SAC agent had a slightly smaller path length on average and saved about a second per episode.
