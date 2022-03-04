from turtle import color
import cv2
import numpy as np

def draw(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        param['drawing'] = True
        param['ix'] = x
        param['iy'] = y

    elif event == cv2.EVENT_MOUSEMOVE:
        if param['drawing']:
            if param['mode']:
                cv2.rectangle( img, ( param['ix'], param['iy'] ), (x,y), color, -1)
            else:
                cv2.circle(img, (x,y), 5, color, -1)
    
    elif event == cv2.EVENT_LBUTTONUP:
        param['drawing'] = False

def change_color(x):
    global color
    color = [0] * 3
    color[x] = 255

if __name__ == '__main__':

    mouse_param = {'drawing':False, 'mode':True, 'ix':-1, 'iy':-1}
    
    color = [255,0,0]

    img = np.empty((512, 512, 3), np.uint8)
    img.fill(255)
    
    cv2.namedWindow('image')
    cv2.createTrackbar('Color', 'image', 0, 2, change_color)
    cv2.setMouseCallback('image', draw, mouse_param)
    
    while True:
        cv2.imshow('image', img)
        k = cv2.waitKey(1) & 0xFF

        if k == ord('m'):
            mouse_param['mode'] = not mouse_param['mode']
        
        elif k == ord('c'):
            img.fill(255)
        
        elif k == ord('q'):
            break
    
    cv2.destroyAllWindows()
