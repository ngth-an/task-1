import cv2 as cv
import numpy as np

check_point1 = False
check_point2 = False

x1, y1, x2, y2 = -1, -1, -1, -1
background = np.zeros((455, 455, 3))
check_draw = False
def draw_line(background=background, radius=100):
    def draw_a_line(event, x, y, flags, param):
        global check_point1, check_point2, check_draw, x1, y1, x2, y2
        if event == cv.EVENT_LBUTTONDOWN and check_point1 == False and check_point2 == False and check_draw == False:
            x1, y1 = x, y
            check_point1 = True
        elif event == cv.EVENT_LBUTTONDOWN and check_point1 == True and check_point2 == False and check_draw == False:
            x2, y2 = x, y
            check_point2 = True
        elif event == cv.EVENT_MOUSEMOVE and check_point1 == False and check_point2 == False and check_draw == False:
            print("founding x1, y1")
        elif event == cv.EVENT_MOUSEMOVE and check_point1 == True and check_point2 == False and check_draw == False:
            print("founding x2, y2")
        elif event == cv.EVENT_MOUSEMOVE and check_point1 == True and check_point2 == True and check_draw == True:
            print("Done")
        elif event == cv.EVENT_LBUTTONUP and check_point1 == True and check_point2 == True and check_draw == False:
            cv.line(background, (x1, y1), (x2, y2), (255, 0, 0), 3)
            check_draw = True

    cv.namedWindow("Draw line")
    cv.setMouseCallback("Draw line", draw_a_line)
    while True:
        cv.imshow("Draw line", background)
        if cv.waitKey(1) & 0xff == ord('d'):
            break

    cv.destroyAllWindows()
    print("Done - Task")


draw_line()