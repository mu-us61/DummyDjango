from django.shortcuts import render, redirect
from django.contrib import messages  # TODO gercekten burasimi yeri kontrol et
from .models import MyUser

# Create your views here.


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if MyUser.objects.filter(username=username).exists():
            messages.warning(request, "the username is taken bro")
            return redirect()  #!TODO render yada redirect hala karistiriyorum
        else:
            user = MyUser(username=username)
            user.set_password(password)
            user.save()
            messages.success(request, "user is registered successfully")
            return redirect("home")

    return render(request, "AppAuth/register.html")


def login(request):
    error = "something not right"
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = MyUser.objects.get(username=username)
            if user.check_password(password):
                # Save user ID in session
                request.session["user_id"] = user.id
                messages.success(request, "user has logged in")
                return redirect("home")
            else:
                return render(request, "AppAuth/login.html", {"error": error})
        except MyUser.DoesNotExist:
            return render(request, "AppAuth/login.html", {"error": error})

    return render(request, "AppAuth/login.html")


def logout(request):
    request.session.flush()  # Clear session data
    # del request.session['user_id']  # alternative ?  but will this delete ? because in mdiddleware ?
    messages.info(request, "user has logged out")
    return redirect("home")
