from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserInfo
from task.models import TaskContent
from . import models
import utils


# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    if request.method == "POST":
        name = request.POST.get("username")
        passwd = request.POST.get("password")
        record = models.UserInfo.objects.get(username=name)
        password = record.password
        if password == passwd:
            ip = utils.getIPaddress(request)
            record.last_login_ip = ip
            record.save()
            request.session['is_login'] = True
            request.session['user'] = record.username
            return redirect('/index/')
        else:
            return render(request, 'login.html', {'errmsg': '密码错误'})
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        ip = utils.getIPaddress(request)
        try:
            record = UserInfo(username=username, password=password, last_login_ip=ip)
            record.save()
        except Exception as e:
            return HttpResponse("注册失败 失败原因:%s" % e)
        return HttpResponse("注册成功")

def logout(request):
    if request.session.get('is_login'):
        request.session.flush()
        return render(request, 'userloginfo.html', {'info': '成功注销用户'})
    else:
        return render(request, 'userloginfo.html', {'info': '未登陆'})