import cv2  #opencv library

import imutils   #imutils library

yellowLower = (20,100,100)   #lower range - HSV value of yellow(can be find in google)

yellowUpper = (30,255,255)   #upper range - HSV value of yellow(can be find in google)

camera = cv2.VideoCapture(0)   #primary camera initialise

while True :      #infinite loop to run camera

    _ ,img = camera.read()  #read frame from camera

    resizedImg = imutils.resize(img,width = 500)   #resize image

    blurImg = cv2.GaussianBlur(resizedImg , (11,11),0)   #smoothen image

    hsv = cv2.cvtColor(blurImg,cv2.COLOR_BGR2HSV)    #convert to HSV

    mask = cv2.inRange(hsv,yellowLower,yellowUpper)   #to detect yellow color in frame

    mask = cv2.erode(mask,None,iterations = 2)    #to remove left overs

    mask = cv2.dilate(mask,None,iterations = 2)   #to remove left overs

    contours = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]   #to find contours(border)

    center = None

    if len(contours) > 0:       #length of contours

            c = max(contours,key = cv2.contourArea)   #to find contour area

            ((x,y), radius) = cv2.minEnclosingCircle(c)   #to draw enclosing circle

            M = cv2.moments(c)    #to find center point of entire area

            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))   #center formula

            if radius > 10 :    #to detect particular radius object

                cv2.circle(resizedImg, (int(x),int(y)),int(radius) , (0,255,0) ,2)  #to draw circle

                cv2.circle(resizedImg , center,5,(0,0,255),-1)     #to draw center point

                print(center,radius)

                if radius > 200:     #track object (depends on object - need to change comparison values 
                      print("stop")
                else:
                      if(center[0] < 250):
                          print("right")
                      elif(center[0] > 250):
                          print("left")
                      elif(radius < 200):
                          print("front")


    cv2.imshow("Frame", resizedImg)   #to display

    key = cv2.waitKey(10)  # wait for 10 frames

    if key == 27:    #when esc key is pressed, close camera
        break

camera.release()   #release camera

cv2.destroyAllWindows()   #close window

         
        
    
