from django.db import models


# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=50, verbose_name="用户名")
    password = models.CharField(max_length=100, verbose_name="密码")
    last_login_ip = models.GenericIPAddressField(verbose_name="最后登录IP地址", null=True)
    # auto_now 为修改后自动修改
    last_login_time = models.DateTimeField(auto_now=True, verbose_name="最后登录时间")
    # auto_now_add 为创建model时自动填写当前时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    # admin中显示每条数据的title
    def __str__(self):
        return self.username

    class Meta:
        # admin点进表中所显示的信息
        verbose_name = "用户信息"
        # admin中显示的表名
        verbose_name_plural = "用户信息"
