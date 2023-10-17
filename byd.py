import os
import shutil
import random

f_train = open('byd_train.txt', 'w')
f_valid = open('byd_valid.txt', 'w')

path = os.getcwd() + '/byd_dataset/'
tmp = os.getcwd()
tmp += '/byd/'
outpath_train_jpg = tmp + 'JPEGImages/train'
outpath_train_txt = tmp + 'labels/train'
outpath_valid_jpg = tmp + 'JPEGImages/val'
outpath_valid_txt = tmp + 'labels/val'

train_jpg_list = []
train_text_list = []
valid_jpg_list = []
valid_text_list = []

# 随机选取10%的数据作为验证集 剩下90%作为训练集
file_list_jpg = []
file_list_txt = []
for image in os.listdir(path):
    if 'jpg' in image:
        file_list_jpg.append(os.path.join(path, image))

random.shuffle(file_list_jpg)
total_files = len(file_list_jpg)
train_ratio = 0.9
train_files = file_list_jpg[:int(total_files * train_ratio)]
valid_files = file_list_jpg[int(total_files * train_ratio):]
# 把文件移动到对应的文件夹中
for file_path in train_files:
    shutil.move(file_path, outpath_train_jpg)
    train_jpg_list.append(os.path.join(outpath_train_jpg, file_path.split('/')[-1]))
    shutil.move(file_path.replace('jpg', 'txt'), outpath_train_txt)
    train_text_list.append(os.path.join(outpath_train_txt, file_path.split('/')[-1].replace('jpg', 'txt')))
for file_path in valid_files:
    shutil.move(file_path, outpath_valid_jpg)
    valid_jpg_list.append(os.path.join(outpath_valid_jpg, file_path.split('/')[-1]))
    shutil.move(file_path.replace('jpg', 'txt'), outpath_valid_txt)
    valid_text_list.append(os.path.join(outpath_valid_txt, file_path.split('/')[-1].replace('jpg', 'txt')))
# 写入txt文件
for file_path in train_jpg_list:
    f_train.write(file_path + '\n')
print("Train set created.")
print("Number of train samples:", len(train_jpg_list))

for file_path in valid_jpg_list:
    f_valid.write(file_path + '\n')
print("Validation set created.")
print("Number of validation samples:", len(valid_jpg_list))