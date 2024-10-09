import cv2

video_capture = cv2.VideoCapture(0)
while video_capture.isOpened():
   # Captures video_capture frame by frame
    _, frame = video_capture.read() 
  
    # To capture image in monochrome                    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
      
    # calls the detect() function    
    canvas = detect(gray, frame)   
  
    # Displays the result on camera feed                     
    cv2.imshow('Video', canvas) 
  
    # The control breaks once q key is pressed                        
    if cv2.waitKey(1) & 0xff == ord('q'):               
        break
  
# Release the capture once all the processing is done.
video_capture.release()                                 
cv2.destroyAllWindows()