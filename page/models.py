# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
TEMPLATE_CHOICE = (
	('speech.html',u'董事长致辞'),
	('introduce.html',u'集团介绍'),
	('organization.html',u'组织架构'),
	('industry.html','集团产业'),
	('idea.html',u'企业理念'),
	('image.html',u'企业风采'),
	('contact.html',u'联系我们'),
)

# Create your models here.
class Page(models.Model):
	name = models.CharField(max_length = 128, verbose_name = u'页面名称')
	banner = models.ImageField(upload_to = 'banner', verbose_name = u'顶部图片', null = True, blank = True)
	template = models.CharField(max_length = 128, verbose_name = u'选择模版',help_text = u'请选择与页面名称相对应的模版',choices = TEMPLATE_CHOICE, unique = True)
	content = RichTextField(verbose_name = u'页面内容',config_name='default', blank = True, null = True)

	class Meta:
		verbose_name = u'页面'
		verbose_name_plural = u'页面'

	def __unicode__(self):
		return self.name