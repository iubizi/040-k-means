###################
# 生成数据
###################

from numpy.random import multivariate_normal as np_mvn
import numpy as np

# 高斯分布
data = np.concatenate( (
    np_mvn( [0, 0], [[2, 0.2], [0.2, 1]], (500,) ),
    np_mvn( [0, 9], [[1, -0.3], [-0.3, 1.5]], (500,) ),
    np_mvn( [12, 0], [[3, 0.5], [0.5, 1]], (500,) ),
    np_mvn( [10, 10], [[1, -0.8], [-0.8, 1]], (500,) ),
    ) )

###################
# 绘图
###################

import matplotlib.pyplot as plt

plt.scatter( [ p[0] for p in data ],
             [ p[1] for p in data ],
             alpha=0.1, marker='.' )

###################
# k-means中心
###################

center = [
    [0, 4],
    [0, 7],
    [6, 4],
    [9, 3],
    ]

k = len(center) # 计算类别
c = [ 'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w' ] # 绘图颜色

# 第一次显示
for i in range(k):
    plt.scatter( center[i][0],
                 center[i][1],
                 c=c[i%len(c)] ) # 避免颜色超了
plt.title('init')
plt.show()

###################
# k-means
###################

counter = 0
print('init\n')
while True:
    
    pool = [ [] for _ in range(k) ]

    for i in data:
        dist = [ np.linalg.norm(center[num] - i) for num in range(k) ]
        
        group = np.argmin(dist)
        pool[group].append(i)

    last_center = [ i for i in center ]

    for i in range(k):
        center[i] = np.mean(pool[i], axis=0)

    for i in range(len(center)): # 收敛即跳出
        flag = 1
        # 只要有一个有区别，那么就说明还不收敛
        if (center[i]-last_center[i]).any(): flag = 0
    if flag: break

    for i in range(k):
        plt.scatter(center[i][0], center[i][1], c=c[i])
        plt.scatter( [p[0] for p in pool[i]],
                     [p[1] for p in pool[i]],
                     alpha=0.1, c=c[i%len(c)], marker='.' )

    counter += 1
    print('turn:', counter)
    plt.title('turn: '+str(counter))
    plt.show()
