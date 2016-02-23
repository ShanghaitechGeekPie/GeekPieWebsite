#coding=utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response,HttpResponse,Http404
from activities_techoverflow_db.models import ActivityTechOverflowModel
from django.views.decorators.csrf import csrf_exempt
import re

@csrf_exempt
def datacontrol_activities_register(request):
    try:
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        if re.match(r'^\S+$', name) and re.match(r'^\d+$', phone) and re.match(r'^[\w\d]+[\d\w\_\.]+@([\d\w]+)\.([\d\w]+)(?:\.[\d\w]+)?$', email):
            t = ActivityTechOverflowModel(
                name = name,
                phone = phone,
                email = email,
                target = 1,
                )
            t.save()
            return HttpResponse('<script language="javascript">alert("您已成功登记报名本次活动~");window.location.href="/activities/techoverflow/";</script>')
        else:
            return HttpResponse('<script language="javascript">alert("输入字段看起来不太合法哦~");window.location.href="/activities/techoverflow/";</script>')
    except:
        return HttpResponse('<script language="javascript">alert("服务器傲娇啦！哼~");window.location.href="/activities/techoverflow/";</script>')
