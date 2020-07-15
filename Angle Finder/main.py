import math
from cv2 import cv2

path = 'angle.jpg'
img = cv2.imread(path)
pointList = []

#For find the mouse points
def mousePoints(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        size = len(pointList)
        if size != 0 and size % 3 != 0:
            cv2.line(img, tuple(pointList[round((size-1)/3)*3]), (x,y), (0 ,0, 255), 2)
        cv2.circle(img, (x, y), 5, (0, 0, 255), cv2.FILLED)
        pointList.append([x,y])
        # print(f'x:-{x}\ty:-{y}')
        # print(f'Points List:-{pointList}')
    

#Finding the slope/gradient
def gradient(pts1, pts2):
    return (pts2[1] - pts1[1])/(pts2[0] - pts1[0])

#Get the angle of the figure
def getAngle(pointList):
    pts1, pts2, pts3 = pointList[-3:]
    # print(f'Point 1:-{pts1}')
    # print(f'Point 2:-{pts2}')
    # print(f'Point 3:-{pts3}')
    m1 = gradient(pts1, pts2)
    m2 = gradient(pts1, pts3)
    angR = math.atan((m2-m1)/1+(m2*m1))
    angD = round(math.degrees(angR))
    # print(f'Angle:-{angD}')
    cv2.putText(img, str(angD), (pts1[0]-40, pts1[1]-20), cv2.FONT_HERSHEY_COMPLEX, 1.5, (0, 0, 255), 2)
    
while True:
    if len(pointList) % 3 == 0 and len(pointList) != 0:
        getAngle(pointList)
    cv2.imshow('Angle', img)
    cv2.setMouseCallback('Angle', mousePoints)
    if cv2.waitKey(1) & 0xff == ord('q'):
        pointList = []
        img = cv2.imread(path)
    # if cv2.waitKey(1) == 13:
    #     break

