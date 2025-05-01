from django.urls import path
from .views import MyView, PostList, PostDetail

urlpatterns = [
    path("", MyView.as_view(), name="myview"),
    path("list/", PostList.as_view(), name="post_list"),
    path("detail/<int:pk>", PostDetail.as_view(), name="post_detail"),
]
