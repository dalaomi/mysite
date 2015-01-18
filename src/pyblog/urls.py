from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^post/draft/$',views.draft,name='draft'),
    url(r'^post/detail/(?P<pk>\d+)/$',views.post_detail,name='post_detail'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
]
