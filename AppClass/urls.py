from django.urls import path
from .views import MyView, PostList, PostDetail, PostCreate, PostUpdate, PostDelete

urlpatterns = [
    path("", MyView.as_view(), name="myview"),
    path("list/", PostList.as_view(), name="post_list"),
    path("detail/<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("postcreate/", PostCreate.as_view(), name="post_create"),
    path("postupdate/<int:pk>/", PostUpdate.as_view(), name="post_update"),
    path("postdelete/<int:pk>/", PostDelete.as_view(), name="post_delete"),
]
