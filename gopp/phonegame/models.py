# This Python file uses the following encoding: utf-8

from django.db import models
# from django_extensions.db.fields import UUIDField
from uuidfield import UUIDField
import uuid
# Create your models here.

class companyinfo(models.Model):
    ccreatedate = models.DateTimeField('date published') #创建时间
    company = models.CharField("厂商名称",max_length=50)  #厂商名称
    companyid= models.CharField("厂商ID",max_length=10,primary_key=True) #厂商ID
    crating = models.IntegerField("评分",blank=True, null=True)  #厂商评分
    cvotes = models.IntegerField("票数",blank=True, null=True) #厂家票数

    def __unicode__(self):
        return self.company


class gameinfo(models.Model):
    cinfo = models.ForeignKey(companyinfo)
    gamename = models.CharField("游戏名称",max_length=50) #游戏名
    gcreatedate = models.DateTimeField('date published') #创建时间
    gameid = models.CharField("游戏ID",max_length=10,primary_key=True) ##游戏ID
    grating = models.IntegerField("游戏评分",blank=True, null=True)  #游戏评分
    appkey = UUIDField(version=1,auto=True)#唯一标识
    gvotes = models.IntegerField("游戏票数",blank=True, null=True) #玩家票数

    def __unicode__(self):
        return self.gamename