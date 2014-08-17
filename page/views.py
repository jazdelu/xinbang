from django.shortcuts import render_to_response
from page.models import Page
from menu.models import MenuItem
from django.http import Http404
from django.template import RequestContext
# Create your views here.
def get_page_by_id(request,pid):
	page = ''
	try:
		page = Page.objects.get(id = pid)
	except:
		raise Http404

	menu = ''
	if page.items.all().count()>1:
		menu = page.items.filter(level__gt = 0)[0]
	else:
		menu = page.items.all()[0]

	target =''
	if request.GET:
		target = '#'+request.GET['target']	
	return render_to_response(page.template,{"page":page, "menu":menu,"target":target},context_instance=RequestContext(request))