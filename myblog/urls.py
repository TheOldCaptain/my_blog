from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^index/$', views.index_page, name='index_page'),

    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),

    url(r'^about/$', views.about_page, name='about_page'),

    url(r'^contact/$', views.contact_page, name='contact_page'),

    url(r'^edit/$', views.edit_page, name='edit_page'),

    url(r'^edit_action/(?P<article_id>[0-9]+)$', views.edit_action, name='edit_action'),

    url(r'^login_edit/$', views.login_page, name='login_page'),

    url(r'^logined_edit/$', views.login_action, name='login_action'),

    url(r'^message/$', views.message_page, name='message_page'),

    url(r'^message_show/$', views.message_onshow, name='message_onshow'),

    url(r'^modify_login/(?P<article_id>[0-9]+)$', views.modify_login, name='modify_login'),




]
