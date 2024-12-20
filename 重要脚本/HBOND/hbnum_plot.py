import numpy as np
import matplotlib.pyplot as plt

# 读取 hbnum.xvg 文件
data = np.loadtxt('hbnum.xvg', comments=['@', '#'])

# 提取时间和氢键数量
time = data[:, 0]  # 时间列
hbonds = data[:, 1]  # 氢键数量列

# 确保时间从0开始，并调整横坐标范围
time -= time[0]  # 让时间从0开始
time = np.clip(time, 0, 100000)  # 限制横坐标范围从0到100000

# 绘制图形
plt.figure(figsize=(10, 50))  # 设置图像尺寸，宽10，高50
plt.plot(time, hbonds, label='Number of Hydrogen Bonds', color='b')

# 添加标题和标签
plt.title('Hydrogen Bond Count vs. Time', fontsize=14)
plt.xlabel('Time (ps)', fontsize=12)
plt.ylabel('Number of Hydrogen Bonds', fontsize=12)

# 设置横坐标范围为 [0, 100000]，纵坐标最大值为50
plt.xlim(0, 100000)
plt.ylim(0, 50)  # 设置纵坐标范围从 0 到 50

# 禁用网格
plt.grid(False)

# 显示图例
plt.legend()

# 保存图像
plt.savefig('hbnum_plot.png')

# 显示图形
plt.show()
