import cv2
import mediapipe as mp
import time

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture("video5.mp4")

pTime = 0
while True:
    
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    print(results.pose_landmarks)
    
    if results.pose_landmarks:  #landmark olursa eğer yani insan vücudunu tespit ederse iskeleti oluştursun.
        mpDraw.draw_landmarks(img, results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        
 #üstte iskelet oluştu fakat istediğimiz eklem noktalarını oluşturmak için:
        
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, _ = img.shape
            cx, cy = int(lm.x*w), int(lm.y*h)
            
            if id == 13:
                cv2.circle(img, (cx,cy), 5, (255,0,0), cv2.FILLED)
                
    cTime =  time.time()
    fps = 1/(cTime - pTime)      
    pTime = cTime
    cv2.putText(img, "FPS :" + str(int(fps)), (10,65), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0),2)            
    
    
    img = cv2.resize(img, (480, 640), interpolation=cv2.INTER_LINEAR) #video ekran sığmadığından boyutlandırdım.
    cv2.imshow("poz",img)
    cv2.waitKey(10) #video akış hızı
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    