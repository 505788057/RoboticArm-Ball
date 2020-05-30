import numpy as np
import parserTR
'''
This program show the how to calculate the transfer and rotation matrix between the two sets of point.
'''

def Get3DR_TransMatrix(srcPoints, dstPoints):
    srcSumX = 0.0
    srcSumY = 0.0
    srcSumZ = 0.0

    dstSumX = 0.0
    dstSumY = 0.0
    dstSumZ = 0.0

    for i in range(0, 3):
        srcSumX = srcSumX + srcPoints[0][i]
        srcSumY = srcSumY + srcPoints[1][i]
        srcSumZ = srcSumZ + srcPoints[2][i]
        dstSumX = dstSumX + dstPoints[0][i]
        dstSumY = dstSumY + dstPoints[1][i]
        dstSumZ = dstSumZ + dstPoints[2][i]

    centerSrcx = srcSumX / 3.
    centerSrcy = srcSumY / 3.
    centerSrcz = srcSumZ / 3.
    centerDstx = dstSumX / 3.
    centerDsty = dstSumY / 3.
    centerDstz = dstSumZ / 3.

    # create a blank matrix
    srcMat = np.zeros((3, 3))
    dstMat = np.zeros((3, 3))

    for i in range(0, 3):
        srcMat[0][i] = srcPoints[0][i] - centerSrcx
        srcMat[1][i] = srcPoints[1][i] - centerSrcy
        srcMat[2][i] = srcPoints[2][i] - centerSrcz

        dstMat[0][i] = dstPoints[0][i] - centerDstx
        dstMat[1][i] = dstPoints[1][i] - centerDsty
        dstMat[2][i] = dstPoints[2][i] - centerDstz

    # matS = srcMat * dstMat.t(); 转置
    matS = np.dot(srcMat, np.transpose(dstMat))

    matU, s, matV = np.linalg.svd(matS)

    # matTemp = matU * matV
    matTemp = np.dot(matU, matV)
    det = np.linalg.det(matTemp)
    matM = np.array(([1, 0, 0], [0, 1, 0], [0, 0, det]))

    matRa = np.dot(np.transpose(matV), matM)
    matR = np.dot(matRa, np.transpose(matU))

    delta_X = centerDstx - (
            np.dot(centerSrcx, matR[0][0]) + np.dot(centerSrcy, matR[0][1]) + np.dot(centerSrcz, matR[0][2]))
    delta_Y = centerDsty - (
            np.dot(centerSrcx, matR[1][0]) + np.dot(centerSrcy, matR[1][1]) + np.dot(centerSrcz, matR[1][2]))
    delta_Z = centerDstz - (
            np.dot(centerSrcx, matR[2][0]) + np.dot(centerSrcy, matR[2][1]) + np.dot(centerSrcz, matR[2][2]))

    TraMatrix = np.array(([delta_X], [delta_Y], [delta_Z]))
    addzeroone = np.array(([0., 0., 0., 1.]))

    temR_T = np.hstack((matR, TraMatrix))
    R_T = np.vstack((temR_T, addzeroone))

    return matR, TraMatrix, R_T


zedPoints = np.array(([-49., 149., 595.], [-60, -336, -143], [901, 1024, 968]))
kukaPoints = np.array(([726.46, 732.03, 547.54], [929.69, 696.64, 306.93], [161.81, 457.81, 255.92]))
# zedPoints = np.array(([100., 0., 0.], [0., 100., 0.], [0., 0., 100.]))
# kukaPoints = np.array(([50., -50., 50.], [100., 0., 0.], [0., 0., 100.]))
# zedPoints, kukaPoints= parserTR.fetch_arguments()

test = np.array(([127.], [-487.], [1372.]))
rotation_matrix, transfer_matrix, c = Get3DR_TransMatrix(zedPoints, kukaPoints)

print(np.dot(rotation_matrix, test) + transfer_matrix)
