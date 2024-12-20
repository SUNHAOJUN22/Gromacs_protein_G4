import numpy as np
import matplotlib.pyplot as plt

# 读取 .xvg 文件，跳过注释行
def read_xvg(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    
    # 只保留数据行，跳过以@和#开头的注释行
    data = []
    for line in lines:
        if not line.startswith(('@', '#')):  # 跳过注释行
            data.append(line.split())  # 按空格分隔数据

    return np.array(data, dtype=float)

# 读取hbang.xvg文件
file_name = 'hbang.xvg'
data = read_xvg(file_name)

# 打印数据的形状和前几行，调试用
print("Data shape:", data.shape)
print("First few rows of data:", data[:5])

# 假设第二列是氢键角度，第三列是密度
if data.shape[1] >= 2:
    angles = data[:, 0]  # 第一列是时间或索引
    density = data[:, 1]  # 第二列是密度或氢键角度分布
else:
    print("Data format is not as expected. Please check the .xvg file.")

# 绘制曲线
plt.figure(figsize=(8, 6))
plt.plot(angles, density, color='skyblue', label='Hydrogen Bond Angle Distribution')

# 设置标题和标签
plt.title('Hydrogen Bond Angle Distribution', fontsize=14)
plt.xlabel('Angle (degrees)', fontsize=12)
plt.ylabel('Density', fontsize=12)

# 设置坐标从0开始
plt.xlim(left=0)  # x轴从0开始
plt.ylim(bottom=0)  # y轴从0开始

# 关闭网格
plt.grid(False)

# 显示图例
plt.legend()

# 保存图像到文件（例如保存为 'hbang_distribution.png'）
output_file = 'hbang_distribution.png'
plt.savefig(output_file, dpi=300)  # 设置dpi为300，确保图像清晰

# 显示图像
plt.show()

print(f"图像已保存为 {output_file}")
