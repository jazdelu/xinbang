from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'xinbang.views.homepage', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$','xinbang.views.homepage',name = 'Homepage'),
    url(r'^post/(?P<pid>\d+)/$','post.views.get_post_by_id',name= 'getPostById'),
    url(r'^page/(?P<pid>\d+)/$','page.views.get_page_by_id',name= 'getPageById'),
    url(r'^category/(?P<cid>\d+)/$','post.views.get_post_by_category',name= 'get_post_by_category'),
    url(r'^ckeditor/', include('ckeditor.urls')),
)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
