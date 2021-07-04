from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
import random
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.views.generic import CreateView

from .models import CommentModel, StoryModel
from .forms import CommentPostForm


def signupfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            User.objects.create_user(username, "", password)
            return redirect("login")
        except IntegrityError:
            return render(request, "signup.html", {"error": "このユーザーは既に登録されています"})
        except ValueError:
            return render(request, "signup.html", {"error": "ユーザー情報を入力してください"})
    return render(request, "signup.html", {})


def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "login.html", {"error": "ユーザーが登録されていないかユーザー情報が間違っています"})
    return render(request, "login.html", {})


def logoutfunc(request):
    logout(request)
    return redirect("index")


def indexfunc(request):
    storymodel_count = StoryModel.objects.all().count()
    if storymodel_count is not None:
        random_pk = random.randint(2, storymodel_count)
        return render(request, "index.html", {"random_pk": random_pk})
    else:
        return render(request, "index.html", {"random_pk": 1})


def readfunc(request, pk):
    if request.method == "POST":
        form = CommentPostForm(request.POST)
        try:
            post = form.save(commit=False)
            post.save()
            return redirect(request.META['HTTP_REFERER'])
        except ValueError:
            return redirect(request.META['HTTP_REFERER'])
    else:
        story_object = StoryModel.objects.get(pk=pk)
        comment_objects = CommentModel.objects.all().filter(story_id=pk)
        return render(request, "read.html", {"story_object": story_object, "comment_objects": comment_objects})


class StoryCreate(CreateView):
    template_name = "create.html"
    model = StoryModel
    fields = ("title", "content", "recommend_drink", "author_id")
    success_url = reverse_lazy("index")
