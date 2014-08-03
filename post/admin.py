from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from post.models import Category, Post
from suit.widgets import SuitSplitDateTimeWidget
from django.forms import ModelForm
# Register your models here.

class CategoryAdmin(MPTTModelAdmin):
	mptt_level_indent = 20
	list_display = ('name','id')
	list_display_links = ('name',)

admin.site.register(Category,CategoryAdmin)


class PostAdminForm(ModelForm):
	class Meta:
		model = Post
		widgets = {
			'pub_date':SuitSplitDateTimeWidget,
		}


class PostAdmin(admin.ModelAdmin):
	list_display = ('title','author','category','pub_date','id')
	fields = ('title','category','cover','content','pub_date')
	list_filter=('category',)
	form = PostAdminForm

	def save_model(self, request, obj, form, change):
		name = ""
		if request.user.last_name or request.user.first_name:
			name = request.user.last_name+request.user.first_name
		else:
			name = "admin"
		obj.author = name
		obj.save()

admin.site.register(Post,PostAdmin)