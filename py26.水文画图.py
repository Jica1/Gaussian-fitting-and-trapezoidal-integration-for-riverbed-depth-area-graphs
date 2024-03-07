import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']

# 读取Excel数据
df = pd.read_excel(r"D:\新建文件夹 (7)\shuwien1.xlsx")

# 提取列数据
x = df['宽度'].tolist()
y = df['高度'].tolist()
z = df['河面'].tolist()[0]
x = [x for x in x if x is not None and not pd.isna(x)]
y = [x for x in y if x is not None and not pd.isna(x)]
ddd={}


fig, ax = plt.subplots()
plt.figure(figsize=(12,4),dpi=400)

# 绘制散点图
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.xaxis.set_ticks_position('top')
plt.xticks(range(0, 35, 1))
# 设置标签和标题
ax.set_xlabel('Y')
ax.set_ylabel('X')
ax.set_title('Scatter Plot')
plt.plot(x, y, 'r-', marker='o')
plt.title('河水断面剖面图')
plt.xlabel('宽度/m')
plt.ylabel('高度/m')


# 计算与折线围成的面积#有问题
area = 0
for i in range(len(x)):
    if y[i] >= z :
        if  y[i-1] < z :
            # 当前点在y=3.54以下且前一个点在y=3.54以上，说明折线与y=3.54交叉
            width = 1
            height =  y[i]-z
            area += width * height*0.5
            print(area)
            height = abs(y[i] + y[i + 1] - z * 2)
            area += width * height * 0.5
            ddd[y[i]] = width * height * 0.5
            print(area)
        elif y[i + 1] < z:
            width = 1
            height = y[i] - z
            area += width * height * 0.5
            ddd[y[i]] = width * height * 0.5
            print(area)
        else :
            width = 1
            height =abs(y[i]+y[i+1]-z*2)
            area += width * height*0.5
            average_y = (y[i] + y[i + 1]) / 2
            ddd[average_y] = width * height * 0.5
            print(width*height)
sorted_keys = sorted(ddd.keys())
print("与折线围成的面积：", abs(area),ddd,sorted_keys )

# 绘制填充区域
plt.fill_between(x, y, z, where=[_y >= z for _y in y], color='cadetblue', alpha=0.5)
# 改变y轴正方向
plt.gca().invert_yaxis()
# 添加水平线
plt.axhline(y=z, color='gray', linestyle='--')
plt.show()
count = len(ddd)

print("字典中的元素个数为：", count)
sorted_data = sorted(ddd.items(), key=lambda item: item[1])

# 提取排序后的键和值
keys = [item[0] for item in sorted_data]
values = [item[1] for item in sorted_data]

# 创建柱状图
import matplotlib.pyplot as plt

# 假设有一个字典 data
data = ddd

# 按照键对字典进行排序
sorted_keys = sorted(data.keys())

