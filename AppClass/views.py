from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponse
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


# class MyView(View):

#     def get(self, request, *args, **kwargs):
#         return HttpResponse("this is my first class view")


class MyView(TemplateView):
    template_name = "AppClass/myview.html"
    extra_context = {"a": "A"}


class PostList(ListView):
    model = Post
    # template_name = "AppClass/post_list.html"  # Optional: default=[appname]/[modelname]_list.html
    # context_object_name = "posts"  # Optional: default=object_list
    paginate_by = 10  # Optional: if none then no pagination


class PostDetail(DetailView):
    model = Post


class PostCreate(CreateView):
    model = Post
    fields = ["title", "description"]
    # fields = "__all__"
    success_url = reverse_lazy("myview")
    # template_name DONE


class PostUpdate(UpdateView):
    model = Post
    fields = ["title", "description"]
    success_url = reverse_lazy("myview")


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy("myview")
