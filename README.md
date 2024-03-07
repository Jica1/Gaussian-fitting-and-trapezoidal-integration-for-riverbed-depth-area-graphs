# Gaussian-fitting-and-trapezoidal-integration-for-riverbed-depth-area-graphs
For a past school project, I was tasked with creating a graph illustrating the relationship between water depth and the cross-sectional area of a riverbed. The provided data included measurements of riverbed width and corresponding water depths. My current objective is to compute the depth-area graph based on this existing data. Being new to this, I would greatly appreciate any guidance or optimization tips from experienced individuals.

Here's my overall approach:

I have a list of collected data, so I will start by reading this data and plotting it. To enhance the accuracy of my results, I plan to fit the data using a Gaussian function, which also allows me to control the variance.
On the graph, the y-axis will represent the water depth, and the x-axis will represent the riverbed width. I intend to use the trapezoidal rule for numerical integration:
I will loop through the y values (which can be adjusted for integration precision), and for each y value, I will subtract the corresponding i value to obtain the list of intervals for integration. If there are any negative values in the list, I will replace them with zeros.
When performing the integration, it's crucial to remember that the actual depth value is y minus i.
Advantages of my code include:

It can be directly applied to similar tasks involving graphical representation and integration.
It ensures high precision in the calculated results.
It allows for the customization of the integration width, providing flexibility in the level of detail for the graph.
中文版：
之前的一次学校作业，求河床水深面积图，已有数据是河床宽度和对应水深高度，现在需要计算，水深面积图。
本人是萌新，如果有大佬看到，恳求指点优化
一、整体思路如下：
已有列表数据，读取数据，画图，为了让结果更精确对数据高斯拟合（方差也可控）
y轴是水深，x轴是河床宽度。采用trapz梯形积分求法：
用i循环遍历y值（可以对积分精度细化），y值-i值=积分对象列表，需要对列表负值替换为0。
之后采用积分，需要注意此时水深为y-i。
二、代码优势：
1、可以直接拿去用来做类似的图形求积分。
2、精度高
3、可以设置积分宽度
