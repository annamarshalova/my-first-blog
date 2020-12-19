from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.main, name='main'),
    path('main/', views.main, name='main'),
    path('1/', views.mercury, name='mercury'),
    path('2/', views.venus, name='venus'),
    path('3/', views.earth, name='earth'),
    path('4/', views.mars, name='mars'),
    path('5/', views.jupiter, name='jupiter'),
    path('6/', views.saturn, name='saturn'),
    path('7/', views.uranus, name='uranus'),
    path('8/', views.neptune, name='neptune'),
    path('other/', views.other, name='other'),
    path('videos/', views.videos, name='videos'),
    path('test/', views.test, name='test'),
    path('posts/', views.posts, name='posts'),
    path('test_1/', views.test_1, name='test_1'),
    path('test_2/', views.test_2, name='test_2'),
    path('test_3/', views.test_3, name='test_3'),
    path('test_4/', views.test_4, name='test_4'),
    path('test_5/', views.test_5, name='test_5'),
    path('test_6/', views.test_6, name='test_6'),
    path('test_7/', views.test_7, name='test_7'),
    path('test_8/', views.test_8, name='test_8'),
    path('counting/', views.counting, name='counting'),
    path('result/', views.result, name='result'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('video/new/', views.video_new, name='video_new'),
    path('post/<int:pk>/delete/',views.delete,name='delete'),
    path('search/', views.search, name='search'),
]



