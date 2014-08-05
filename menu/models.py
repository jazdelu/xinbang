# -*- coding: utf-8 -*-
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from post.models import Category
from page.models import Page
# Create your models here.

MTYPE_CHOICE = (
	( '0', u'分类目录'),
	( '1', u'页面'),
	( '2', u'自定义页面'),
)

MENU_CHOICE = (
	( '0', u'顶部菜单'),
)

class MenuItem(MPTTModel):
	name = models.CharField(max_length = 128, verbose_name = u'菜单项名称')
	menu = models.CharField(max_length = 128, verbose_name = u'所属菜单', choices = MENU_CHOICE, default = 0)
	parent = TreeForeignKey('self',verbose_name = u'父菜单项',null = True, blank = True)
	mtype = models.CharField(max_length = 128, choices = MTYPE_CHOICE, verbose_name = u'菜单项类型')
	category = TreeForeignKey(Category,verbose_name = u'分类目录', blank = True, null = True,related_name = 'items')
	page = models.ForeignKey(Page, verbose_name = u'页面', blank = True, null = True,related_name = 'items')
	url = models.CharField(max_length = 512, verbose_name = u'链接', null = True , blank = True)
	weight = models.IntegerField(verbose_name = u'权重', help_text = u'影响菜单项从左到右的顺序')


	class MPTTMeta:
		order_insertion_by = ['menu','-weight']

	class Meta:
		verbose_name = u'菜单项'
		verbose_name_plural = u'菜单项'

	def __unicode__(self):
		return self.name



	def save(self, *args, **kwargs):
		s = '/'
		if self.mtype == '0':
			s+='category/'+str(self.category.id)+'/'
			print s
			self.url = s
		if self.mtype == '1':
			s+='page/'+str(self.page.id)+'/'
			print s
			self.url = s
		super(MenuItem, self).save(*args, **kwargs)
		MenuItem.objects.rebuild()