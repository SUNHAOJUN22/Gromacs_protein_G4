import numpy as np
import matplotlib.pyplot as plt
import os

# 绘制图形的函数
def plot_xvg_subplot(ax, file_name, xlabel, ylabel, title, color, xlim_max=None, ylim_max=None):
    try:
        # Check if the file exists
        if not os.path.exists(file_name):
            print(f"File {file_name} does not exist.")
            return
        
        # 读取 .xvg 文件，跳过注释行
        data = np.loadtxt(file_name, comments=['@', '#'])
        
        # 确定列数，调整数据
        if data.shape[1] >= 2:
            x_data = data[:, 0]  # 第一列
            y_data = data[:, 1]  # 第二列
        elif data.shape[1] >= 3:
            x_data = data[:, 0]  # 第一列
            y_data = data[:, 2]  # 第三列
        else:
            print(f"Data format error in {file_name}.")
            return
        
        # 调整横坐标范围，让时间从0开始
        x_data -= x_data[0]
        
        # 如果提供了 xlim_max，限制横坐标范围
        if xlim_max is not None:
            x_data = np.clip(x_data, 0, xlim_max)  # 限制横坐标范围

        # 在子图上绘制
        ax.plot(x_data, y_data, label=title, color=color)
        
        # 添加标题和标签
        ax.set_title(title, fontsize=10)
        ax.set_xlabel(xlabel, fontsize=8)
        ax.set_ylabel(ylabel, fontsize=8)
        
        # 设置横坐标范围，确保从0开始
        ax.set_xlim(0, np.max(x_data))  # 横坐标从0开始，并自动适应数据最大值
        if ylim_max is not None:
            ax.set_ylim(0, ylim_max)  # 设置纵坐标最大值
        
        # 禁用网格
        ax.grid(False)
        
        # 显示图例
        ax.legend()

    except Exception as e:
        print(f"Error processing file {file_name}: {e}")

# 文件和图像设置
files = [
    {'file': 'hbnum.xvg', 'xlabel': 'Time (ps)', 'ylabel': 'Number of Hydrogen Bonds', 'title': 'Hydrogen Bond Count vs. Time', 'color': 'b', 'xlim_max': None, 'ylim_max': 30},
    {'file': 'hbdist.xvg', 'xlabel': 'Distance (nm)', 'ylabel': 'Density', 'title': 'Hydrogen Bond Distance Distribution', 'color': 'r', 'xlim_max': None, 'ylim_max': None},
    {'file': 'hblife.xvg', 'xlabel': 'Lifetime (ps)', 'ylabel': 'Density', 'title': 'Hydrogen Bond Lifetime Distribution', 'color': 'g', 'xlim_max': None, 'ylim_max': None},
    {'file': 'nhbdist.xvg', 'xlabel': 'Distance (nm)', 'ylabel': 'Density', 'title': 'Neighbor Hydrogen Bond Distance Distribution', 'color': 'y', 'xlim_max': None, 'ylim_max': None},
    {'file': 'hbang.xvg', 'xlabel': 'Angle (degrees)', 'ylabel': 'Density', 'title': 'Hydrogen Bond Angle Distribution', 'color': 'c', 'xlim_max': None, 'ylim_max': None},
]

# 创建 2x3 的子图布局（2行3列）
fig, axs = plt.subplots(3, 2, figsize=(15, 12))

# 删除多余的子图（只有5个图形，因此需要删除一个）
fig.delaxes(axs[2, 1])

# 生成所有图形并将它们绘制在子图上
for i, file_info in enumerate(files):
    row = i // 2  # 计算子图的行
    col = i % 2   # 计算子图的列
    plot_xvg_subplot(axs[row, col], file_info['file'], file_info['xlabel'], file_info['ylabel'], file_info['title'], file_info['color'], file_info['xlim_max'], file_info['ylim_max'])

# 调整子图间距
plt.tight_layout()

# 保存整个图像
plt.savefig('combined_plots.png', dpi=1000, bbox_inches='tight')

# 显示图形
plt.show()
