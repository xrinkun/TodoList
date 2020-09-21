from django.shortcuts import render
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
            'last_change': item.last_change
        }
        task_list.append(task_detail)
    return render(request, 'index.html', {'username': name, 'task_num': task_num, 'task_list': task_list})
