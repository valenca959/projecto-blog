from django.urls import path
from blog.views import new_post, PostList, PostDetail

urlpatterns = [
    path('', PostList.as_view(), name='index'), 
    path("new/", new_post, name="new_post"),  
    path('<slug:slug>/', PostDetail.as_view(), name='detail'),
    ]