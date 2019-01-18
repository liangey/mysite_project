#Author:ley
# --*-- coding: utf-8 --*--
#@Time : 2019-01-18 10:09
#@Author: ley
#@Site : 
#@File : send_mail.py
#@Software : PyCharm

import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'MySite.settings'

if __name__ == '__main__':

    send_mail(
        '来自测试邮件',
        '这里是test站点',
        'ddd@sina.com',
        ['ddd@qq.com'],
    )