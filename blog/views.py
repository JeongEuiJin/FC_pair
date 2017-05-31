from django.contrib.auth import get_user_model
from django.shortcuts import render

from blog.models import Post

User = get_user_model()

def post_list(request):
    posts = Post.objects.order_by('-created_date')
    context = {
        'posts': posts,
        'title': 'blaaka',
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):

    context = {
        'posts': Post.objects.get(pk=pk),

    }
    return render(request, 'blog/post_detail.html', context)