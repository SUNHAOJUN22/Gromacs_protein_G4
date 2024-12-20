import numpy as np
import matplotlib.pyplot as plt
import argparse

# 定义读取 .xvg 文件的函数
def read_xvg(filename):
    # 读取文件中的数据，跳过注释行（以 # 或 @ 开头的行）
    data = np.loadtxt(filename, comments=["@", "#"])
    return data

# 主函数
def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='Plot Radius of Gyration (Rg) from GROMACS .xvg file.')
    parser.add_argument('filename', type=str, default='rg.xvg', nargs='?', help='Path to the .xvg file (default is rg.xvg)')
    parser.add_argument('--output', type=str, default='rg_plot.png', help='Output image file name (default is rg_plot.png)')
    args = parser.parse_args()
    
    # 读取 .xvg 文件
    data = read_xvg(args.filename)
    
    # 假设文件的第一列是时间（或步数），第二列是回旋半径（Rg）
    time = data[:, 0]  # 取第一列作为时间
    Rg = data[:, 1]    # 取第二列作为回旋半径
    
    # 绘制图形
    plt.plot(time, Rg, label='Radius of Gyration (Rg)')
    
    # 自动设置横坐标范围（0 到 100000）
    plt.xlim(0, 100000)  # 横坐标从 0 到 100000
    
    # 根据回旋半径的数据动态设置纵坐标范围，增加 0.25 的缓冲区域
    plt.ylim(np.min(Rg) - 0.25, np.max(Rg) + 0.25)  # 设置纵坐标为 Rg 的最小和最大值之间，增加 0.25 的缓冲
    
    # 设置标签和标题
    plt.xlabel('Time (ps)')  # 根据需要修改时间单位
    plt.ylabel('Radius of Gyration (nm)')  # 修改回旋半径的单位为 nm
    plt.title('Radius of Gyration vs Time')
    
    # 去除网格
    plt.grid(False)
    
    # 保存图像
    plt.savefig(args.output, dpi=300, bbox_inches='tight')
    print(f"图像已保存为 {args.output}")
    
    # 显示图形
    plt.show()

if __name__ == "__main__":
    main()
