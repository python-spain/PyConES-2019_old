from django.shortcuts import render
from blog.models import Post


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')  # The minus means is ordered descending, from newer to older
    context = {
            'posts': posts,
    }
    return render(request, 'blog_index.html', context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
            'post': post,
    }

    return render(request, 'blog_detail.html', context)
    
