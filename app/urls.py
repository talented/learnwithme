from django.conf.urls import url
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
        url(r'^$', views.home, name='home'),
        # url(r'^login/$', auth_views.login, name='login'),
        # url(r'^logout/$', auth_views.logout, name='logout'),
        url(r'^gigs/(?P<id>[0-9]+)/$', views.gig_detail, name='gig_detail'),

]
