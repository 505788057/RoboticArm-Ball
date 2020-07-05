
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D


def list2array(listx, listy, listz, timelist):
    timelistcali = timelist.copy()
    timecali = np.array(timelistcali)
    time = np.array(timelist[10:20])
    lasttime = np.array(timelistcali[20:])

    x = np.array(listx[10:20])
    y = np.array(listy[10:20])
    y_l = np.array(listy[20:])
    z = np.array(listz[10:20])

    tem_time = timelist[0] % 10000
    minus_time = timelist[0] - tem_time

    # Least squares
    Least_x = np.polyfit(time - minus_time, x, 1)
    equation_x = np.poly1d(Least_x)
    Least_z = np.polyfit(time - minus_time, z, 1)
    equation_z = np.poly1d(Least_z)
    Least_y = np.polyfit(time - minus_time, y, 2)
    equation_y = np.poly1d(Least_y)
    print(equation_x)
    print(equation_y)
    print(equation_z)

    # or use yvals=np.polyval(z1,x)
    fit_x = equation_x(time - minus_time)
    fit_z = equation_z(time - minus_time)
    # fit_y = equation_y(time - minus_time)
    fit_y = equation_y(timecali - minus_time)

    # # 2D
    plot1 = plt.plot(time - minus_time, z, '*', label='original values')
    plot2 = plt.plot(time - minus_time, fit_z, 'r', label='polyfit values')
    # plot2 = plt.plot(timecali - minus_time, fit_y, 'r', label='polyfit values')
    # plot3 = plt.plot(lasttime - minus_time,y_l,'*', label='cali values')

    plt.xlabel('time axis')
    plt.ylabel('position axis')
    plt.legend(loc=1)  # 指定legend的位置,读者可以自己help它的用法
    plt.title('polyfitting')
    # plt.show()
    plt.savefig('test1.png')

    print('Calidation Fished.')

    # 3D
    # mpl.rcParams['legend.fontsize'] = 10
    # fig = plt.figure()
    # ax = fig.gca(projection='3d')
    # ax.plot(x, z, y, label='parametric curve')
    # ax.plot(fit_x, fit_z, fit_y, label='parametric curve')
    #
    # ax.set_ylabel('Z')
    # ax.set_zlabel('Y')
    # ax.set_xlabel('X')
    # ax.legend()
    # plt.show()


if __name__ == '__main__':
    # listx = [530.503, 441.775, 359.437, 387.658, 346.852, 379.405, 359.437, 387.658, 367.056, 339.555, 296.515, 203.365,
    #          156.585, 110.929, 80.253, 31.548, 8.76, -26.513, -88.382, -112.684, -168.117, -199.791, -272.723, -289.129,
    #          -340.819]
    #
    # listy = [634.055, 562.273, 486.082, 557.337, 511.259, 566.238, 542.73, 634.72, 629.543, 513.086, 328.724, -97.621,
    #          -295.208, -371.538, -459.652, -596.961, -592.906, -597.09, -549.353, -513.193, -360.881, -280.195, 18.388,
    #          145.981, 420.237]
    #
    # listz = [4499.35, 3936.931, 3315.31, 3705.347, 3315.31, 3499.494, 3315.31, 3705.347, 3936.931, 3499.494, 3315.31,
    #          2738.735, 2738.735, 2422.727, 2332.996, 2332.996, 2172.1, 2031.964, 1799.74, 1702.457, 1431.611, 1369.367,
    #          1049.848, 912.912, 715.806]
    #
    # timelist = [1592279019.6114244, 1592279019.6666343, 1592279019.7271214, 1592279019.7855422, 1592279019.8470416,
    #             1592279019.899831, 1592279019.960042, 1592279020.0147157, 1592279020.073564, 1592279020.1297188,
    #             1592279020.251368, 1592279020.3160286, 1592279020.3703296, 1592279020.425001, 1592279020.486829,
    #             1592279020.5405035, 1592279020.594173, 1592279020.6514804, 1592279020.7062948, 1592279020.7669036,
    #             1592279020.824749, 1592279020.8770735, 1592279020.9478786, 1592279021.0041757, 1592279021.0599868]
    listx = [75.985, 1476.443, 1354.1, 1253.719, 909.78, 871.114, 831.249, 533.148, 433.731, 216.874, 66.593, -43.015,
             -247.671, -432.53, -540.066, -713.143, -1454.109]
    listy = [5.812, -203.385, -293.354, -468.88, -454.001, -587.458, -645.07, -580.712, -573.783, -506.565, -455.605,
             -401.38, -229.635, -98.121, 37.474, 298.941, 776.486]
    listz = [61.726, 1679.757, 1630.335, 1711.781, 1373.599, 1545.638, 1627.44, 1359.287, 1332.387, 1226.683, 1225.768,
             1207.539, 1067.879, 1070.581, 1000.652, 834.316, 1396.787]

    list2array(listx, listy, listz, timelist)
