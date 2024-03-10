
import os
import datetime

# 获取当前日期和时间
now = datetime.datetime.now()
date_str = now.strftime('%Y-%m-%d')
time_str = now.strftime('%H-%M-%S')

# 生成文件名
file_name = f'win_env_{date_str}_{time_str}.txt'

# 检查目录是否存在，如果不存在，则新建目录
if not os.path.exists('win_env_records'):
    os.makedirs('win_env_records')

# 检查文件名是否存在，如果存在，则在文件名末尾加上序号
if os.path.exists(f'win_env_records/{file_name}'):
    i = 1
    while os.path.exists(f'win_env_records/{file_name}({i})'):
        i += 1
    file_name = f'{file_name}({i})'

# 获取所有环境变量
env_vars = os.environ

# 将环境变量保存到文件中
with open(f'win_env_records/{file_name}', 'w') as f:
    for key, value in env_vars.items():
        f.write(f'{key} = {value}\n')

