from django.urls import path
from blog.views import *

urlpatterns = [
    path("", index, name="index"),
    path("blogs", blogs, name='blogs'),
    path("blog/<int:blog_id>", blog, name="blog"),
    path("about", about, name='about')
]