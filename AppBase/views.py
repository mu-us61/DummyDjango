from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.contrib import messages


# Create your views here.
def home(request):

    articles = Article.objects.all()
    context = {"articles": articles}

    return render(request, "home.html", context=context)


def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()  # save article to database
            messages.success(request, "Article succesfully created")
            return redirect("home")
    else:
        form = ArticleForm()

    context = {"form": form}
    return render(request, "create.html", context=context)


def read(request, id):
    # article = Article.objects.get(id=id) #TODO sorulcak
    article = get_object_or_404(Article, id=id)
    return render(request, "read.html", {"article": article})


def update(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, "succesfully updated")
            return redirect(read, id=id)
    form = ArticleForm(instance=article)

    return render(request, "update.html", {"form": form})


def delete(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == "POST":
        article.delete()
        return redirect("home")
    return render(request, "delete.html", {"article": article})
