import cv2
import mediapipe as mp
import pyautogui
import time

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
tipIds = [4, 8, 12, 16, 20]

last_action = None  # to avoid repeating key presses

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lmList = []
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((id, cx, cy))
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            if lmList:
                fingers = []
                # Thumb
                if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
                # Other fingers
                for id in range(1, 5):
                    if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                totalFingers = fingers.count(1)
                cv2.putText(img, f'Fingers: {totalFingers}', (10, 70),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

                # 🎮 Finger Gestures to Key Events
                if totalFingers == 2 and last_action != 'right':
                    pyautogui.keyUp('left')  # ensure left is released
                    pyautogui.keyDown('right')
                    last_action = 'right'
                    print("➡️ Accelerate")
                elif totalFingers == 1 and last_action != 'left':
                    pyautogui.keyUp('right')  # ensure right is released
                    pyautogui.keyDown('left')
                    last_action = 'left'
                    print("⬅️ Brake")
                elif totalFingers == 0 and last_action != 'none':
                    pyautogui.keyUp('right')
                    pyautogui.keyUp('left')
                    last_action = 'none'
                    print("🛑 Stop")

    cv2.imshow("Gesture Control - Hill Climb", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
pyautogui.keyUp('right')
pyautogui.keyUp('left')
