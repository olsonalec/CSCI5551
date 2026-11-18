| Algorithm | Metric | Mean | Seed SD | 95% bootstrap interval | n |
| --- | --- | ---: | ---: | --- | ---: |
| SAC | success_rate | 0.9583 | 0.0144 | [0.9500, 0.9750] | 3 |
| SAC | collision_rate | 0.0333 | 0.0144 | [0.0250, 0.0500] | 3 |
| SAC | mean_success_time | 15.3735 | 0.6294 | [14.9947, 16.1000] | 3 |
| SAC | mean_path_length | 2.8834 | 0.0845 | [2.7886, 2.9505] | 3 |
| SAC | mean_return | 21.8970 | 0.4250 | [21.5023, 22.3469] | 3 |
| SAC | training_steps | 350000.0000 | 0.0000 | [350000.0000, 350000.0000] | 3 |
| TD3 | success_rate | 0.9750 | 0.0433 | [0.9250, 1.0000] | 3 |
| TD3 | collision_rate | 0.0167 | 0.0289 | [0.0000, 0.0500] | 3 |
| TD3 | mean_success_time | 16.6841 | 1.1786 | [15.8500, 18.0324] | 3 |
| TD3 | mean_path_length | 3.0069 | 0.1675 | [2.8912, 3.1990] | 3 |
| TD3 | mean_return | 22.2426 | 1.2735 | [20.7728, 23.0160] | 3 |
| TD3 | training_steps | 350000.0000 | 0.0000 | [350000.0000, 350000.0000] | 3 |

Uncertainty resamples training seeds, not individual episodes. N/A for n<2; successful time is undefined without successful episodes.
