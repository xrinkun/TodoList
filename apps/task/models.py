from django.db import models
from user.models import UserInfo


# Create your models here.
class TaskContent(models.Model):
    title = models.CharField(max_length=100, verbose_name="标题")
    content = models.TextField(verbose_name="内容")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    last_change = models.DateTimeField(auto_now=True, verbose_name="最后一次修改时间")
    user = models.ForeignKey(UserInfo, verbose_name="用户信息", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "任务内容"
        verbose_name_plural = verbose_name
