# 040-k-means

040 k-means

Use your own function to implement k-means, the official function:

```
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2, random_state=0).fit(data)

kmeans.labels_ # 每个点类别
kmeans.predict([[0, 0], [12, 3]]) # 测试集
kmeans.cluster_centers_ # 收敛中心
```
