import serial
import datetime
import os

# 用途：打开串口COM4，波特率为115200，打印接收到串口的每一行数据，
# 如果接收到一行的数据的开头是"[rec]"时，记录到文件，文件名为当前路径的相对路径 .\SerRec ，
# 文件名为当前日期时间，格式时txt。


# 打开串口COM4，波特率为115200
ser = serial.Serial('COM4', 115200)

# 获取当前日期时间，并格式化为文件名
current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
file_path = f".\\SerRec\\{current_time}.txt"

# 判断目录是否存在，不存在则创建
os.makedirs(os.path.dirname(file_path), exist_ok=True)

# 创建文件
with open(file_path, 'w') as file:
    pass

try:
    while True:
        # 读取一行数据，并处理解码错误
        line = ser.readline().decode('utf-8', errors='replace').strip()
        
        # 打印接收到的数据
        print(line)
        
        # 如果数据以"[rec]"开头，则写入文件
        if line.startswith("[rec]"):
            with open(file_path, 'a') as file:
                file.write(line + '\n')
except KeyboardInterrupt:
    print("程序终止")
finally:
    ser.close()
    print(f"数据已保存到文件：{file_path}")