# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from common.mymako import render_mako_context, render_json
from home_application import models
from home_application.utils import ESB


def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/demo_one.html')


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')

def business(request):
    """
    获取业务的接口
    :param request:
    :return:
    """
    response = {}
    data_list = []
    try:
        result = ESB.ESBApi(request).search_business()
        if result['result']:
            response['result'] = True
            response['code'] = 0
            response['message'] = 'success'
            response['data'] = {}
            if len(result['data']['info']) > 0:
                for item in result['data']['info']:
                    dic = {}
                    dic['id'] = item['bk_biz_id']
                    dic['name'] = item['bk_biz_name']
                    data_list.append(dic)
                    response['data'] = data_list
        else:
            response['result'] = True
            response['code'] = 0
            response['message'] = u'该用户下没有业务'
            response['data'] = {}
    except Exception, e:
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' %e
        response['data'] = {}
    return render_json(response)

def cluster(request, bk_biz_id):
    """
    根据业务获取集群的接口
    :param request:
    :return:
    """
    bk_biz_id = int(bk_biz_id)
    response = {}
    try:
        result = ESB.ESBApi(request).search_set(bk_biz_id=bk_biz_id)
        if result:
            response['result'] = True
            response['code'] = 0
            response['message'] = 'success'
            response['data'] = []
            list = []
            if len(result['data']['info']) > 0:
                for item in result['data']['info']:
                    dic = {}
                    dic['set_id'] = item['bk_set_id']
                    dic['set_name'] = item['bk_set_name']
                    list.append(dic)
                response['data'] = list
            else:
                response['result'] = True
                response['code'] = 0
                response['message'] = u'该用户下无业务'
                response['data'] = []
        else:
            response = result
    except Exception, e:
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取主机列表失败：%s'%e
        response['data'] = []
    return render_json(response)

def host(request):
    """
    根据业务获取主机的接口
    :param request:
    :param bk_biz_id:
    :return:
    """
    bk_biz_id = request.GET.get('bk_biz_id')
    print bk_biz_id
    # bk_biz_id = 39
    set_id = request.GET.get('set_id')
    print set_id
    # set_id = 98
    response = {}
    try:
        result = ESB.ESBApi(request).search_host_set(biz_id=bk_biz_id)
        list = []
        if result:
            response['result'] = True
            response['code'] = 0
            response['message'] = 'success'
            response['data'] = []
            if result['data']['count'] > 0:
                for i in result['data']['info']:
                    for j in i['set']:
                        if int(j['bk_set_id']) == int(set_id):
                            dic = {}
                            dic['hostname'] = i['host']['bk_host_name']
                            dic['ip'] = i['host']['bk_host_innerip']
                            dic['os_type'] = i['host']['bk_os_type']
                            dic['os_name'] = i['host']['bk_os_name']
                            bk_cloud = i['host']['bk_cloud_id']
                            dic['area'] = bk_cloud[0]['bk_inst_name']
                            dic['area_id'] = bk_cloud[0]['bk_inst_id']
                            list.append(dic)
                response['result'] = True
                response['code'] = 0
                response['message'] = 'success'
                response['data'] = list
            else:
                response['result'] = True
                response['code'] = 0
                response['message'] = u'没有主机'
                response['data'] = []
    except Exception, e:
        response['result'] = False
        response['code'] = 1
        response['message'] = '%s' % e
        response['data'] = []
    return render_json(response)


def select_script(request):
    """
    选择脚本的接口
    :param request:
    :return:
    """
    response = {}
    l = []
    try:
        data = models.Script.objects.all()
        if data:
            for i in data:
                dic = {}
                dic['id'] = i.id
                dic['name'] = i.name
                l.append(dic)
            response['code'] = 0
            response['message'] = 'success'
            response['data'] = l
        else:
            response['code'] = 0
            response['message'] = u'没有脚本'
            response['data'] = []
    except Exception, e:
        response['code'] = 1
        response['message'] = '%s' % e
        response['data'] = []
    return render_json(response)


def script_management(request):
    """
    脚本展示的接口
    :param request:
    :return:
    """
    all_script_data = models.Script.objects.all()
    return render_mako_context(request, '/home_application/script_supervise.html', {'all_script_data': all_script_data})


def add_script(request):
    """
    添加脚本的接口
    :param request:
    :return:
    """
    name = request.GET.get('script_name')
    content = request.GET.get('script_content')
    models.Script.objects.create(
        name=name,
        script_content=content
    )
    return redirect(reverse(script_management))

def delete_script(request, script_id):
    """
    删除脚本的接口
    :param request:
    :return:
    """
    script_data = models.Script.objects.get(id=script_id)
    script_data.delete()
    return redirect(reverse(script_management))