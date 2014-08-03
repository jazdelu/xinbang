from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from menu.models import MenuItem
from django.forms import ModelForm
from suit.widgets import EnclosedInput
# Register your models here.

class MenuItemAdminForm(ModelForm):
	class Meta:
		model = MenuItem

	class Media:
		js = ('/static/xinbang/js/menu_admin.js',)


class MenuItemAdmin(MPTTModelAdmin):
	mptt_level_indent = 20
	list_display = ('name','menu','mtype','url','weight','id')
	list_display_links = ('name',)
	form = MenuItemAdminForm

admin.site.register(MenuItem,MenuItemAdmin)