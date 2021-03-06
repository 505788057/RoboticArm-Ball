import cv2
import numpy as np
import pyzed.sl as sl
import time
import imutils


def load_image_into_numpy_array(image):
    ar = image.get_data()
    ar = ar[:, :, 0:3]
    (im_height, im_width, channels) = image.get_data().shape
    return np.array(ar).reshape((im_height, im_width, 3)).astype(np.uint8)


width = 2560
height = 720

image_np_global = np.zeros([width, height, 3], dtype=np.uint8)

zed = sl.Camera()
input_type = sl.InputType()
init_params = sl.InitParameters(input_t=input_type)
init_params.camera_resolution = sl.RESOLUTION.HD720
init_params.camera_fps = 60
init_params.svo_real_time_mode = True

err = zed.open(init_params)
print(err)
while err != sl.ERROR_CODE.SUCCESS:
    err = zed.open(init_params)
    print(err)
    time.sleep(1)

image_mat = sl.Mat()
runtime_parameters = sl.RuntimeParameters()
image_size = sl.Resolution(width, height)

while (True):

    if zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:
        zed.retrieve_image(image_mat, sl.VIEW.SIDE_BY_SIDE, resolution=image_size)
        image_np_global = load_image_into_numpy_array(image_mat)

    LeftImage = image_np_global[0:720, 0:1280]
    RightImage = image_np_global[0:720, 1280:2560]
    Leftblurred = cv2.GaussianBlur(LeftImage, (11, 11), 0)
    Rightblurred = cv2.GaussianBlur(RightImage, (11, 11), 0)
    Lefthsv = cv2.cvtColor(Leftblurred, cv2.COLOR_BGR2HSV)
    Righthsv = cv2.cvtColor(Rightblurred, cv2.COLOR_BGR2HSV)

    greenLower = (29, 86, 6)
    greenUpper = (64, 255, 255)

    Leftmask = cv2.inRange(Lefthsv, greenLower, greenUpper)
    Rightmask = cv2.inRange(Righthsv, greenLower, greenUpper)
    Leftmask = cv2.erode(Leftmask, None, iterations=2)
    Rightmask = cv2.erode(Rightmask, None, iterations=2)
    Leftmask = cv2.dilate(Leftmask, None, iterations=2)
    Rightmask = cv2.dilate(Rightmask, None, iterations=2)

    Lcnts = cv2.findContours(Leftmask.copy(), cv2.RETR_EXTERNAL,
                             cv2.CHAIN_APPROX_SIMPLE)
    Lcnts = imutils.grab_contours(Lcnts)
    Rcnts = cv2.findContours(Rightmask.copy(), cv2.RETR_EXTERNAL,
                             cv2.CHAIN_APPROX_SIMPLE)
    Rcnts = imutils.grab_contours(Rcnts)

    Lcenter = None
    Rcenter = None
    # only proceed if at least one contour was found
    if len(Lcnts) > 0 and len(Rcnts) > 0:
        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid
        Lc = max(Lcnts, key=cv2.contourArea)
        Rc = max(Rcnts, key=cv2.contourArea)
        ((Lx, Ly), Lradius) = cv2.minEnclosingCircle(Lc)
        ((Rx, Ry), Rradius) = cv2.minEnclosingCircle(Rc)

        LM = cv2.moments(Lc)
        RM = cv2.moments(Rc)

        Lcenter = (int(LM["m10"] / LM["m00"]), int(LM["m01"] / LM["m00"]))
        Rcenter = (int(RM["m10"] / RM["m00"]), int(RM["m01"] / RM["m00"]))
        # only proceed if the radius meets a minimum size
        if Lradius > 10 and Rradius > 10:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            cv2.circle(LeftImage, (int(Lx), int(Ly)), int(Lradius),
                       (0, 255, 255), 2)
            cv2.circle(LeftImage, Lcenter, 5, (0, 0, 255), -1)
            cv2.circle(RightImage, (int(Rx), int(Ry)), int(Rradius),
                       (0, 255, 255), 2)
            cv2.circle(RightImage, Rcenter, 5, (0, 0, 255), -1)

    cv2.imshow('LeftImage', LeftImage)
    cv2.imshow('RightImage', RightImage)
    if cv2.waitKey(1) == ord('q'):
        break

print('succeed.')
