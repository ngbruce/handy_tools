import os
from datetime import datetime
import re  # 引入正则表达式模块

# 用途：与SerialRecorder.py配合使用
# 打开相对路径目录 .\SerRec 下的一个文本文件 ，每一行的信息整理成日期时间数据，
# 然后检查是否每一行的日期时间是否前一行的之后，如果不是，则打印一条消息。

# 定义文件路径
file_path = os.path.join('.', 'SerRec', '20250415_012511.txt')

# 打开文件并读取内容
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 初始化上一个日期时间和错误计数器
previous_datetime = None
error_count = 0

# 遍历每一行
for line in lines:
    # 使用正则表达式提取日期时间部分
    match = re.search(r'======(\d{4}-\d{2}-\d{2}, \d{2}:\d{2}:\d{2})', line.strip())
    if match:
        datetime_str = match.group(1)
        # 打印识别到的日期时间
        print(f"\t识别到的日期时间: {datetime_str}")
    else:
        print(f"错误：无法解析日期时间，行内容为：{line.strip()}")
        error_count += 1
        continue
    
    # 将字符串转换为datetime对象
    current_datetime = datetime.strptime(datetime_str, '%Y-%m-%d, %H:%M:%S')
    
    # 检查当前日期时间是否在上一行之后
    if previous_datetime and current_datetime <= previous_datetime:
        print(f"\t\t错误：日期时间 {current_datetime} 不在 {previous_datetime} 之后")
        error_count += 1
    
    # 更新上一个日期时间
    previous_datetime = current_datetime

# 打印错误统计信息
print(f"日期时间顺序检查完成，共发现 {error_count} 处错误。")