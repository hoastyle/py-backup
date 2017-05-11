#!/usr/bin/env python
#coding=utf-8
# Filename: backup.py
# Description: backup script

import subprocess
import time
import os

'''
* 1 源：需要备份的文件
* 2 目的：备份文件存放位置
* 3 备份方式：比如使用zip压缩
* 4 备份
* 5 转移
'''

# version 1: 某些特定文件
# version 2: 某种类型文件
# version 3: 自动扫描目录下的文件
# Note: python的格式？
source_list = ['/Users/Eric/Workspace/my_project/python/backup/source/a.c', '/Users/Eric/Workspace/my_project/python/backup/source/b.c', '/Users/Eric/Workspace/my_project/python/backup/source/c.c']

comment = raw_input('Enter comment: ')


date = time.strftime('%Y.%m.%d')
time = time.strftime('%H:%M:%S')

dest_dir = '/Users/Eric/Workspace/my_project/python/backup/dest'
# os.sep: 目录分隔符 增加跨平台性
target_dir = dest_dir + os.sep + date

file_name = time + '_' + comment.replace(' ', '_')
file_fmt = 'zip'
file_en = file_name + '.' + file_fmt

if not os.path.exists(dest_dir):
	os.mkdir(dest_dir)

if not os.path.exists(target_dir):
	os.mkdir(target_dir)

pk_cmd = "zip -r %s %s" % (file_en, ' '.join(source_list))
mv_cmd = "mv %s %s" % (file_en, target_dir + '/')

if subprocess.call(pk_cmd, shell=True) == 0:
	if subprocess.call(mv_cmd, shell=True) == 0:
		print 'Successful backup to', target_dir + '/' + file_en
	else:
		print 'Failed to move'
else:
	print 'Backup failed'
