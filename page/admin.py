from django.contrib import admin
from page.models import Page
from django.forms import ModelForm
from suit.widgets import AutosizedTextarea
# Register your models here.


class PageAdminForm(ModelForm):
	class Meta:
		model = Page
		widgets = {
			'content':AutosizedTextarea,
		}

class PageAdmin(admin.ModelAdmin):
	list_display = ('name','template',"id")
	form = PageAdminForm

admin.site.register(Page, PageAdmin)