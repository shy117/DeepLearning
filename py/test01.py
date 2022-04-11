import cv2

img = cv2.imread('H:/DeepLearning/img/img.jpg')  # 读取图片../img/img.jpgimg

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.resizeWindow('img', 640, 360)
cv2.imshow('img', img)  # 显示图片

while 1:
    key = cv2.waitKey(0)
    if key == ord('q') or key == 27:  # 读取键盘按键‘q’或‘Esc’
        cv2.destroyAllWindows()  # 摧毁所有窗口
        break
