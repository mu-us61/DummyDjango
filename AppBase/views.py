from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.contrib import messages


# Create your views here.
def home(request):
    page = request.GET.get("page", 1)
    try:
        page = int(page)
    except ValueError:
        page = 1

    items_per_page = 10
    # articles = Article.objects.all()
    # Optimize: Use `.order_by()` to ensure consistent ordering
    articles = Article.objects.order_by("id")  # Order by newest first (-id)

    start = (page - 1) * items_per_page
    stop = page * items_per_page
    current_page_articles = articles[start:stop]
    total_articles = articles.count()  # Efficiently count total articles
    total_pages = (total_articles + items_per_page - 1) // items_per_page

    context = {
        "articles": current_page_articles,
        "current_page": page,
        "total_pages": total_pages,
    }

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
