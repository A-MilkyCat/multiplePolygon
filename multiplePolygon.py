import pyautogui, math

n = int(input())
pyautogui.sleep(5)
side = 200
nowX = side 
nowY = 0
theta = 360/n
sintheta = math.sin(math.radians(theta))
costheta = math.cos(math.radians(theta))
point = ['']*(n+1)
for i in range(n):
    # print(str(nowX) + ' , ' + str(nowY))
    point[i] = ([nowX,nowY])
    nextX = ((nowX*costheta - nowY*sintheta))
    nextY = ((nowX*sintheta + nowY*costheta))
    nowX = nextX
    nowY = nextY
point[n] = point[0]
propotion = 0.15
while side >= 50:
    last = [point[0][0], point[0][1]]
    nowX = point[0][0]
    nowY = point[0][1]
    # nextpoint[0] = [point[0][0]*(1-propotion) + point[0+1][0]*propotion, point[0][1]*(1-propotion) + point[0+1][1]*propotion]
    for i in range(1,n+1):
        nextX = point[i][0]
        nextY = point[i][1]
        pyautogui.drag(nextX - nowX, nowY-nextY, duration=0.1)
        nowX = nextX
        nowY = nextY
    for i in range(n):
        point[i] = [point[i][0]*(1-propotion) + point[i+1][0]*propotion, point[i][1]*(1-propotion) + point[i+1][1]*propotion]
    point[n] = point[0]
    pyautogui.drag(point[0][0] - last[0], last[1] - point[0][1],duration=0.1)
    side = math.sqrt((point[0][0]-point[1][0])**2 + (point[0][1]-point[1][1])**2)