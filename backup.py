#!/usr/bin/env python
#coding=utf-8
# Filename: backup.py
# Description: backup script

import subprocess
import time
import os
import sys,getopt

'''
* 1 源：需要备份的文件
* 2 目的：备份文件存放位置
* 3 备份方式：比如使用zip压缩
* 4 备份
* 5 转移
'''

opts,args = getopt.getopt(sys.argv[1:], 'ht:', ['help', 'type='])
for opt,arg in opts:
	if opt in ('-h', '--help'):
		print 'Please input backup.py -h -t zip or tar.gz'
	if opt in ('-t', '--type'):
		file_fmt = arg

# version 1: 某些特定文件
# version 2: 某种类型文件
# version 3: 自动扫描目录下的文件
# Note: python的格式？
src_dir = '/Users/Eric/Workspace/my_project/python/backup/source/'
dest_dir = '/Users/Eric/Workspace/my_project/python/backup/dest'
source_list = [src_dir + 'a.c', src_dir + 'b.c', src_dir + 'c.c']

comment = raw_input('Enter comment: ')

date = time.strftime('%Y.%m.%d')
time = time.strftime('%H:%M:%S')

# os.sep: 目录分隔符 增加跨平台性
target_dir = dest_dir + os.sep + date

if len(comment) == 0:
	file_name = time
else:
	file_name = time + '_' + comment.replace(' ', '_')

file_en = file_name + '.' + file_fmt

if not os.path.exists(dest_dir):
	os.mkdir(dest_dir)

if not os.path.exists(target_dir):
	os.mkdir(target_dir)

if file_fmt == 'zip':
	pk_cmd = "zip -r %s %s" % (file_en, ' '.join(source_list))
elif file_fmt == 'tar.gz':
	pk_cmd = "tar -czvf %s %s" % (file_en, ' '.join(source_list))

mv_cmd = "mv %s %s" % (file_en, target_dir + '/')

if subprocess.call(pk_cmd, shell=True) == 0:
	if subprocess.call(mv_cmd, shell=True) == 0:
		print 'Successful backup to', target_dir + '/' + file_en
	else:
		print 'Failed to move'
else:
	print 'Backup failed'
