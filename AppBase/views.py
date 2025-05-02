from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


def home(request):
    page = request.GET.get("page", 1)
    items_per_page = 10
    articles = Article.objects.order_by("id")  # Order by newest first (-id)

    query = request.GET.get("q", "")
    if query:
        articles = articles.filter(Q(title__icontains=query) | Q(description__icontains=query))

    paginator = Paginator(articles, items_per_page)
    try:
        current_page_articles = paginator.page(page)
    except Exception:
        current_page_articles = paginator.page(1)

    context = {
        "articles": current_page_articles,
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


class CreateView(FormView):
    form_class = ArticleForm
    template_name = "create.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "AArticle succesfully created")
        return response


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
