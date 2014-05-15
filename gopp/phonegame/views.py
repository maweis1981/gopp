# This Python file uses the following encoding: utf-8
from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
import json
from phonegame.models import gameinfo,companyinfo
from django.core import serializers
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def allCompanyData(request):
    try:
        responsejson = {}
        if companyinfo.objects.count() > 0:
            responsejson['result'] ='1'
            datas = {}
            for obj in companyinfo.objects.all():
                datas['company'] = obj.company
                datas['companyid'] = obj.companyid
                datas['ccreatedate'] = obj.ccreatedate.strftime('%Y-%m-%d %H:%M')
                if obj.crating is not None:
                    datas['crating'] = obj.crating
                else :
                    datas['crating'] = ''
                if obj.crating is not None:
                    datas['cvotes'] = obj.cvotes
                else :
                    datas['cvotes'] = ''
                ginfos =  obj.gameinfo_set.all()
                infodic = [0]*obj.gameinfo_set.all().count()
                gindex = 0
                for info in ginfos:
                    gamedic = {}
                    gamedic['gamename'] = info.gamename
                    gamedic['gcreatedate'] = info.gcreatedate.strftime('%Y-%m-%d %H:%M')
                    gamedic['gameid'] = info.gameid
                    gamedic['grating'] = info.grating
                    gamedic['appkey'] = str(info.appkey)
                    gamedic['gvotes'] = info.gvotes
                    infodic[gindex] = gamedic
                    gindex+=1

                datas['games'] = infodic

            responsejson['datas'] =datas
        else :
            responsejson['result'] ='0'
        jsonall =  json.dumps(responsejson)
    except companyinfo.DoesNotExist:
        raise Http404
    return HttpResponse(jsonall,content_type="application/json")
# def detail(request, poll_id):
#     response_data = {}
#     # response_data['result'] = 'failed'
#     # response_data['message'] = 'You messed up'
#     try:
#         poll =Poll.objects.get(pk=poll_id)
#         response_data['question'] = poll.question
#         response_data['pub_date'] = poll.pub_date.strftime('%Y-%m-%d %H:%M')
#     except Poll.DoesNotExist:
#         raise Http404
#     return HttpResponse(json.dumps(response_data), content_type="application/json")