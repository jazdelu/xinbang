from django.contrib import admin
from util.models import Person, Message
from django.forms import ModelForm
from suit.widgets import SuitDateWidget,AutosizedTextarea
# Register your models here.

class PersonAdminForm(ModelForm):
	class Meta:
		model = Person
		widgets = {
			'birthday':SuitDateWidget,
		}

class PersonAdmin(admin.ModelAdmin):
	list_display = ('name','birthday')
	form = PersonAdminForm

admin.site.register(Person, PersonAdmin)


class MessageAdminForm(ModelForm):
	class Meta:
		model = Message
		widgets = {
			'content':AutosizedTextarea,
		}

class MessageAdmin(admin.ModelAdmin):
	list_display = ('id','pub_date')
	form = MessageAdminForm

admin.site.register(Message, MessageAdmin)