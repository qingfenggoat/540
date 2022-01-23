#coding:utf-8
import re
from tqdm import trange
# inputfile = "dials.txt"
input_file = "Text.src_dm"
output_file = "splited.txt"

'''split_write_function(input_file，output_file)'''
'''函数作用：用于输入字符串，按照问答分割为list后写入到输入文件中'''
def split_write_function(filename1,filename2):
    '''统计目标文件的行数（\n个数），以便于后续range（count）'''
    count = 0
    target_file = open(filename1, encoding='utf-8')
    while True:
        buffer = target_file.read(1024 * 8192)
        if not buffer:
            break
        count += buffer.count('\n')
    target_file.close()
    # print(count)
    with open(filename1,'r',encoding='utf-8') as f:
        lines = f.read().splitlines()
        # test
        # for i in range(100):
        #     print(re.split("答：|问：",lines[i]))
        with open(filename2, 'w',encoding='utf-8' ) as f:
            for i in trange(count+1):
                f.write(str(re.split("答：|问：",lines[i])) + ',')
                pass
split_write_function(input_file, output_file)

