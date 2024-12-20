import matplotlib.pyplot as plt

def read_xvg(filename):
    """读取 .xvg 文件的残基和 RMSF 数据"""
    residues, rmsf = [], []
    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith(("#", "@")):  # 忽略注释和元信息行
                cols = line.split()
                residues.append(int(cols[0]))  # 残基编号
                rmsf.append(float(cols[1]))  # RMSF 值
    return residues, rmsf

# 读取 RMSF 数据
residues, rmsf = read_xvg("rmsf.xvg")

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(residues, rmsf, label="Protein Backbone RMSF", color="black")  # 设置为黑色线条
plt.xlabel("Residue Number")
plt.ylabel("RMSF (nm)")
plt.title("RMSF of Protein Backbone")
plt.legend()
plt.grid(False)
plt.savefig("rmsf_plot.png")  # 保存图片为 PNG 文件
plt.show()
