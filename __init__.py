import cv2

cap = cv2.VideoCapture(0)   #(id of primary webcam)
# cap.set(3,640)      #(id of width,dimension)
# cap.set(4,480)      #(id of height,dimension)
# cap.set(10,100)     #(if for brightness, brightness level)
print(cap)

while True:
    success, img = cap.read()
    face_cascade = cv2.CascadeClassifier("resources/face.xml")
    # body_cascade = cv2.CascadeClassifier("resources/body.xml")

    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(imgGray,1.1,4)
    # bodies = body_cascade.detectMultiScale(imgGray,1.1,4)

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    
    # for(x,y,w,h) in bodies:
    #     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("FaceCam",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break