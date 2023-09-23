import os
import shutil
from os import listdir, getcwd
from os.path import join
import random

f_train = open('VisDronetrain.txt', 'w')
f_test = open('VisDronetext.txt', 'w')
f_valid = open('VisDronevalid.txt', 'w')

tmp = os.getcwd()
tmp += '/VisDrone2019-VID-YOLOv7/'
dirpath = ['train', 'test-dev', 'val']
list_dir = ['JPEGImages', 'labels']
train_list = []
test_list = []
valid_list = []

for i in range(len(dirpath)):
    for j in range(len(list_dir)):
        if j == 0:
            path = tmp + '/' + dirpath[i] + '/' + list_dir[j]
            for image in os.listdir(path):
                if 'jpg' in image:
                    if i == 0:
                        train_list.append(os.path.join(path, image))
                    elif i == 1:
                        test_list.append(os.path.join(path, image))
                    elif i == 2:
                        valid_list.append(os.path.join(path, image))
        elif j == 1:
            # 把labels文件夹中的txt文件移动到到JPEGImages文件夹中
            path = tmp + '/' + dirpath[i] + '/' + list_dir[j]
            for label in os.listdir(path):
                if 'txt' in label:
                    shutil.move(os.path.join(path, label), tmp + '/' + dirpath[i] + '/' + list_dir[0])

for i in range(len(train_list)):
    f_train.write(train_list[i] + '\n')
print("Train set created.")
print("Number of train samples:", len(train_list))
for i in range(len(test_list)):
    f_test.write(test_list[i] + '\n')
print("Test set created.")
print("Number of test samples:", len(test_list))
for i in range(len(valid_list)):
    f_valid.write(valid_list[i] + '\n')
print("Validation set created.")
print("Number of validation samples:", len(valid_list))

f_train.close()
f_valid.close()
