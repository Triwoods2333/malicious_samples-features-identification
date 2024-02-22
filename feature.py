from pathlib import Path
import pandas as pd
from collections import Counter

# 定义源码所在的目录路径，根据实际情况进行调整
source_code_directory_path = Path("/home/kali/Desktop/urijs/src/")

# 初始化计数器
total_words = 0
total_lines = 0

# 初始化文件类型计数器
file_types = ['.bat', '.bz2', '.c', '.cert']
file_type_counts = Counter({ext: 0 for ext in file_types})

# 遍历目录中的每个文件
for file_path in source_code_directory_path.rglob("*"):  # 使用rglob以递归查找所有文件
    # 统计指定文件扩展名的文件数量
    if file_path.suffix in file_types:
        file_type_counts[file_path.suffix] += 1
    
    # 统计JavaScript文件的单词数和行数
    if file_path.suffix == '.js' and file_path.is_file():  # 确保是文件而不是目录
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total_lines += len(lines)  # 累加行数
            total_words += sum(len(line.split()) for line in lines)  # 累加单词数

# 准备数据
data = {
    "Number of Words in source code": [total_words],
    "Number of lines in source code": [total_lines]
}

# 加入各文件类型的数量
data.update({ext: [file_type_counts[ext]] for ext in file_types})

# 创建DataFrame
df = pd.DataFrame(data)

# 保存到CSV文件
csv_file_path = "/home/kali/Desktop/source_code_statistics.csv"
df.to_csv(csv_file_path, index=False)

# 输出CSV文件路径，以便下载
print(csv_file_path)
