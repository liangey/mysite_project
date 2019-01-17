#Author:ley
# --*-- coding: utf-8 --*--
#@Time : 2019-01-17 15:43
#@Author: ley
#@Site : 
#@File : forms.py
#@Software : PyCharm
from django import forms

class UserForm(forms.Form):
    username=forms.CharField(label='用户名',max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    #用于指定该字段在form表单里表现为<input type='password' />，也就是密码输入框
    password=forms.CharField(label='密码',max_length=256,widget=forms.PasswordInput(attrs={'class':'form-control'}))

