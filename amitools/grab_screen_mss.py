import mss
import numpy as np
import cv2

screen_width = 1920  # 屏幕宽
screen_height = 1080  # 屏幕高
GAME_LEFT, GAME_TOP, GAME_WIDTH, GAME_HEIGHT = screen_width // 3, screen_height // 3, screen_width // 3, screen_height // 3  # 游戏内截图区域
RESIZE_WIN_WIDTH, RESIZE_WIN_HEIGHT = screen_width // 4, screen_height // 4  # 显示窗口大小
sct = mss.mss()
monitor = {
    'left': GAME_LEFT,
    'top': GAME_TOP,
    'width': GAME_WIDTH,
    'height': GAME_HEIGHT
}
window_name = 'test'

while True:
    img = sct.grab(monitor=monitor)
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)  # 将图片通道类型转为BGR
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)  # 创建窗口
    cv2.resizeWindow(window_name, RESIZE_WIN_WIDTH, RESIZE_WIN_HEIGHT)
    cv2.imshow(window_name, img)  # 显示窗口

    k = cv2.waitKey(1)
    if k % 256 == 27:  # ESC
        cv2.destroyAllWindows()
        exit('结束img_show 进程中...')
