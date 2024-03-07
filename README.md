# Gaussian-fitting-and-trapezoidal-integration-for-riverbed-depth-area-graphs
之前的一次学校作业，求河床水深面积图，已有数据是河床宽度和对应水深高度，现在需要计算，水深面积图。（A previous school assignment required the creation of a riverbed depth-area graph, with given data of river width and corresponding water depths. Now, you need to calculate the water depth-area graph.）
本人是萌新，如果有大佬看到，恳求指点优化
整体思路如下：
已有列表数据，读取数据，画图，为了让结果更精确对数据高斯拟合（方差也可控）
y轴是水深，x轴是河床宽度。采用trapz梯形积分求法：
用i循环遍历y值（可以对积分精度细化），y值-i值=积分对象列表，需要对列表负值替换为0。
之后采用积分，需要注意此时水深为y-i。
