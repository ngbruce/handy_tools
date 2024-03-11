import os
import io

# 用途：递归地遍历指定文件夹及其所有子文件夹，并检查每个可以打开为文本的文件是否包含该字符串
# 在环境的记录文件里，例如 myPy310\conda-meta\history ，有当时建立环境的命令行记录
# 有一些 .py文件和无扩展名文件，在开头会有一行： “#!F:\Installed_Soft\Anaconda3\envs\new3109\python.exe”
# 考虑以后要加个程序选项，可以过滤掉这些

# 设置要搜索的文件夹：
path_to_search = 'D:\\Conda_offline\\new3109cc'
# 'D:\\Conda_offline\\new3109cc' # 'C:\\Users\\Bruce\\anaconda3\\envs\\new3109cc'
# 要搜索的字符串（大小写敏感）
search_string = 'F:\\Installed_Soft'
# zx7: 'F:\\Installed_Soft\\Anaconda3'  'Qwen'
# x99: 'D:\\Conda_offline\\new3109cc' # 'C:\\Users\\Bruce\\anaconda3\\envs\\new3109cc'

# 忽略特定扩展名的文件：
# .pyc是编译的文件，应该先运行 del_pycache.py 清除，exe文件里面也可能带有文本存放的路径      '.pyc', '.exe', '.dll',
# ignore_files = ( '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.bin', '.so')
ignore_files = ( '.png', '.jpg', '.jpeg', '.gif', '.bmp')
# 定义一个函数来检查文件是否包含特定字符串
def check_file_for_string(file_path, search_string):
    try:
        # 尝试以文本模式打开文件
        with io.open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            # 读取文件内容并检查字符串
            if search_string in file.read():
                print(f'Found "{search_string}" in {file_path}')
                return True
    except Exception as e:
        # 如果文件无法以文本模式打开，则忽略错误并继续
        print(f'Error reading {file_path}: {e}')
    return False


# 遍历目录并检查文件
def search_directory_for_string(path, search_string):
    for root, dirs, files in os.walk(path):
        for filename in files:
            # 忽略特定扩展名的文件，只检查可能的文本文件
            if not filename.endswith(ignore_files):
                file_path = os.path.join(root, filename)
                # 检查文件是否包含搜索字符串
                check_file_for_string(file_path, search_string)

            # 调用函数开始搜索


search_directory_for_string(path_to_search, search_string)