from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib import messages

# TODO form_asp acilacak daha ayrintili bir sekilde, kaynagi nerede nasil bakilir hepsi bakilcak


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


# def home(request):
#     errors = {}
#     title = ""
#     description = ""

#     if request.method == "POST":
#         # retrieve data from form
#         title = request.POST.get("title", "").strip()
#         description = request.POST.get("description", "").strip()

#         # check for errors
#         if title == "":
#             errors["title"] = "bu alani doldurmak zorunludur"
#         elif len(title) < 4:
#             errors["title"] = "en az 4 harf olmali"
#         elif len(title) > 12:
#             errors["title"] = "en cok 12 harf olabilir"

#         if description == "":
#             errors["description"] = "bu alani doldurmak zorunludur"
#         elif len(description) < 4:
#             errors["description"] = "en az 4 harf olmali"
#         elif len(description) > 12:
#             errors["description"] = "en cok 12 harf olabilir"
#         # if no errors complete the form and save the Article
#         if not errors:
#             Article.objects.create(title=title, description=description)
#             messages.success(request, "the article created successfully")
#             return redirect("home")

#     articles = Article.objects.all()
#     context = {
#         "errors": errors,
#         "title": title,
#         "description": description,
#         "articles": articles,
#     }
#     return render(request, "home.html", context=context)
