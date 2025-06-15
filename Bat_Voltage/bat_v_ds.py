import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 全局变量定义
DATA_FILE_PATH = "./batch_earlier/bat_rec_4.txt"  # 数据文件路径
SMOOTHING_WINDOW = 5  # 平滑化窗口大小，可调整
NUM_Intervals = 20  # 划分区间数量

# 设置中文字体，避免中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'WenQuanYi Zen Hei']  # 常用中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题


def read_file(file_path):
    """读取数据文件并处理成列表"""
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:  # 忽略空行
                parts = line.split(',')
                if len(parts) == 2:
                    try:
                        voltage = int(parts[1].strip())
                        data.append(voltage)
                    except ValueError:
                        continue
    return data


def split_into_intervals(data, num_intervals=NUM_Intervals):
    """将电压数据分成指定数量NUM_Intervals 的区间"""
    # 使用linspace生成精确的等分索引（包含首尾）
    interval_indices = np.linspace(0, len(data)-1, num=num_intervals+1, dtype=int)
    # 返回前的反转操作
    # return [data[i] for i in interval_indices]
    temp = [data[i] for i in interval_indices]
    return temp[::-1]  # 反转列表，让数值最小的区间先出现


def smooth_data(data, window_size):
    """平滑化处理数据"""
    smoothed = []
    half_window = window_size // 2

    for i in range(len(data)):
        # 确定窗口边界
        start = max(0, i - half_window)
        end = min(len(data), i + half_window + 1)

        # 计算平均值
        window = data[start:end]
        avg = sum(window) / len(window)
        smoothed.append(avg)

    return smoothed


def main():
    # 1. 读取文件数据
    voltage_data = read_file(DATA_FILE_PATH)
    print("原始电压数据:", voltage_data[:10], "...")  # 只打印前10个作为示例

    # 2. 平滑化处理 (顺序调整到分割区间之前)
    smoothed_data = smooth_data(voltage_data, SMOOTHING_WINDOW)
    print("\n平滑化后的数据:", smoothed_data[:10], "...")

    # 3. 分割电压区间 (现在基于平滑化后的数据)
    intervals = split_into_intervals(smoothed_data)
    print("\n电压区间 (" + str(NUM_Intervals) + " 等分):")
    for i, v in enumerate(intervals):
        print(f"区间{i + 1}: {v:.2f} mV")

    print("\n原始数据条目数:", len(voltage_data))
    # 4. JavaScript格式打印区间数据(转换为伏特，基于平滑化数据)
    print("\nJavaScript格式区间数据:")
    print("[")
    for i, v in enumerate(intervals):
        x_val = i * (100/NUM_Intervals)  # 修正变量名NUM_Intervals -> num_intervals
        y_val = v / 1000
        print(f"    [{(x_val):.1f}, {y_val:.2f}],")
    print("]")

    # 5. 绘制曲线图
    fig, ax = plt.subplots(figsize=(10, 5))
    line_original, = ax.plot(voltage_data, label='原始数据', color='blue', alpha=0.5)
    line_smoothed, = ax.plot(smoothed_data, label='平滑数据', color='red', linewidth=2)

    # 设置X轴刻度为数据量的 NUM_Intervals 间隔
    num_intervals = NUM_Intervals
    interval_size = len(voltage_data) // num_intervals
    xticks = [i * interval_size for i in range(num_intervals + 1+1+2)]
    ax.set_xticks(xticks)

    # 添加标注
    annot = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                        bbox=dict(boxstyle="round", fc="w"),
                        arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)

    def update_annot(ind):
        x, y = line_smoothed.get_data()
        annot.xy = (x[ind["ind"][0]], y[ind["ind"][0]])
        text = f"X: {x[ind['ind'][0]]:.0f}\nY: {y[ind['ind'][0]]:.2f} mV"
        annot.set_text(text)
        annot.get_bbox_patch().set_alpha(0.4)

    def hover(event):
        vis = annot.get_visible()
        if event.inaxes == ax:
            cont, ind = line_smoothed.contains(event)
            if cont:
                update_annot(ind)
                annot.set_visible(True)
                fig.canvas.draw_idle()
            else:
                if vis:
                    annot.set_visible(False)
                    fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", hover)

    ax.set_title('电池放电电压曲线', fontproperties='SimHei')
    ax.set_xlabel('测试序号', fontproperties='SimHei')
    ax.set_ylabel('电压(mV)', fontproperties='SimHei')
    ax.legend(prop={'family': 'SimHei'})
    ax.grid(True)
    plt.show()


if __name__ == "__main__":
    main()