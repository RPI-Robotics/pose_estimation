import cv2
import mediapipe as mp
import time

pTime = 0
cap = cv2.VideoCapture(0) # Camera 0 capture

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

while True:
  success, img = cap.read()
  imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  results = pose.process(imgRGB)
  if results.pose_landmarks:
    mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

  cTime = time.time()
  fps = 1/(cTime-pTime)
  pTime = cTime

  cv2.putText(img, str(int(fps)), (70,50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

  cv2.imshow("Image", img)
  cv2.waitKey(1)