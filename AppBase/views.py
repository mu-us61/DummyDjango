from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib import messages


# Create your views here.
def home(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()  # save article to database
            messages.success(request, "Article succesfully created")
            return redirect("home")
    else:
        form = ArticleForm()

    articles = Article.objects.all()
    context = {"articles": articles, "form": form}

    return render(request, "home.html", context=context)


def create():
    pass


def read():
    pass


def update():
    pass


def delete():
    pass
