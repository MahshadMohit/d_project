# to save the address of any modules we use url
from django.urls import path
# to use functions and addressing them from views.py
from . import views

urlpatterns = [
    path('', views.index, name='starting-page'),  # this url references index.html function of view page
    path('posts', views.posts, name='posts-page'),  # the name of url is made been referenced in project
    path('posts/<slug:slug>', views.single_post, name='post-detail-page')  # posts/new-post -> slug = new-post

]
