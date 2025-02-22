import os
import io

# 用途：递归地遍历指定文件夹及其所有子文件夹，并检查每个可以打开为文本的文件是否包含该字符串
# 在环境的记录文件里，例如 myPy310\conda-meta\history ，有当时建立环境的命令行记录
# 有一些 .py文件和无扩展名文件，在开头会有一行 shebang： “#!F:\Installed_Soft\Anaconda3\envs\new3109\python.exe”
# 有一些exe文件则在末尾处有嵌入此字符串

# 设置要搜索的文件夹：...
path_to_search = "F:\Installed_Soft\Anaconda3\envs\\new3109qwen\\Scripts"
#"/home/bruce/My_Doc/llama.cpp_test"#
# 'D:\\MY_DOCUMENTS\\Python_Projs\\My_Apps\\handy_tools'
# 'D:\\Conda_offline\\new3109cc' # 'C:\\Users\\Bruce\\anaconda3\\envs\\new3109cc'

# 要搜索的字符串（大小写敏感）
search_string = "F:\Installed_Soft\Anaconda3\envs\\new3109qwen\python.exe"
# 'graph has different number of nodes'
# zx7: 'F:\\Installed_Soft\\Anaconda3'  'Qwen'
# x99: 'D:\\Conda_offline\\new3109cc' # 'C:\\Users\\Bruce\\anaconda3\\envs\\new3109cc'

# 文本文件，忽略特定扩展名的文件：...
file_type_shebang_exclude = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.bin', '.so', '.exe', '.dll', '.sys', '.mof')#, ''
# ignore_files = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')

# 要搜索的二进制文件
file_type_bin = ['.exe', '.dll', '.bin']
search_string_bytes = search_string.encode('utf-8')

# 定义一个函数来检查文件是否包含特定字符串
def check_file_for_string(file_path, search_string, search_string_bytes):
    global cnt_found, cnt_case_unsen
    try:
        # 尝试以文本模式打开文件
        with io.open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            file_content = file.read()
            # 读取文件内容并检查字符串
            if search_string in file_content:
                print(f'Found(txt mode)\t\t\t "{search_string}" in {file_path}')
                cnt_found += 1
                return True
            elif search_string.lower() in file_content.lower():
                print(f'(U)Found(txt mode)\t\t\t "{search_string}" in {file_path}')
                cnt_case_unsen += 1
                return True
    except Exception as e:
        # 如果文件无法以文本模式打开，则忽略错误并继续
        print(f'Error reading {file_path}: {e}')
        return False


def check_bin_file_for_string(file_path, search_string, search_string_bytes):
    global cnt_found, cnt_case_unsen, cnt_found_bin
    try:
        with open(file_path, 'rb') as file:
            file_content = file.read()
            search_pos = file_content.find(search_string_bytes)
            if search_pos != -1:
                print(f'Found(binPos={search_pos})\t "{search_string}" in {file_path}')
                cnt_found_bin += 1
                return True
    except Exception as e:
        # 如果文件无法以二进制模式打开，则忽略错误并继续
        print(f'Error reading {file_path} in binary mode: {e}')
        return False


# 遍历目录并检查文件
def search_directory_for_string(path, search_string, search_string_bytes, file_type_bin):
    for root, dirs, files in os.walk(path):
        for filename in files:
            # 忽略特定扩展名的文件，只检查可能的文本文件
            # if not filename.endswith(ignore_files):
            file_extension = os.path.splitext(filename)[1].lower()
            file_path = os.path.join(root, filename)
            if (file_extension not in file_type_shebang_exclude):
                # 检查文件是否包含搜索字符串
                check_file_for_string(file_path, search_string, search_string_bytes)
            elif file_extension in file_type_bin:
                # 检查二进制文件是否包含搜索字符串
                check_bin_file_for_string(file_path, search_string, search_string_bytes)

cnt_found = 0
cnt_case_unsen = 0
cnt_found_bin = 0
search_directory_for_string(path_to_search, search_string, search_string_bytes, file_type_bin)
print(f'找到 {cnt_found} 个， {cnt_case_unsen} 个(大小写不敏感)，{cnt_found_bin} 个二进制文件')