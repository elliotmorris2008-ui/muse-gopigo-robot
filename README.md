# Blink-Controlled GoPiGo3 Robot (Muse 2 EEG)

A Muse 2 EEG headband controls a GoPiGo3 robot using eye blinks. I built this to test how accurately a consumer EEG headband can drive a robot in real time.

**Note:** the system reads eye-blink artifacts from the forehead sensors. It does not read thoughts or brain waves.

## How it works

Muse 2 -> BrainFlow (Python, Mac) -> UDP over WiFi -> Raspberry Pi 3B on GoPiGo3 -> motors

- `brain.py` (Mac): reads the headband with BrainFlow and looks at the left forehead sensor. A blink pushes the signal to the sensor's maximum, so the code counts how many of the last 50 samples have an absolute value above 900. More than 35 counts as a blink event. It then waits 0.3 s and checks again. If the signal is still high, it sends a turn command (this responds to double blinks). If not, it sends a forward command. A 2 s pause follows each command.
- `robot.py` (Raspberry Pi): listens for UDP messages and drives the robot.

| Gesture | Command |
|---|---|
| Single blink | Forward 20 cm |
| Double blink | Turn 45 degrees |

## Hardware

- Muse 2 EEG headband
- GoPiGo3 robot with a Raspberry Pi 3B (powered by a USB power bank)
- Mac laptop

## Results

Each session was 30 trials, one gesture about every 5 seconds, at the same detection threshold.

| Gesture | Session 1 | Session 2 |
|---|---|---|
| Single blink | 70% (21/30) | 50% (15/30) | 2 trials TBD |
| Double blink | 33% (10/30) | 36.7% (11/30) | 2 trials TBD |

At rest (sitting still), there were 0 false triggers in 90 seconds.

## Limitations

- Accuracy was moderate and varied between sessions. Headset fit and signal noise likely matter, and with only 30 trials per session the uncertainty is large.
- I first tried to detect jaw clenches, but that was unreliable. The sustained-signal check responds mainly to double blinks, so I use that gesture instead.
- Results are from one person on one headset.

## Future work

- Detect blinks as separate peaks and use frequency analysis instead of a simple threshold.
- Add a camera to the robot.
- Test more people and more thresholds.

## Author

Elliot Morris
