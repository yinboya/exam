# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'home_application.views',
    (r'^$', 'home'),
    (r'^dev-guide/$', 'dev_guide'),
    (r'^contactus/$', 'contactus'),
    (r'^business/$', 'business'),  # 获取业务的接口
    (r'^cluster/(\d+)$', 'cluster'),  # 根据业务获取集群的接口
    (r'^host/$', 'host'),  # 根据业务获取集群的接口
    (r'^select_script/$', 'select_script'),  # 选择脚本的接口
    (r'^script_management/$', 'script_management'),  # 脚本列表的接口
    (r'^add_script/$', 'add_script'),  # 添加脚本的接口
    (r'^delete_script/(\d+)$', 'delete_script'),  # 删除脚本的接口
    (r'^delete_script/(\d+)$', 'delete_script'),  # 删除脚本的接口

)
