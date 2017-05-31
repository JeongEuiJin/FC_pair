from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

from blog.forms import PostCreateForm
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


def post_add(request):
    form = PostCreateForm()

    if request.method == 'GET':
        context = {
            'form': form
        }
        return render(request, 'blog/post_add.html', context)
    elif request.method == 'POST':
        print("POST run...")
        form = PostCreateForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            user = User.objects.first()
            post = Post.objects.create(
                title=title,
                text=text,
                author=user
            )
            return redirect('post_detail', pk=post.pk)
        else:
            context = {
                'form': form
            }
            return render(request, 'post_add.html', context)
