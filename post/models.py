# -*- coding: utf-8 -*-
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField
import datetime
# Create your models here.
TEMPLATE_CHOICE = (
	('0',u'新闻列表'),
	('1',u'图片列表'),
	('2',u'图文列表'),
)

class Category(MPTTModel):
	name = models.CharField(max_length = 128, verbose_name = u'分类名称')
	template = models.CharField(max_length = 128, verbose_name = u'模版类型',choices = TEMPLATE_CHOICE)
	banner = models.ImageField(upload_to = 'banner/',verbose_name = u'顶部图片', null = True, blank = True)
	parent = TreeForeignKey('self',verbose_name = u'上级分类',null = True, blank = True,related_name = 'children')

	class MPTTMeta:
		order_insertion_by = ['name']

	class Meta:
		verbose_name = u'分类目录'
		verbose_name_plural = u'分类目录'

	def __unicode__(self):
		return self.name

	def get_url(self):
		url = '/'
		c = self
		for c in c.get_ancestors(include_self = True):
			url +=c.slug+'/'
		return url

	def save(self, *args, **kwargs):
		super(Category, self).save(*args, **kwargs)
		Category.objects.rebuild()

class Post(models.Model):
	title = models.CharField(max_length = 128,verbose_name = u'文章标题')
	author = models.CharField(max_length = 128,verbose_name = u'作者',null = True, blank = True)
	category = TreeForeignKey(Category,verbose_name = u'分类目录',related_name = 'posts')
	content = RichTextField(verbose_name = u'文章内容',config_name='default', blank = True, null = True)
	cover = models.ImageField(upload_to = 'cover/', verbose_name = u'封面图片', blank = True, null = True)
	pub_date = models.DateTimeField(verbose_name=u'文章发布时间',default = datetime.datetime.today())
	last_modified = models.DateTimeField(verbose_name=u'最近修改时间',auto_now = True)

	def __unicode__(self):
		return self.title


	class Meta:
		verbose_name = u'文章'
		verbose_name_plural = u'文章'
		ordering = ['-pub_date',]