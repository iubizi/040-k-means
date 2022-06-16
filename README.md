# 040-k-means

040 k-means

Use my own function to implement k-means, the official function:

```
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2, random_state=0).fit(data)

kmeans.labels_ # 每个点类别
kmeans.predict([[0, 0], [12, 3]]) # 测试集
kmeans.cluster_centers_ # 收敛中心
```

## result
![init](https://github.com/iubizi/040-k-means/blob/main/0.PNG)
![1](https://github.com/iubizi/040-k-means/blob/main/1.PNG)
![2](https://github.com/iubizi/040-k-means/blob/main/2.PNG)
![3](https://github.com/iubizi/040-k-means/blob/main/3.PNG)
