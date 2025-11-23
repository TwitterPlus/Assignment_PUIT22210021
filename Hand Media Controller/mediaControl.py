import cv2
import mediapipe as mp
import time
import numpy as np
import pyautogui 

# --- Windows Volume Control Imports (Kept for reference) ---
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    model_complexity=0, 
    min_detection_confidence=0.7, 
    min_tracking_confidence=0.5
)
mp_drawing = mp.solutions.drawing_utils

# State management class for cooldown
class CooldownTimer:
    def __init__(self):
        self.last_action_time = time.time()
        # Cooldown for discrete actions (Play/Pause/Mute/Next/Prev) - 2.0 SECONDS
        # This prevents repeated actions when holding the gesture still.
        self.ACTION_COOLDOWN = 2.0 
        self.last_volume_action = time.time()
        # Very short cooldown for rapid volume changes (to feel responsive)
        self.VOLUME_COOLDOWN = 0.05 
        
timer = CooldownTimer()

# Mode is determined by handedness, but initialized for startup message
mode = 'VOLUME' 

# Start Video Capture (pTime and other initializations follow)
cap = cv2.VideoCapture(0)

# Simple Frame Rate counter (Removed FPS for cleaner UI)
pTime = 0 

# Define Custom Colors (BGR)
ORANGE_YELLOW = (0, 165, 255) # A softer, less intense orange/yellow
CORAL = (80, 127, 255) # For the finger gesture visuals

print("Starting Hand Gesture Controller (Left: Media, Right: Volume). Press 'q' to quit...")

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # 1. Process the Image
    image = cv2.flip(image, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        # We only process the first detected hand for simplicity
        hand_landmarks = results.multi_hand_landmarks[0]

        # Get the handedness (Right/Left hand)
        handedness = results.multi_handedness[0].classification[0].label
        
        # --- 1. Extract Key Landmarks for Logic ---
        lmList = []
        h, w, c = image.shape
        for id, lm in enumerate(hand_landmarks.landmark):
            cx, cy = int(lm.x * w), int(lm.y * h)
            lmList.append([id, cx, cy])
        
        if lmList:
            current_time = time.time()

            # Landmark IDs: Thumb Tip (4) and Index Finger Tip (8)
            x1, y1 = lmList[4][1], lmList[4][2] # Thumb Tip
            x2, y2 = lmList[8][1], lmList[8][2] # Index Tip
            
            # Calculate the Euclidean distance (length) for the volume pinch gesture
            length = np.hypot(x2 - x1, y2 - y1)

            # --- FINGER COUNTING ---
            # Index 1 = Index finger, Index 2 = Middle finger, etc.
            finger_tips = [8, 12, 16, 20]
            fingers_up = []
            
            # 1. Check Thumb (x-axis for side view)
            if lmList[4][1] > lmList[3][1]:
                fingers_up.append(1)
            else:
                fingers_up.append(0)

            # 2. Check other 4 fingers (y-axis for vertical tips)
            for tip_id in finger_tips:
                if lmList[tip_id][2] < lmList[tip_id - 2][2]: 
                    fingers_up.append(1)
                else:
                    fingers_up.append(0)
            
            total_fingers_up = sum(fingers_up)
            # ------------------------------------

            # =========================================================
            # A. MODE ASSIGNMENT (Handedness determines the mode)
            # =========================================================
            if handedness == 'Left':
                mode = 'MEDIA'
            else:
                mode = 'VOLUME'
                
            # =========================================================
            # B. MODE-SPECIFIC CONTROL LOGIC
            # =========================================================
            
            if mode == 'VOLUME':
                # --- VOLUME CONTROL LOGIC (Thumb-Index Distance) ---
                
                # Map length (thumb-index distance) to volume percentage
                # Calibrate the input range (20, 200) to your hand's min/max distance
                volPer = np.interp(length, [20, 200], [0, 100])
                volPer = np.clip(volPer, 0, 100) # Clamp between 0 and 100

                if current_time - timer.last_volume_action > timer.VOLUME_COOLDOWN:
                    # Use extreme thresholds to trigger volume keys repeatedly
                    if volPer > 95:
                        pyautogui.press('volumeup')
                        timer.last_volume_action = current_time
                        
                    elif volPer < 5: 
                        pyautogui.press('volumedown')
                        timer.last_volume_action = current_time
                
                # --- VOLUME VISUALS (ONLY drawn in VOLUME mode) ---
                
                # Finger Distance Visual Feedback (Coral color and less thick)
                cv2.circle(image, (x1, y1), 8, CORAL, cv2.FILLED) # Reduced size
                cv2.circle(image, (x2, y2), 8, CORAL, cv2.FILLED) # Reduced size
                cv2.line(image, (x1, y1), (x2, y2), CORAL, 2) # Reduced thickness

                # Draw Volume Bar and Percentage (ORANGE_YELLOW)
                bar_height = np.interp(volPer, [0, 100], [400, 150])
                cv2.rectangle(image, (50, 150), (85, 400), ORANGE_YELLOW, 3) # Bar outline
                cv2.rectangle(image, (50, int(bar_height)), (85, 400), ORANGE_YELLOW, cv2.FILLED) # Bar fill
                cv2.putText(image, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_PLAIN, 2, ORANGE_YELLOW, 3) # Percentage
            
            
            elif mode == 'MEDIA':
                
                # --- DISCRETE GESTURE LOGIC (Play/Pause/Mute/Next/Prev) ---

                # GESTURE 3: All 5 fingers up (Open Palm) -> Next Track
                if total_fingers_up == 5:
                    if current_time - timer.last_action_time > timer.ACTION_COOLDOWN:
                        print("Action: Next Track")
                        pyautogui.press('nexttrack') 
                        timer.last_action_time = current_time

                # GESTURE 4: 4 fingers up (Thumb Tucked) -> Previous Track
                elif total_fingers_up == 4:
                    if current_time - timer.last_action_time > timer.ACTION_COOLDOWN:
                        print("Action: Previous Track")
                        pyautogui.press('prevtrack') 
                        timer.last_action_time = current_time

                # GESTURE 1 (Existing): Index + Middle Finger Up (Victory sign) -> Play/Pause
                elif total_fingers_up == 2 and fingers_up[1] == 1 and fingers_up[2] == 1:
                    if current_time - timer.last_action_time > timer.ACTION_COOLDOWN:
                        print("Action: Play/Pause")
                        pyautogui.press('playpause') 
                        timer.last_action_time = current_time 

                # GESTURE 2 (Existing): Closed Fist (0 fingers up) -> Mute Toggle
                # This now comes directly after the 2-finger gesture.
                elif total_fingers_up == 0:
                     if current_time - timer.last_action_time > timer.ACTION_COOLDOWN:
                        print("Action: Mute")
                        pyautogui.press('volumemute')
                        timer.last_action_time = current_time
                        
            
            # Draw ALL hand landmarks for the current hand
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Draw the current mode status (Top-left corner)
        cv2.putText(image, f"MODE: {mode} ({handedness})", (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, ORANGE_YELLOW, 2)


    # 3. Display Frame Rate (CODE REMOVED FOR CLEANER UI)
    cTime = time.time()
    pTime = cTime
    
    # 4. Show the Output
    cv2.imshow('Hand Gesture Media Controller', image)

    # Exit on 'q' press
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()