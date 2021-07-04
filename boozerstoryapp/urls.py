from django.contrib import admin
from django.urls import path
from .views import signupfunc, loginfunc, logoutfunc, indexfunc, readfunc, StoryCreate
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signupfunc, name="signup"),
    path('login/', loginfunc, name="login"),
    path('logout/', logoutfunc, name="logout"),
    path('/', indexfunc, name="index"),
    path('read/<int:pk>', readfunc, name="read"),
    path("create/", StoryCreate.as_view(), name="create"),
]
