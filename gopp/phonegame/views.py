# This Python file uses the following encoding: utf-8
from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
import json
from phonegame.models import gameinfo
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

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