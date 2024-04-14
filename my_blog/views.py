from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "my_blog/index.html"
    paginate_by =6
