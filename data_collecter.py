
import cv2
cap = cv2.VideoCapture(0)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 180)
cp=0
while True:
    cp+=1
    ret, frame = cap.read()
    #frame= cv2.flip(frame, -2)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('a') and cp !=50 :
        cv2.imwrite("image"+str(cp)+".jpeg",frame)
        print("image"+str(cp)+".jpeg well save it")
        #break
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
        
cap.release()
cv2.destroyAllWindows()
