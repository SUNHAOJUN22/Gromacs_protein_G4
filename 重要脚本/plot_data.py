import numpy as np
import matplotlib.pyplot as plt
import os

# 读取 .xvg 文件的函数
def read_xvg(filename):
    """读取 .xvg 文件的时间和 RMSD 数据"""
    if not os.path.exists(filename):
        print(f"Error: {filename} not found.")
        return [], []
    
    time, rmsd = [], []
    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith(("#", "@")):  # 忽略注释和元信息行
                cols = line.split()
                if len(cols) >= 2:  # Ensure data is valid
                    try:
                        time.append(float(cols[0]))  # 时间
                        rmsd.append(float(cols[1]))  # RMSD 值
                    except ValueError:
                        print(f"Warning: Invalid data at line {file.tell()}")
    print(f"Read {len(time)} data points from {filename}")  # 输出数据点数量
    return time, rmsd

# 绘制回旋半径图 (Rg)
def plot_rg(filename="rg.xvg", output="rg_plot.png"):
    """绘制回旋半径 vs 时间"""
    time, rg = read_xvg(filename)
    if not time or not rg:
        return  # Early exit if the file is empty or invalid
    
    # 自动设置横坐标范围
    time_min, time_max = np.min(time), np.max(time)
    
    # 绘图
    plt.figure(figsize=(10, 6))
    plt.plot(time, rg, label="Radius of Gyration (Rg)", color="black")
    plt.xlabel("Time (ps)")
    plt.ylabel("Radius of Gyration (nm)")
    plt.title("Radius of Gyration vs Time")
    plt.xlim(time_min, time_max)  # 设置横坐标范围为数据的最小值和最大值
    plt.ylim(np.min(rg) - 0.25, np.max(rg) + 0.25)  # 根据 Rg 数据动态设置纵坐标范围
    plt.grid(False)  # 无网格
    plt.legend()
    plt.savefig(output, dpi=1000, bbox_inches='tight')  # 设置DPI为1000
    plt.show()

# 绘制 RMSF 图
def plot_rmsf(filename="rmsf.xvg", output="rmsf_plot.png"):
    """绘制 RMSF"""
    residues, rmsf = read_xvg(filename)
    if not residues or not rmsf:
        return  # Early exit if the file is empty or invalid
    
    # 自动设置横坐标范围
    residues_min, residues_max = np.min(residues), np.max(residues)
    
    # 绘图
    plt.figure(figsize=(10, 6))
    plt.plot(residues, rmsf, label="Protein Backbone RMSF", color="black")
    plt.xlabel("Residue Number")
    plt.ylabel("RMSF (nm)")
    plt.title("RMSF of Protein Backbone")
    plt.xlim(residues_min, residues_max)  # 设置横坐标范围为数据的最小值和最大值
    plt.grid(False)
    plt.legend()
    plt.savefig(output, dpi=1000, bbox_inches='tight')  # 设置DPI为1000
    plt.show()

# 绘制 RMSD 图
def plot_rmsd(filename_protein="rmsd_protein.xvg", filename_dna="rmsd_dna.xvg", output="rmsd_plot.png"):
    """绘制蛋白质和DNA的RMSD"""
    time_protein, rmsd_protein = read_xvg(filename_protein)
    time_dna, rmsd_dna = read_xvg(filename_dna)
    if not time_protein or not rmsd_protein or not time_dna or not rmsd_dna:
        return  # Early exit if any file is empty or invalid
    
    # 强制横坐标从 0 开始
    time_offset = time_protein[0]  # 假设时间列从蛋白质 RMSD 文件获取偏移量
    time_protein = [t - time_offset for t in time_protein]
    time_dna = [t - time_offset for t in time_dna]

    # 自动设置横坐标范围
    time_min = 0  # 横坐标从 0 开始
    time_max = max(np.max(time_protein), np.max(time_dna))  # 获取两个数据集的最大时间

    # 绘图
    plt.figure(figsize=(10, 6))
    plt.plot(time_protein, rmsd_protein, label="Protein Backbone RMSD", color="blue")  # 蓝色线条表示蛋白质
    plt.plot(time_dna, rmsd_dna, label="DNA Backbone RMSD", color="red")  # 红色线条表示DNA
    plt.xlabel("Time (ps)")
    plt.ylabel("RMSD (nm)")
    plt.title("RMSD of Protein and DNA Backbones")
    
    # 设置横坐标范围
    plt.xlim(time_min, time_max)  # 自适应横坐标范围
    
    # 设置纵坐标范围
    plt.ylim(0, 2.0)

    plt.legend()
    plt.grid(False)
    plt.savefig(output, dpi=1000, bbox_inches='tight')  # 设置DPI为1000
    plt.show()

# 主函数，调用三个绘图函数
def main():
    plot_rg(filename="rg.xvg", output="rg_plot.png")  # 回旋半径图
    plot_rmsf(filename="rmsf.xvg", output="rmsf_plot.png")  # RMSF图
    plot_rmsd(filename_protein="rmsd_protein.xvg", filename_dna="rmsd_dna.xvg", output="rmsd_plot.png")  # RMSD图

if __name__ == "__main__":
    main()
