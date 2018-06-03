from django.contrib import admin
from django.urls import path,re_path
from . import views

app_name='posts-api'
urlpatterns = [
    path('PostList/',views.PostListApiView.as_view(), name='PostList'),
    path('<int:pk>/',views.PostDetailAPIView.as_view(),name='detail'),
    path('<int:pk>/delete/',views.PostDeleteAPIView.as_view(),name='delete'),
    path('<int:pk>/edit/',views.PostUpdateAPIView.as_view(),name='update'),
    path('create/',views.PostCreteApiView.as_view(),name='create')
]
