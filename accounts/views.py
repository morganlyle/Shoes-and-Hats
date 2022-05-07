from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, User

# from django.views.generic.edit import CreateView


# Create your views here.
# request --> response
#  request handler
#  action


def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = request.POST("username")
            password = request.POST("password")
            user = User.objects.create_user(
                username=username, password=password
            )
            user.save()
            login(request.user)

            return redirect("home")

    else:

        form = UserCreationForm(request.POST)
        context = {"form": form}
        return render(request, "registration/signup.html", context)
