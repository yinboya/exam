# _*_ coding:utf-8 _*_
from django.db import models


class Script(models.Model):
    name = models.CharField(verbose_name=u'脚本名称', max_length=100)
    script_content = models.TextField(verbose_name=u'脚本内容', null=True)

    class Meta:
        verbose_name = u'脚本表'