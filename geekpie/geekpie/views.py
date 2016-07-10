#coding=utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response,HttpResponse,Http404
from django.http import HttpResponse, JsonResponse
from activities_techoverflow_db.models import ActivityTechOverflowModel
from activities_vot_db.models import ActivityVOTModel
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

@csrf_exempt
def datacontrol_vot_reply(request):
    try:
        f = filter.DFAFilter()
        f.parse("keywords")
        name = request.POST.get('name')
        reply = f.filter(request.POST.get('reply'))
        t = ActivityVOTModel(
            name = name,
            reply = reply,
            )
        t.save()
        return HttpResponse('biu~')
    except:
        return HttpResponse('服务器傲娇啦！哼~')

import filter
def datacontrol_vot_show(request):
    replies = ActivityVOTModel.objects.all()[::-1][:100]
    content = [{
        'name': reply.name,
        'reply': reply.reply,
        } for reply in replies]

    return JsonResponse(content, safe=False)
