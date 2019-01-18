#Author:ley
# --*-- coding: utf-8 --*--
#@Time : 2019-01-17 15:43
#@Author: ley
#@Site : 
#@File : forms.py
#@Software : PyCharm
from django import forms
from django.forms import fields
from captcha.fields import CaptchaField

class UserForm(forms.Form):
    username=forms.CharField(label='用户名',max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    #用于指定该字段在form表单里表现为<input type='password' />，也就是密码输入框
    password=forms.CharField(label='密码',max_length=256,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    captcha=CaptchaField(label='验证码')


class RegisterForm(forms.Form):
    gender=(
        ('male','男'),
        ('Famale','女')
    )

    username=forms.CharField(label='用户名',max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='密码',max_length=256,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='确认密码',max_length=256,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email=forms.EmailField(label='邮箱地址',widget=forms.EmailInput(attrs={'class':'form-control'}))
    sex=forms.ChoiceField(label='性别',choices=gender)
    captcha=CaptchaField(label='验证码')



class FileForm(forms.Form):
    file=fields.FileField()