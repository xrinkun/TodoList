import xadmin
from xadmin import views
from .models import TaskContent


class GlobalSettings:
    """
    后台修改
    """
    site_title = 'todolist后台'
    site_footer = 'xrinkkun @copyright 2020'
    # menu_style = 'accordion'  开启分组折叠


class TaskContentAdmin:
    list_display = ['title', 'content', 'add_time', 'last_change', 'user']
    list_filter = ['title', 'content', 'add_time', 'last_change', 'user']
    search_fields = ['user', 'title']


xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(TaskContent, TaskContentAdmin)
