# -*- coding: utf-8 -*-
# __auther__ = 'lewen'



import os,time
#fork只能用于linux/unix中
print("bobby")
pid = os.fork()   # 创建子进程

# print("bobby")
if pid == 0:

  print('子进程 {} ，父进程是： {}.' .format(os.getpid(), os.getppid()))
else:
  print('我是父进程：{}.'.format(pid))

time.sleep(2)
#  进程的数据是完全隔离的
#  子进程完全拷贝父进程的数据去执行



# 很底层了
