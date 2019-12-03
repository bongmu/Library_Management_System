# coding=utf-8
# File  : urls.py
# Author: Jack秦
# Date  : 2019/11/27
from django.conf.urls import url,include
from app01 import views

urlpatterns = [
    # 首页
    url(r'^home/',views.home,name='home'),

    # 登录相关
    url(r'^login/',views.login,name='login'),
    url(r'^register/',views.register,name='register'),

    # 图书相关
    url(r'^book_list/',views.boot_list,name='book_list'),
    url(r'^add_book/',views.add_book,name='add_book'),
    # url(r'^edit_book/(\d+)/(?P<currentPage>\d+)',views.edit_book,name='edit_book'),
    url(r'^edit_book/(\d+)',views.edit_book,name='edit_book'),
    # url(r'^delete_book/(\d+)',views.delete_book,name='delete_book'),

    # 出版社相关
    url(r'^publish_list/',views.publish_list,name='publish_list'),
    url(r'^add_publish/',views.add_publish,name='add_publish'),
    url(r'^edit_publish/(\d+)',views.edit_publish,name='edit_publish'),
    # url(r'^delete_publish/(\d+)',views.delete_publish,name='delete_publish'),

    # 作者相关
    url(r'^author_list/',views.author_list,name='author_list'),
    url(r'^add_author/',views.add_author,name='add_author'),
    # url(r'^add_publish/',views.add_publish,name='add_publish'),
    # url(r'^edit_publish/(\d+)',views.edit_publish,name='edit_publish'),
]
