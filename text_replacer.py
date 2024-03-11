import os

# 用途：用于复制conda环境后更改python.exe的路径
# 检查文本文件(排除的除外)，搜索第一行是否包含特定路径，如果包含，则替换为新的路径
# 检查二进制文件(扩展名在列表的)，搜索是否包含特定路径，如果包含，则用空格覆盖路径，只留下"python.exe"

# 要搜索的路径
path_to_search = 'F:\\Installed_Soft\\Anaconda3\\envs\\new3109qwen\\Scripts'
# 要搜索的字符串
search_string = 'F:\\Installed_Soft\\Anaconda3\\envs\\new3109cc\\python.exe'
# "D:\\Conda_offline\\new3109cc\\python.exe"
# "C:\\Users\\Bruce\\anaconda3\\envs\\new3109cc\\python.exe"
# "F:\\Installed_Soft\\Anaconda3\\envs\\new3109cc\\python.exe"

# 文本搜索，要排除的扩展名，如要排除无扩展名文件，列表中加空字符串 ''
file_type_shebang_exclude = ['.exe', '.dll', '.bin', '.png', '.jpg', '.jpeg', '.gif', '.bmp']
# 要替换的新路径
txt_replace_with = 'F:\\Installed_Soft\\Anaconda3\\envs\\new3109qwen\\python.exe'
# "F:\\Installed_Soft\\Anaconda3\\envs\\new3109cc\\python.exe"
# "D:\\Conda_offline\\new3109cc\\python.exe"

# 要搜索的二进制文件  用空格覆盖python路径，仅保留 "python.exe"
file_type_bin = ['.exe', '.dll', '.bin']
search_string_bytes = search_string.encode('utf-8')
python_exe_bytes = b"python.exe"


# 遍历指定路径下的所有文件
def traverse_and_replace(path_to_search, search_string, file_type_shebang_exclude, txt_replace_with, file_type_bin):
    global cnt_text, cnt_bin
    for root, dirs, files in os.walk(path_to_search):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_extension = os.path.splitext(filename)[1].lower()

            # 处理文本文件或没有扩展名的文件
            if (file_extension not in file_type_shebang_exclude) :
                try:
                    with open(file_path, 'r+', encoding='utf-8', errors='ignore') as f:
                        # 读取文件的第一行
                        first_line = f.readline()
                        # 检查第一行是否以 "#!" 开头，并且包含 search_string
                        if first_line.startswith('#!') and search_string in first_line:
                            # 替换 search_string 为 txt_replace_with
                            new_first_line = first_line.replace(search_string, txt_replace_with)
                            # 写入新的第一行到临时变量
                            new_content = new_first_line
                            # 读取文件的剩余部分
                            remaining = f.read()
                            # 将剩余内容追加到新的第一行后面
                            new_content += remaining
                            # 将文件指针移回文件的开始
                            f.seek(0)
                            # 写入整个新内容（新的第一行加上剩余内容）
                            f.write(new_content)
                            print(f"(text) Replaced in {file_path}")
                            cnt_text += 1
                except IOError as e:
                    print(f"Error reading or writing {file_path}: {e}")

            # 处理二进制文件
            elif file_extension in file_type_bin:
                try:
                    with open(file_path, 'rb+') as f:
                        content = f.read()
                        # 查找 search_string_bytes 的位置
                        search_pos = content.find(search_string_bytes)
                        if search_pos != -1:
                            # 查找 python_exe_bytes 的位置
                            python_exe_pos = content.find(python_exe_bytes, search_pos)
                            if python_exe_pos != -1:
                                # 确定要替换的部分的长度
                                replace_length = python_exe_pos - search_pos
                                # 创建替换后的内容，用空格替换掉部分字符串
                                # 注意这里使用 b' ' * replace_length 来创建相应长度的空格字节串
                                new_content = content[:search_pos] + b' ' * replace_length + content[python_exe_pos:]
                                # 检查新内容是否比原始内容短
                                if len(new_content) < len(content):  # 文件字节数，应该相等的
                                    # 写入替换后的内容
                                    f.seek(0)
                                    f.write(new_content)
                                    # 截断文件以去除多余的内容
                                    print("警告！截断文件, new len = ", len(new_content), " old len = ", len(content))
                                    f.truncate()
                                else:
                                    # 直接从文件开头位置写入替换内容
                                    f.seek(0)
                                    f.write(new_content)
                                print(f"(bin) Replaced in {file_path}")
                                cnt_bin += 1
                except IOError as e:
                    print(f"Error reading or writing binary file {file_path}: {e}")


# 开始执行程序
cnt_text = 0
cnt_bin = 0
traverse_and_replace(path_to_search, search_string, file_type_shebang_exclude, txt_replace_with, file_type_bin)
print("总替换数量：", cnt_text + cnt_bin, "  / 文本文件：", cnt_text, "  / 二进制文件：", cnt_bin)
print("替换完成！")
