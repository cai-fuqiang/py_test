import re
from datetime import datetime

# 输入文件和输出文件
input_file = 'log.txt'
output_file = 'log.txt2'

# 日期时间的正则表达式模式
datetime_pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})'

# 打开输入文件并读取内容
with open(input_file, 'r') as file:
    content = file.read()

# 使用正则表达式查找并替换日期时间字符串
def replace_datetime_with_timestamp(match):
    datetime_str = match.group(1)
    # 将日期时间字符串转换为 Unix 时间戳
    dt = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
    timestamp = int(dt.timestamp())
    return str(timestamp)

# 替换所有匹配的日期时间字符串
new_content = re.sub(datetime_pattern, replace_datetime_with_timestamp, content)

# 将替换后的内容写入输出文件
with open(output_file, 'w') as file:
    file.write(new_content)

