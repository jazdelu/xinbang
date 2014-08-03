from menu.models import MenuItem

def get_menu(request):
	items = MenuItem.objects.all()
	return { "items":items }