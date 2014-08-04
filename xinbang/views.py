# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from post.models import Post
from util.models import Person, Message
import datetime
def homepage(request):
	zxgg = Post.objects.filter(category__name = u'最新公告')[:4]
	xwkx = Post.objects.filter(category__name = u'新闻快讯')[:2]
	today = datetime.datetime.today()
	persons = Person.objects.filter(birthday__month = today.month).filter(birthday__day = today.day)
	messages = Message.objects.filter(pub_date__lte = today)[:3]
	print messages
	return render_to_response("index.html",{ 'xwkx':xwkx, 'zxgg':zxgg, 'persons':persons, 'messages':messages },context_instance=RequestContext(request))

def list(request):
	return render_to_response("template_list_text.html",context_instance=RequestContext(request))

def pics(request):
	return render_to_response("template_list_pic.html",context_instance=RequestContext(request))

def pt(request):
	return render_to_response("template_list_pt.html",context_instance=RequestContext(request))
