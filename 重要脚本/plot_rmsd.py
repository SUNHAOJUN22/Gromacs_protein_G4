import matplotlib.pyplot as plt

def read_xvg(filename):
    """读取 .xvg 文件的时间和 RMSD 数据"""
    time, rmsd = [], []
    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith(("#", "@")):  # 忽略注释和元信息行
                cols = line.split()
                time.append(float(cols[0]))  # 时间
                rmsd.append(float(cols[1]))  # RMSD 值
    return time, rmsd

# 读取数据
time_protein, rmsd_protein = read_xvg("rmsd_protein.xvg")
time_dna, rmsd_dna = read_xvg("rmsd_dna.xvg")

# 强制横坐标从 0 开始
time_offset = time_protein[0]  # 假设时间列从蛋白质 RMSD 文件获取偏移量
time_protein = [t - time_offset for t in time_protein]
time_dna = [t - time_offset for t in time_dna]

# 计算时间范围的最大值和最小值（如果需要，可以修改这里的逻辑以适应你需要的时间区间）
time_end = max(max(time_protein), max(time_dna))  # 获取最大的时间点

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(time_protein, rmsd_protein, label="Protein Backbone RMSD", color="blue")  # 蓝色线条表示蛋白质
plt.plot(time_dna, rmsd_dna, label="DNA Backbone RMSD", color="red")  # 红色线条表示DNA
plt.xlabel("Time (ps)")
plt.ylabel("RMSD (nm)")
plt.title("RMSD of Protein and DNA Backbones")

# 设置横坐标范围，确保从0开始，并且最大时间为 time_end
plt.xlim(0, time_end)

# 设置纵坐标范围
plt.ylim(0, 2.0)

plt.legend()
plt.grid(False)
plt.savefig("rmsd_plot.png")  # 保存图片为 PNG 文件
plt.show()
