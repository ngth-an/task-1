import cv2 as cv
import numpy as np

check_draw = False

xx, yy = -1, -1
background = np.zeros((455, 455, 3))


def draw_circle(background=background, radius=100):
    def draw_a_circle(event, x, y, flags, param):

        global check_draw, xx, yy

        if event == cv.EVENT_LBUTTONDOWN and check_draw == False:
            xx, yy = x, y
            check_draw = True
        elif event == cv.EVENT_MOUSEMOVE and check_draw == False:
            print("founding")
            print(x, y)
        elif event == cv.EVENT_MOUSEMOVE and check_draw == True:
            print("Done")
        elif event == cv.EVENT_LBUTTONUP and check_draw == True:
            cv.circle(background, (xx, yy), radius, (255, 0, 0), -1)

    cv.namedWindow("Draw")
    cv.setMouseCallback("Draw", draw_a_circle)
    while True:
        cv.imshow("Draw", background)
        if cv.waitKey(1) & 0xff == ord('d'):
            break

    cv.destroyAllWindows()
    print("Done - Task")


draw_circle()