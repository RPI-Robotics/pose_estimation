import cv2
##import serial
import time
import mediapipe as mp

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap = cv2.VideoCapture(0)
pTime = 0
# 2d array to track the position of the landmarks 12X16
arr = [['.' for i in range(16)] for j in range(12)]
k=0
while k<50:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    # print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            ##print(id, lm)
            cx, cy = int(lm.x*w), int(lm.y*h)
            cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
            ##print(lm.y*h,lm.x*w)
            ##arr[int(lm.y*h/80)][int(lm.x*w/35)] = 0
            arr[min(int(lm.y*h/80),11)][min(int(lm.x*w/35), 15)] = 0 ##scale the input to fit on the grid
            ##print(h, w)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    k+=1

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)

## image IS REVERSED
# print array in grid format, the grid
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end="")
    print()


# 12 zones, 3upx4wide grid
# 9 pieces per zone, 3x3 grid
# 108 pieces total