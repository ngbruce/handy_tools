# 原始文本
text = "姿态检测胸章GZ祺威"

# 转换为UTF-8字节对象（自动处理中文编码）
bytes_data = text.encode('utf-8')

# 转换为十进制数组，并在末尾添加0
byte_array = list(bytes_data) + [0]

# 打印结果
print("UTF-8编码数组：")
print(byte_array)

# 验证解码（可选）
print("\n解码验证：")
print(bytes(byte_array[:-1]).decode('utf-8'))  # 去除末尾0后解码