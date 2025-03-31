# 给定的字节数组（十进制表示）
byte_values = [229,167,191,230,128,129,230,163,128,230,181,139,232,131,184,231,171,160,0]

# 将十进制值转换为字节对象，并去除末尾的0
bytes_data = bytes(byte_values[:-1])

# 解码为UTF-8字符串
decoded_text = bytes_data.decode('utf-8')

print("解码得到的内容：\n"+decoded_text)
