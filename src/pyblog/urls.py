from django.conf.urls import url
from . import views
urlpatterns = [
    
    url(r'^$',views.index,name='index'),
    url(r'^post/draft/$',views.draft,name='draft'),
    url(r'^post/detail/(?P<pk>\d+)/$',views.post_detail,name='post_detail'),
    url(r'^post/edit/(?P<pk>\d+)/$',views.post_edit,name='post_edit'),
    url(r'^post/publish/(?P<pk>\d+)/$',views.post_publish,name='post_publish'), 
    url(r'^post/remove/(?P<pk>\d+)/$',views.post_remove,name='post_remove'),  
    url(r'^post/new/$',views.post_new,name='post_new'),
    url(r'^post/drafts/$', views.post_draft_list, name='post_draft_list'),
]
