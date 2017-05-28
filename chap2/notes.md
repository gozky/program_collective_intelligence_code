## notes

1. 根据欧氏距离计算平方差时，值越小代表越相近，为了使得相似度与数值成正比，取其倒数；但倒数有可能为0，所以，最终式子为<img src="https://latex.codecogs.com/gif.latex?\frac{1}{1&plus;\sqrt{diff}}" title="\frac{1}{1+\sqrt{diff}}" />
2. pearson系数，考虑到每个人的打分习惯，修正了某些用户“打分高”的情况，比欧氏距离更通用；代码使用了数学公式展开，原来式子等于**协方差与标准差的商**。