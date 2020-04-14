# -*- encoding: utf-8 -*-
"""
@File    : demo.py
@Time    : 2020/4/9 13:19
@Author  : yuecong
@Email   : yueconger@163.com
@Software: PyCharm
"""
# a = ''
# if a:
#   print('000000000')


m = [(True, {'url': 'http://www.jinyongwang.com/public/uploads/baike/2015-08-15/71791439631762_120.jpg', 'path': '射雕英雄传_梁子翁.jpg', 'checksum': '273f43e91d8b6f0739cc226d9009b499'})]
print(len(m))
print(m[0][1]['path'])


a = ['http://www.jinyongwang.com/public/uploads/2015-08-14/55cdbcc654719_120.jpg']
n = ['http://www.jinyongwang.com/public/uploads/2015-08-14/55cdbd25d168e_120.jpg']

mmmmm = a[0].split('/')[-1]
print(mmmmm)