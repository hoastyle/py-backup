#!/usr/bin/env python
#coding=utf-8
# Filename: backup.py
# Description: backup script

import subprocess
import time

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

dest_dir = '/Users/Eric/Workspace/my_project/python/backup/dest'
file_name = time.strftime('%Y.%m.%d-%H:%M:%S')
file_fmt = 'zip'
file_en = file_name + '.' + file_fmt

print file_name
print file_fmt
print file_en

package_command = "zip -r %s %s" % (file_en, ' '.join(source_list))
print package_command
move_command = "mv %s %s" % (file_en, dest_dir + '/')
print move_command

if subprocess.call(package_command, shell=True) == 0:
	if subprocess.call(move_command, shell=True) == 0:
		print 'Successful backup to', dest_dir + '/' + file_en
	else:
		print 'Failed to move'
else:
	print 'Backup failed'
