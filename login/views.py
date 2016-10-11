from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from login.models import User

# Create your views here.


class UserForm(forms.Form):
    username = forms.CharField(label='用户',max_length=100)
    password = forms.CharField(label='password',widget=forms.PasswordInput())
#注册
def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单信息
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #写入数据库
            # user = User()
            # user.username = username
            # user.password = password
            # user.save()
            User.objects.create(username=username,password=password)
            return HttpResponse('resgist ok!')
    else:
        uf = UserForm()
    return render_to_response('register/register.html',{'uf':uf})

#登录
def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            # 获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact=username, password__exact=password)
            #与数据库进行比较密码
            if user:
                response = HttpResponseRedirect('../index/')
                response.set_cookie('username',username,3600)
                return response
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render_to_response('login/login.html', {'uf': uf})

#
def index(req):
    username = req.COOKIES.get('username')
    return render_to_response('index/index.html',{'username':username})

#
def logout(req):
    response = HttpResponse('logout!!')
    response.delete_cookie('username')
    return response


