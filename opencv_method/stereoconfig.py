"""
:Author:  Vitae
:Create:  2020/7/5 11:51
:Methed: They are zed2's parameters.
Copyright (c) 2020, Vitae Group All Rights Reserved.
"""

import numpy as np
import cv2

# zed双目相机参数
class stereoCamera(object):
    def __init__(self):

        #左相机内参数
        self.cam_matrix_left = np.array([[526.9, 0., 611.875], [0., 526.715, 377.7745], [0., 0., 1.]])
        #右相机内参数
        self.cam_matrix_right = np.array([[529.105, 0., 652.22], [0., 528.705, 359.2085], [0., 0., 1.]])

        #左右相机畸变系数:[k1, k2, p1, p2, k3]
        self.distortion_l = np.array([[-0.0360949, 0.00361507, -6.58687e-05, -0.000454802, -0.00270976]])
        self.distortion_r = np.array([[-0.0439664, 0.0108345, -0.00102937, 0.000156864, -0.00479573]])

        #旋转矩阵
        om = np.array([0.00497864, 0.00958521, -0.00185401])
        self.R = cv2.Rodrigues(om)[0]  # 使用Rodrigues变换将om变换为R
        #平移矩阵
        self.T = np.array([119.575, -0.224, -0.517917])
