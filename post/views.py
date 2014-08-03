from django.shortcuts import render_to_response
from post.models import Post, Category
from menu.models import MenuItem
from django.http import Http404
from django.template import RequestContext

# Create your views here.
def get_post_by_id(request,pid):
	post = ''
	try:
		post = Post.objects.get(id = pid)
	except:
		raise Http404

	posts = list(Post.objects.all())
	i = posts.index(post)
	next_p = ''
	prev_p = ''
	if len(posts)>1:
		if (i == 0):
			next_p = posts[i+1]
		elif (i == len(posts)-1):
			prev_p = posts[i-1]
		else:
			next_p = posts[i+1]
			prev_p = posts[i-1]
	else:
		pass

	menu = ''
	if post.category.items.all().count()>1:
		menu = post.category.items.filter(level__gt = 0)[0]
	else:
		menu = post.category.items.all()[0]

	return render_to_response("detail.html",{'post':post,'next_p':next_p, 'prev_p': prev_p, "menu":menu},context_instance=RequestContext(request))

def get_post_by_category(request,cid):
	category = ''
	try:
		category = Category.objects.get(id = cid)
	except:
		raise Http404

	posts = Post.objects.filter(category = cid)
	t = ''
	if category.template == '0':
		t = 'template_list_text.html'
	elif category.template == '1':
		t = 'template_list_pic.html'
	else:
		t = 'template_list_pt.html'

	menu = ''
	if category.items.all().count()>1:
		menu = category.items.filter(level__gt = 0)[0]
	else:
		menu = category.items.all()[0]

	return render_to_response(t,{'posts':posts,'category':category,"menu":menu},context_instance=RequestContext(request))

