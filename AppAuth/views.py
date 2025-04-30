from django.shortcuts import render, redirect
from django.contrib import messages  # TODO gercekten burasimi yeri kontrol et
from django.contrib.auth import get_user_model, authenticate, login as auth_login, logout as auth_logout

User = get_user_model()
# Create your views here.


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.warning(request, "the username is taken bro")
            return redirect("register")  # TODO render yada redirect hala karistiriyorum
        else:
            user = User.objects.create_user(username=username, password=password)  # TODO  double check
            auth_login(request, user)  # TODO authenticate yapmadi ?
            messages.success(request, "user is registered successfully")
            return redirect("home")
    return render(request, "AppAuth/register.html")


def login(request):
    error = "something not right"
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("home")
        else:
            return render(request, "AppAuth/login.html", {"error": error})

        # try:
        #     user = User.objects.get(username=username)
        #     if user.check_password(password):
        #         # Save user ID in session
        #         request.session["user_id"] = user.id
        #         messages.success(request, "user has logged in")
        #         return redirect("home")
        #     else:
        #         return render(request, "AppAuth/login.html", {"error": error})
        # except User.DoesNotExist:
        #     return render(request, "AppAuth/login.html", {"error": error})

    return render(request, "AppAuth/login.html")


def logout(request):
    auth_logout(request)
    # request.session.flush()  # Clear session data
    # del request.session['user_id']  # alternative ?  but will this delete ? because in mdiddleware ?
    messages.info(request, "user has logged out")
    return redirect("home")
