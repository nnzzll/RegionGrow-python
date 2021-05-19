import numpy as np

def RegionGrow(image: np.ndarray, seed: tuple, threshold: float, max_val: float, connectivity: bool = True):
    '''区域生长算法

    args:
        image:输入图片,(Height,Width)的numpy数组
        seed:种子点
        threshold:判断生长的阈值
        max_val:目标区域的最大灰度
        connectivity:连通方式,
            True:8连通
            False:4连通
    '''
    if connectivity:
        connects = [[-1, 1], [0, -1], [1, -1],
                    [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]
    else:
        connects = [[0, -1], [1, 0], [0, 1], [-1, 0]]

    height, width = image.shape
    result = np.zeros(image.shape)
    seedList = [seed] # 存储种子点的堆栈
    while(seedList):
        currentPoint = seedList.pop(0) # 当前种子点出栈
        result[currentPoint[1], currentPoint[0]] = 1
        for i in range(len(connects)):
            new_x = currentPoint[0]+connects[i][0]
            new_y = currentPoint[1]+connects[i][1]
            if new_x < 0 or new_y < 0 or new_x >= width or new_y >= height:
                continue
            # 计算种子点与领域点的灰度差
            diff = abs(image[new_y,new_x]-image[currentPoint[1],currentPoint[0]])
            # 生长条件:种子点与领域点的差小于阈值,且领域点未被标记,且当前点的灰度值小于目标区域的最大灰度值
            if diff<threshold and result[new_y,new_x]==0 and image[new_y,new_x]<=max_val:
                result[new_y,new_x] = 1
                seedList.append((new_x,new_y))
    return result