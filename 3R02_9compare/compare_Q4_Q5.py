import matplotlib.pyplot as plt

def read_xvg(filename):
    """读取 .xvg 文件的时间和数据"""
    time, data = [], []
    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith(("#", "@")):  # 忽略注释和元信息行
                cols = line.split()
                time.append(float(cols[0]))  # 时间
                data.append(float(cols[1]))  # 数据值
    return time, data

def read_xvg_with_residue(filename):
    """读取 .xvg 文件的残基编号和 RMSF 数据"""
    residues, rmsf = [], []
    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith(("#", "@")):  # 忽略注释和元信息行
                cols = line.split()
                residues.append(int(cols[0]))  # 残基编号
                rmsf.append(float(cols[1]))  # RMSF 值
    return residues, rmsf

def plot_rmsd_comparison(ax, time_4_rmsd_protein, rmsd_4_protein, time_5_rmsd_protein, rmsd_5_protein,
                         time_4_rmsd_dna, rmsd_4_dna, time_5_rmsd_dna, rmsd_5_dna):
    """绘制 RMSD 对比图（蛋白质和 DNA）"""
    ax.plot(time_4_rmsd_protein, rmsd_4_protein, label="3R02-9-Q4 Protein RMSD", color="blue", linewidth=2)
    ax.plot(time_5_rmsd_protein, rmsd_5_protein, label="3R02-9-Q5 Protein RMSD", color="red", linewidth=2)
    ax.plot(time_4_rmsd_dna, rmsd_4_dna, label="3R02-9-Q4 DNA RMSD", color="green", linewidth=2)
    ax.plot(time_5_rmsd_dna, rmsd_5_dna, label="3R02-9-Q5 DNA RMSD", color="orange", linewidth=2)
    ax.set_xlabel("Time (ps)")
    ax.set_ylabel("RMSD (nm)")
    ax.set_title("RMSD Comparison of Protein and DNA for Q4 and Q5")
    ax.legend()
    ax.grid(False)
    ax.set_xlim(0, 10000)
    
    # 设置 RMSD 图的 y 轴范围为 0 到 1，使图的高度为 1
    ax.set_ylim(0, 1)

def plot_rmsf_comparison(ax, residue_4_rmsf, rmsf_4, residue_5_rmsf, rmsf_5):
    """绘制 RMSF 对比图（蛋白质）"""
    ax.plot(residue_4_rmsf, rmsf_4, label="3R02-9-Q4 Protein RMSF", color="blue", linewidth=2)
    ax.plot(residue_5_rmsf, rmsf_5, label="3R02-9-Q5 Protein RMSF", color="red", linewidth=2)
    ax.set_xlabel("Residue Number")
    ax.set_ylabel("RMSF (nm)")
    ax.set_title("RMSF Comparison of Protein Backbone for Q4 and Q5")
    ax.legend()
    ax.grid(False)
    ax.set_xlim(min(residue_4_rmsf), max(residue_4_rmsf))  # 自动设置x轴范围为残基编号的最小值到最大值

def plot_rg_comparison(ax, time_4_rg, rg_4, time_5_rg, rg_5):
    """绘制 Rg 对比图"""
    ax.plot(time_4_rg, rg_4, label="3R02-9-Q4 Rg", color="blue", linewidth=2)
    ax.plot(time_5_rg, rg_5, label="3R02-9-Q5 Rg", color="red", linewidth=2)
    ax.set_xlabel("Time (ps)")
    ax.set_ylabel("Rg (nm)")
    ax.set_title("Rg Comparison for Q4 and Q5")
    ax.legend()
    ax.grid(False)
    ax.set_xlim(0, 10000)

# 主函数，调用绘图函数
def main():
    # 读取 Q4 和 Q5 的 RMSD、RMSF 和 Rg 数据
    # RMSD 数据
    time_4_rmsd_protein, rmsd_4_protein = read_xvg("Q4rmsd_protein.xvg")
    time_5_rmsd_protein, rmsd_5_protein = read_xvg("Q5rmsd_protein.xvg")
    time_4_rmsd_dna, rmsd_4_dna = read_xvg("Q4rmsd_dna.xvg")
    time_5_rmsd_dna, rmsd_5_dna = read_xvg("Q5rmsd_dna.xvg")

    # RMSF 数据（带有残基编号）
    residue_4_rmsf, rmsf_4 = read_xvg_with_residue("Q4rmsf.xvg")
    residue_5_rmsf, rmsf_5 = read_xvg_with_residue("Q5rmsf.xvg")

    # Rg 数据
    time_4_rg, rg_4 = read_xvg("Q4rg.xvg")
    time_5_rg, rg_5 = read_xvg("Q5rg.xvg")

    # 强制横坐标从 0 开始
    time_offset = time_4_rmsd_protein[0]  # 假设时间列从 Q4 Rg 文件获取偏移量
    time_4_rmsd_protein = [t - time_offset for t in time_4_rmsd_protein]
    time_5_rmsd_protein = [t - time_offset for t in time_5_rmsd_protein]
    time_4_rmsd_dna = [t - time_offset for t in time_4_rmsd_dna]
    time_5_rmsd_dna = [t - time_offset for t in time_5_rmsd_dna]
    time_4_rg = [t - time_offset for t in time_4_rg]
    time_5_rg = [t - time_offset for t in time_5_rg]

    # 创建一个 1 行 3 列的子图
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # 调用各个绘图函数，绘制到相应的子图
    plot_rmsd_comparison(axes[0], time_4_rmsd_protein, rmsd_4_protein, time_5_rmsd_protein, rmsd_5_protein,
                         time_4_rmsd_dna, rmsd_4_dna, time_5_rmsd_dna, rmsd_5_dna)
    plot_rmsf_comparison(axes[1], residue_4_rmsf, rmsf_4, residue_5_rmsf, rmsf_5)
    plot_rg_comparison(axes[2], time_4_rg, rg_4, time_5_rg, rg_5)

    # 自动调整子图之间的间距
    plt.tight_layout()

    # 保存整个图像，DPI=1000
    plt.savefig("all_plots.png", dpi=1000, bbox_inches='tight')

    # 显示所有图像
    plt.show()

if __name__ == "__main__":
    main()
