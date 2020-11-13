from django.urls import path
from . import views
from .views import (
	PostListView, 
	PostDetailView, 
	PostCreatView,
	PostUpdateView,
	PostDeletelView,
	UserPostListView,
)

urlpatterns = [

	path('',PostListView.as_view(), name='blog-home'),
	path('user/<str:username>',UserPostListView.as_view(), name='user-posts'),
	path('about/', views.about, name ='blog-about'),
	path('post/<int:pk>',PostDetailView.as_view(), name = 'post-detail'),
	path('post/new',PostCreatView.as_view(), name = 'post-create'),
	path('post/<int:pk>/update',PostUpdateView.as_view(), name = 'post-update'),
	path('post/<int:pk>/delete',PostDeletelView.as_view(), name = 'post-delete'),

	]