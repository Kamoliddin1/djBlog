from django.shortcuts import render

from post.models import Post


def index(request):
    queryset = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    context = {
        'object_list': queryset,
        'latest': latest,
    }
    return render(request, 'index.html', context)

def blog(request):
    all_blogs = Post.objects.all()
    latest = Post.objects.order_by('-timestamp')[0:3]
    context = {
        'all_blogs': all_blogs,
        'latest': latest
    }
    return render(request, 'blog.html', context)

def post(request):
    return render(request, 'post.html')


