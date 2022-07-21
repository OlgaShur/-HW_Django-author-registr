from django.urls import path
from .views import PostList, PostDelete, PostUpdate, PostDetail, PostListSearch, PostCreate

urlpatterns = [
    path('',PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post'),
    path('search', PostListSearch.as_view(), name='news-search'),
    path('create/', PostCreate.as_view(), name='news-create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='news-update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='news-delete'),

]
