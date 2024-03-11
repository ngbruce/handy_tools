import os
# 目前初步看ok，二进制部分不知会否误删内容
# 给定的变量
path_to_search = 'D:\\Conda_offline\\test\\sub folder'
search_string = "C:\\Users\\Bruce\\anaconda3\\envs\\new3109cc\\python.exe"
# "D:\\Conda_offline\\new3109cc\\python.exe"
# "C:\\Users\\Bruce\\anaconda3\\envs\\new3109cc\\python.exe"
# "F:\\Installed_Soft\\Anaconda3\\envs\\new3109cc\\python.exe"
file_type_shebang = ['.py', '.txt']
txt_replace_with = "D:\\Conda_offline\\new3109cc\\python.exe"
# "F:\\Installed_Soft\\Anaconda3\\envs\\new3109cc\\python.exe"
# "D:\\Conda_offline\\new3109cc\\python.exe"
include_no_ext_files = True  # 是否包含无扩展名文件
file_type_bin = ['.exe', '.dll', '.bin']
search_string_bytes = search_string.encode('utf-8')
python_exe_bytes = b"python.exe"

# 遍历指定路径下的所有文件
def traverse_and_replace(path_to_search, search_string, file_type_shebang, txt_replace_with, include_no_ext_files,
                         file_type_bin):
    for root, dirs, files in os.walk(path_to_search):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_extension = os.path.splitext(filename)[1].lower()

            # 处理文本文件或没有扩展名的文件
            if (file_extension in file_type_shebang) or (not file_extension and include_no_ext_files):
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
                                # 将文件指针移回文件的开始
                                f.seek(0)
                                # 写入替换后的内容
                                f.write(new_content)
                                # 截断文件以去除多余的内容（如果有的话）
                                f.truncate()
                                print(f"(bin) Replaced in {file_path}")
                            # else:
                            #     print(f"Did not find {python_exe_bytes} after {search_string_bytes} in {file_path}")
                        # else:
                        #     print(f"Did not find {search_string_bytes} in {file_path}")
                except IOError as e:
                    print(f"Error reading or writing binary file {file_path}: {e}")

                # 开始执行程序


traverse_and_replace(path_to_search, search_string, file_type_shebang, txt_replace_with, include_no_ext_files,
                     file_type_bin)
