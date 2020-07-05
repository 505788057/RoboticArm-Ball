"""
:Author:  Vitae
:Create:  2020/7/5 11:22
:Methed: The positon of the Robot arm and zed2 are always moving. The Transfer matrix and Rotation matrix are changing.
        so this script can calculate the TR matrix by three sets of points.
Copyright (c) 2020, Vitae Group All Rights Reserved.
"""

import numpy as np
import os


def fetch_arguments():
    zed_x1 = input(
        "Please input three sets of data which scan from the ZED2 and KUKA.\nNOTE: The unit entered is mm.\n\nzed_x1:")
    zed_y1 = input('zed_y1:')
    zed_z1 = input('zed_z1:')

    kuka_x1 = input("\nkuka_x1:")
    kuka_y1 = input('kuka_y1:')
    kuka_z1 = input('kuka_z1:')

    zed_x2 = input("\nzed_x2:")
    zed_y2 = input('zed_y2:')
    zed_z2 = input('zed_z2:')

    kuka_x2 = input("\nkuka_x2:")
    kuka_y2 = input('kuka_y2:')
    kuka_z2 = input('kuka_z2:')

    zed_x3 = input("\nzed_x3:")
    zed_y3 = input('zed_y3:')
    zed_z3 = input('zed_z3:')

    kuka_x3 = input("\nkuka_x3:")
    kuka_y3 = input('kuka_y3:')
    kuka_z3 = input('kuka_z3:')

    zed_x1, zed_y1, zed_z1 = float(zed_x1), float(zed_y1), float(zed_z1)
    zed_x2, zed_y2, zed_z2 = float(zed_x2), float(zed_y2), float(zed_z2)
    zed_x3, zed_y3, zed_z3 = float(zed_x3), float(zed_y3), float(zed_z3)

    kuka_x1, kuka_y1, kuka_z1 = float(kuka_x1), float(kuka_y1), float(kuka_z1)
    kuka_x2, kuka_y2, kuka_z2 = float(kuka_x2), float(kuka_y2), float(kuka_z2)
    kuka_x3, kuka_y3, kuka_z3 = float(kuka_x3), float(kuka_y3), float(kuka_z3)

    zedPoints = np.array(([zed_x1, zed_x2, zed_x3], [zed_y1, zed_y2, zed_y3], [zed_z1, zed_z2, zed_z3]))
    kukaPoints = np.array(([kuka_x1, kuka_x2, kuka_x3], [kuka_y1, kuka_y2, kuka_y3], [kuka_z1, kuka_z2, kuka_z3]))

    print('The zed2 matrix is :\n', zedPoints, '\n The kuka matrix is:\n', kukaPoints)

    ContinueFlag = False
    while (not ContinueFlag):
        judgeFlag = input('Do you want to continue?(y/n)  :')
        if judgeFlag == 'y':
            ContinueFlag = True

        elif judgeFlag == 'n':
            os._exit(0)

        else:
            pass
    return zedPoints, kukaPoints


if __name__ == '__main__':
    fetch_arguments()
