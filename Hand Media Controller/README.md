# Hand Gesture Media Controller

This Python script utilizes computer vision and hand tracking to control media playback and system volume using hand gestures. It leverages `mediapipe` for hand detection and `pyautogui` for sending keyboard commands to the operating system.

## Features

- **Dynamic Mode Switching**: Automatically switches between "VOLUME" and "MEDIA" control modes based on the detected hand (Right hand for Volume, Left hand for Media).
- **Volume Control**: Adjusts system volume by pinching the thumb and index finger. The closer the fingers, the lower the volume.
- **Media Playback Control**:
    - **Play/Pause**: "Victory" sign (Index and Middle fingers up).
    - **Mute/Unmute**: Closed fist (0 fingers up).
    - **Next Track**: Open palm (All 5 fingers up).
    - **Previous Track**: Four fingers up (Thumb tucked in).
- **Visual Feedback**: Displays hand landmarks, current mode, and volume level directly on the camera feed.
- **Cooldown Mechanism**: Prevents rapid, unintended actions by implementing cooldown timers for both volume adjustments and discrete media controls.

## Requirements

- Python 3.x (Python 3.9 recommended)
- `opencv-python`
- `mediapipe`
- `numpy`
- `pyautogui`
- `pycaw` (for Windows-specific volume control, though `pyautogui` is used for cross-platform key presses)
- `comtypes` (dependency for `pycaw`)

## Installation

1. **Clone the repository (or download the script):**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install the required Python packages:**
   ```bash
   pip install opencv-python mediapipe numpy pyautogui pycaw comtypes
   ```

## How to Run

1. **Execute the script:**
   ```bash
   python mediaControl3.py
   ```

2. **Grant Camera Access**: If prompted, allow the script to access your webcam.

3. **Control with Gestures:**
   - **Right Hand**: Activates "VOLUME" mode.
     - Pinch your thumb and index finger closer together to decrease volume.
     - Move them further apart to increase volume.
   - **Left Hand**: Activates "MEDIA" mode.
     - **Play/Pause**: Hold up your index and middle fingers (like a peace sign).
     - **Mute/Unmute**: Form a closed fist.
     - **Next Track**: Open your palm (all five fingers extended).
     - **Previous Track**: Hold up four fingers (thumb tucked in).

4. **Quit**: Press the 'q' key on your keyboard to exit the application.

## Configuration

- **`ACTION_COOLDOWN`**: (Default: `2.0` seconds) Adjust this value in the `CooldownTimer` class to change how quickly discrete media actions (Play/Pause, Mute, Next/Prev) can be triggered. A higher value means less responsiveness but fewer accidental triggers.
- **`VOLUME_COOLDOWN`**: (Default: `0.05` seconds) Adjust this for volume control responsiveness. A lower value allows for faster volume changes.
- **`volPer` mapping**: The `np.interp(length, [20, 200], [0, 100])` line maps the distance between thumb and index finger to a volume percentage. You might need to adjust the `[20, 200]` range based on your hand size and typical gesture range for optimal volume control.
- **`volPer` thresholds**: The `volPer > 95` and `volPer < 5` thresholds for `volumeup` and `volumedown` can be adjusted to make the volume control more or less sensitive to extreme pinch gestures.

## Troubleshooting

- **"Ignoring empty camera frame."**: Ensure your webcam is properly connected and not being used by another application.
- **Gestures not recognized**:
    - Make sure your hand is well-lit and clearly visible to the camera.
    - Try to perform gestures distinctly.
    - Adjust `min_detection_confidence` and `min_tracking_confidence` in `mp_hands.Hands()` if detection is poor, though default values are usually good.
- **`pyautogui` issues**: On some systems, `pyautogui` might require additional permissions or setup. Refer to `pyautogui` documentation for platform-specific issues.
- **`pycaw` errors**: `pycaw` is Windows-specific. If you're on another OS, the `pycaw` imports will still be there but the volume control logic relies on `pyautogui.press('volumeup')` etc., which is cross-platform for common media keys.

## Future Enhancements

- Add visual indicators for detected gestures.
- Implement more complex gestures for additional controls (e.g., fast forward/rewind).
- Allow user configuration of gesture-to-action mappings.
- Support for multiple hands simultaneously.
- Integration with specific media players.

## License

This project is open-source and available under the [MIT License](LICENSE).

---
