from PIL import Image
import os

# 用途：用于批量裁剪图片

# 1. 设置工作文件夹路径和输出文件夹路径
work_dir = "D:/MY_DOCUMENTS/Python_Projs/My_Apps/handy_tools/images_to_cut"  # 修改为实际工作目录
output_dir = os.path.join(work_dir, "output")

# 2. 设置支持的图片文件扩展名列表
supported_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']

# 3. 读取工作文件夹下的图片文件
image_files = [f for f in os.listdir(work_dir) 
              if os.path.splitext(f)[1].lower() in supported_extensions]
# 打印读取到的文件数量
print(f"Found {len(image_files)} image files.")

# 4. 设置裁剪坐标 (左上角x, 左上角y, 右下角x, 右下角y)
# 多组坐标将保存成多个文件
crop_coords = [
    (114, 574, 964, 1825),  # 示例坐标1
    # (43, 1987, 1013, 2293),    # 示例坐标2
    # 添加更多裁剪坐标...
]

# 5. 创建输出文件夹（如果不存在）
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 用于计数处理文件数量的变量
processed_files = 0
# 6. 对每个图片文件进行裁剪操作
for image_file in image_files:
    # 打开图片
    img_path = os.path.join(work_dir, image_file)
    with Image.open(img_path) as img:
        # 对每个裁剪坐标进行裁剪
        for i, coords in enumerate(crop_coords):
            # 执行裁剪
            cropped_img = img.crop(coords)
            
            # 生成输出文件名
            base_name, ext = os.path.splitext(image_file)
            output_filename = f"{base_name}_crop{i+1}{ext}"
            output_path = os.path.join(output_dir, output_filename)
            
            # 保存裁剪后的图片
            cropped_img.save(output_path)
            print(f"Saved: {output_path}")
        # 打印已处理多少个文件/共多少个文件
        processed_files += 1
        print(f"(Processed {processed_files}/{len(image_files)} files.)")

print("All images processed!")
