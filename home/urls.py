from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.update_profile, name='profile'),
    path('', views.AnnounceListView.as_view(), name='index'),
    path('info/', views.info, name='info'),
    url(r'^want_to_go/(?P<announce_pk>\d+)$', views.want_to_go, name='want-to-go'),
    url(r'^comment/(?P<announce_pk>\d+)$', views.add_comment, name='add-comment'),
    url(r'^tag/(?P<tag_pk>\d+)$', views.TagAnnounceListView.as_view(), name='tag-announces'),
    path('kaganov/', views.kaganov, name='kaganov'),
    path('zhuk/', views.zhuk, name='zhuk'),
    path('karpenko/', views.karpenko, name='karpenko'),
    path('redko/', views.redko, name='redko'),
    path('yushenko/', views.yushenko, name='yushenko'),
    path('committee/', views.committee, name='committee'),
    path('plan/', views.plan, name='plan'),
    path('literature/', views.literature, name='literature'),
]
