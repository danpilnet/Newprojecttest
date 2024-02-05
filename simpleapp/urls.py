from django.urls import path
from .views import PostDetail, PostList, PostFilter, PostCreate, PostUpdate, PostDelete, PostSearch



urlpatterns = [
   path('', PostList.as_view()),
   path('<int:pk>/', PostDetail.as_view()),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('search/', PostSearch.as_view(), name= 'post_search'),
]

