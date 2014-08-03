# -*- coding: utf-8 -*-
from django.db import models
import datetime
# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length = 128, verbose_name = "员工姓名")
	birthday = models.DateField(verbose_name = "生日", help_text = u'生日年份可以任意选择' )

	class Meta:
		verbose_name = u'员工生日'
		verbose_name_plural = u'员工生日'

	def __unicode__(self):
		return self.name

class Message(models.Model):
	content = models.TextField(verbose_name = '内容')
	pub_date = models.DateTimeField(verbose_name = "发布日期", default = datetime.datetime.today())

	class Meta:
		verbose_name = u'曝光内容'
		verbose_name_plural = u'曝光内容'

	def __unicode__(self):
		return str(self.id)