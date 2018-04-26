
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_view


app_name = 'photos'

urlpatterns =[
    #/photos
    url(r'^$', views.index, name='index'),
    #/photos/1
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    url(r'^photographer/$', views.view_photographer, name='view_photographer'),

    url(r'^tags/$', views.view_tags, name='view_tags'),

    #/photos/picture/add
    url(r'picture/add/$', views.PictureCreate.as_view(), name='picture-add'),
    #
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', auth_view.login, {'template_name':'photos/login.html'},name='login'),
    url(r'^logout/$', auth_view.logout, {'template_name': 'photos/logout.html'},name='logout'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$',views.edit_profile,name='edit_profile'),
    url(r'^profile/image$',views.profile_image,name='profile_image'),
    url(r'^profile/password/$',views.change_password,name='change_password'),
    url(r'^invite/$', views.friend_invite, name='invite'),
    url(r'^accept/(?P<code>\w+)/$', views.friend_accept, name='friend_accept'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.PictureDelete, name='picture_delete'),
    url(r'^like/(?P<picture_pk>(\d+))/$', views.like, name='like'),
    url(r'^download/(?P<picture_pk>\w+)/$', views.download, name='download'),



]
