import os
import shutil

# 获取当前脚本所在的目录路径
conda_env_path = os.path.dirname(os.path.abspath(__file__))

cnt = 0
# 遍历conda环境目录
for root, dirs, files in os.walk(conda_env_path):
    # 检查当前目录是否包含__pycache__
    if '__pycache__' in dirs:
        # 构建__pycache__的完整路径
        pycache_dir = os.path.join(root, '__pycache__')
        # 递归删除__pycache__目录
        shutil.rmtree(pycache_dir)
        cnt += 1
        #print("删除文件夹数量=", cnt)
        print(f"\r删除文件夹数量={cnt}     ", end="")
