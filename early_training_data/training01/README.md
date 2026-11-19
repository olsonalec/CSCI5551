# Training 1

The results from the first round of training for SAC and TD3 are compiled in this folder.
This folder includes both the raw data (in `.csv` files) and graphs that provide more information about how the agents compare against each other in key metrics such as total reward per episode, collision rate, success rate, navigation time, and path length.

About 21% of the episodes used for training contained an obstacle in the path of the robot from its starting position to the goal.
Since this percentage is quite low these trained agents are not consistently able to avoid obstacles that block the path.

New training is being done with training episodes that block the robots path nearly 100% of the time.

In this first round of training the TD3 agent did seem to perform better with a slightly higher success rate and a much lower collision rate.
However, the SAC agent had a slightly smaller path length on average and saved about a second per episode.

## Training episode variability

When training episodes are created the environment is created randomly.
That is the starting and goal positions are determined randomly and the number of obstacles along with their position is also decided randomly.
For the training I included a mix of difficulties as follows:

| difficulty name | percentage of episodes with this difficulty | description |
|---|---|---|
| empty | 10% | no obstacles in environment |
| sparse static | 20% | up to two static obstacles in environment |
| dense static | 25% | up to six and at least three static obstacles in environment |
| static and moving | 45% | up to six and at least two static obstacles in environment with up to two moving obstacles included |
