from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import TaskContent
from user.models import UserInfo


# Create your views here.
def index(request):
    status = request.session.get('is_login')
    if not status:
        return render(request, 'index.html', {'username': '未登陆', 'task_num': 0, 'task_list': None})
    name = request.session.get('user')
    record = UserInfo.objects.filter(username=name).first()
    obj_set = record.taskcontent_set.filter(user_id=record.id)
    task_num = obj_set.count()
    task_list = []
    for item in obj_set:
        task_detail = {
            'title': item.title,
            'content': item.content,
            'add_time': item.add_time,
            'last_change': item.last_change,
            'id': item.id
        }
        task_list.append(task_detail)
    return render(request, 'index.html', {'username': name, 'task_num': task_num, 'task_list': task_list})

def addTask(request):
    if request.method == "POST":
        if request.session['is_login']:
            if request.GET.get("type") == "add":
                username = request.session['user']
                title = request.POST.get('title')
                content = request.POST.get('content')
                user_id = UserInfo.objects.filter(username=username).first().id
                record = TaskContent(title=title, content=content, user_id=user_id)
                record.save()
                return redirect('/index/')
            elif request.GET.get("type") == "edit":
                username = request.session['user']
                title = request.POST.get("title")
                content = request.POST.get("content")
                task_id = request.POST.get("task_id")
                record = TaskContent.objects.filter(id=task_id).first()
                record.title = title
                record.content = content
                record.save()
                return redirect('/index/')
        else:
            return HttpResponse("<a href='/login/'>请登陆</a>")

def deleteTask(request):
    if request.method == "GET":
        id = request.GET.get("id")
        TaskContent.objects.get(id=id).delete()
        return redirect('/index/')