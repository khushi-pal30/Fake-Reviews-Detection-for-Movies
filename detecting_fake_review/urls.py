"""detecting_fake_review URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path
from review.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('login_page', login_page,name="login_page"),
    path('signup', signup,name="signup"),
    path('admin_home', admin_home,name="admin_home"),
    path('user_home', user_home,name="user_home"),
    path('logout', logout,name="logout"),
    path('view_user', view_user,name="view_user"),
    path('delete_user\<int:pid>', delete_user,name="delete_user"),
    path('add_movie', add_movie,name="add_movie"),
    path('view_movie_admin', view_movie_admin,name="view_movie_admin"),
    path('view_movie_user', view_movie_user,name="view_movie_user"),
    path('delete_movie\<int:id>', delete_movie,name="delete_movie"),
    path('edit_movie\<int:id>', edit_movie,name="edit_movie"),
    path('change_poster\<int:id>', change_poster,name="change_poster"),
    path('change_passwordadmin', change_passwordadmin,name="change_passwordadmin"),
    path('change_passworduser', change_passworduser,name="change_passworduser"),
    path('feedback', feedback,name="feedback"),
    path('user_profile', user_profile,name="user_profile"),
    path('add_review_user\<int:id>', add_review_user,name="add_review_user"),
    path('view_review_user\<int:id>', view_review_user,name="view_review_user"),
    path('view_feedback', view_feedback,name="view_feedback"),
    path('delete_feedback\<int:id>', delete_feedback,name="delete_feedback"),
    path('delete_contact\<int:id>', delete_contact,name="delete_contact"),
    path('view_review_admin\<int:id>', view_review_admin,name="view_review_admin"),
    path('detect_review', detect_review,name="detect_review"),
    path('delete_review\<int:id>', delete_review,name="delete_review"),
    path('contact', contact,name="contact"),
    


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
