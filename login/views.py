from django.shortcuts import render,redirect
from django.http import HttpResponse
from login import models,forms
import hashlib

# Create your views here.

def hash_code(s,salt='MySite'):
    h=hashlib.sha256()
    s+=salt
    # update方法只接收bytes类型
    h.update(s.encode())
    return h.hexdigest()



def index(request):
    pass
    #print("hello world")
    return render(request,'login/index.html')



def login(request):
    if request.session.get('is_login',None):
            return redirect("/index/")
    if request.method=="POST":
        login_form=forms.UserForm(request.POST)
        message = "所有字段都必须填写！"
        if login_form.is_valid():
            username=login_form.cleaned_data['username']
            password=login_form.cleaned_data['password']
            try:
                user=models.User.objects.get(username=username)

                if user.password==hash_code(password):
                    request.session['is_login']=True
                    request.session['user_id']=user.id
                    request.session['user_name']=user.username
                    return redirect('/index')
                else:
                    message="密码不正确！"
            except:
                message = "用户名不存在！"
        return render(request,'login/login.html',locals())
    login_form=forms.UserForm()
    return render(request, 'login/login.html',locals())




def register(request):
    if request.session.get('is_login',None):
        return redirect("/index/")
    if request.method=="POST":
        register_form=forms.RegisterForm(request.POST)
        message="请检查填写的内容"
        if register_form.is_valid():
            username=register_form.cleaned_data['username']
            password1=register_form.cleaned_data['password1']
            password2=register_form.cleaned_data['password2']
            email=register_form.cleaned_data['email']
            sex=register_form.cleaned_data['sex']

            if password1 != password2:
                message="两次输入的密码不一致"
                return render(request,'login/register.html',locals())
            else:
                same_name_user=models.User.objects.filter(username=username)
                if same_name_user:
                    message="该用户名已存在"
                    return render(request,'login/register.html',locals())

                same_email=models.User.objects.filter(email=email)
                if same_email:
                    message="该邮箱已被注册"
                    return render(request,'login/register.html',locals())


                new_user=models.User()
                new_user.username=username
                new_user.password=hash_code(password1)
                new_user.email=email
                new_user.sex=sex
                new_user.save()
                return redirect('/login/')
    register_form=forms.RegisterForm()
    return render(request,'login/register.html',locals())



def logout(request):
    if not request.session.get('is_login',None):
        return redirect("/index/")
    request.session.flush()
    #在顶部额外导入了redirect，用于logout后，页面重定向到‘index’首页
    return redirect("/index/")