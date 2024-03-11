import os
import shutil


# 要搜索的conda环境路径
conda_env_path = 'F:\\Installed_Soft\\Anaconda3\\envs\\new3109glm3'  # new3109  new3109glm new3109glm3
# 'D:\\Conda_offline\\new3109finetune'  # 'C:\\Users\\Bruce\\anaconda3\\envs\\new3109cc'
# "D:\\My_Doc\\PythonProjs\\chatRecorder_Env"

cnt=0
# 遍历conda环境目录
for root, dirs, files in os.walk(conda_env_path):
    # 检查当前目录是否包含__pycache__
    if '__pycache__' in dirs:
        # 构建__pycache__的完整路径
        pycache_dir = os.path.join(root, '__pycache__')
        # 递归删除__pycache__目录
        shutil.rmtree(pycache_dir)
        cnt += 1
        print("删除文件夹数量=", cnt)

