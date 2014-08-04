# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Page(models.Model):
	name = models.CharField(max_length = 128, verbose_name = u'页面名称')
	banner = models.ImageField(upload_to = 'banner', verbose_name = u'顶部图片', null = True, blank = True)
	template = models.CharField(max_length = 128, verbose_name = u'选择模版',help_text = u'请选择与页面名称相对应的模版')
	content = models.TextField(verbose_name = u'页面内容',blank = True, null = True)

	class Meta:
		verbose_name = u'页面'
		verbose_name_plural = u'页面'

	def __unicode__(self):
		return self.name