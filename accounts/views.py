from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.


def register(request):
    if request.method == "POST":

        # GET FORM VALUES

        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        # CHECK IF PASSWORD MATCH

        if password == password2:

            # CHECK USERNAME
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is taken")
                return redirect("register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email is taken")
                    return redirect("register")

                else:
                    # Looks good
                    user = User.objects.create_user(
                        username=username,
                        password=password,
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                    )

                    user.save()
                    messages.success(request, "you are now Registered")
                    return redirect("login")

                    # Login

                    # auth.login(request, user)
                    # messages.success(request, "you are now loggedin")
                    # return redirect("index")

        else:

            messages.error(request, "Passwords do not match")
            return redirect("register")

    else:

        return render(request, "accounts/register.html")


def login(request):
    if request.method == "POST":
        # LOGIN USER

        return
    else:

        return render(request, "accounts/login.html")


def logout(request):
    return redirect("index")


def dashboard(request):
    return render(request, "accounts/dashboard.html")
