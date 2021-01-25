import numpy as np


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y


def regionGrow(image: np.ndarray, seed: Point, threshold: float = 0.5, label: int = 1, connectivity=True):
    '''
    image:输入图片,(Height,Width)的numpy数组
    seed:种子点
    threshold:判断生长的阈值
    label:生长区域的标签
    connectivity:连通方式,
        True:8连通
        False:4连通
    '''
    if connectivity:
        connects = [Point(-1, -1), Point(0, -1), Point(1, -1), Point(1, 0), Point(1, 1),
                    Point(0, 1), Point(-1, 1), Point(-1, 0)]
    else:
        connects = [Point(0, -1),  Point(1, 0), Point(0, 1), Point(-1, 0)]

    height, width = image.shape
    result = np.zeros(image.shape)
    seedList = [] #存储种子点的堆栈
    seedList.append(seed)
    while(len(seedList) > 0):
        currentPoint = seedList.pop(0) # 当前种子点出栈
        result[currentPoint.x, currentPoint.y] = label
        for i in range(len(connects)):
            tempX = currentPoint.x + connects[i].x
            tempY = currentPoint.y + connects[i].y
            if tempX < 0 or tempY < 0 or tempX >= height or tempY >= width:
                continue
            # 计算种子点与领域点的灰度差
            diff = abs(image[currentPoint.x, currentPoint.y] - image[tempX, tempY])
            # 生长条件:种子点与领域点的差小于阈值,且领域点未被标记
            if diff < threshold and result[tempX, tempY] == 0:
                result[tempX, tempY] = label
                seedList.append(Point(tempX,tempY)) #将领域点作为新的生长种子点,入栈
    return result