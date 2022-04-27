import math, pyautogui

n = 0
print('請輸入為正幾角形(不為偶數) : ', end='')
while n %2 != 1:
    n = int(input())
pyautogui.sleep(5)
side = 100
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
point[n] = [side,0]
# for i in range(len(point)):
#     for j in range(len(point[i])):
#         print(point[i][j],end=' ')
#     print('')
s = int(n/2)
i = 0
j = s +1
IsJorI = True # true = i , false = j
while j != n+1:
    if IsJorI == True:
        nextX = point[i][0]
        nextY = point[i][1]
        i += 1
        IsJorI = False
    else:
        nextX = point[j][0]
        nextY = point[j][1]
        j += 1
        IsJorI = True
    pyautogui.drag(nextX - nowX, nowY-nextY, duration=0.05)
    nowX = nextX
    nowY = nextY