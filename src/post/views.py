from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import Paginator

from post.models import Post


def search(request):
    query = request.GET.get('q')
    result_list = Post.objects.filter(
        Q(title__icontains=query) | Q(overview__icontains=query)
    )
    context = {
        'result_list': result_list,
    }
    return render(request, 'search_results.html', context)


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
    paginator = Paginator(all_blogs, 2)
    page = request.GET.get('page')
    paginated_blogs = paginator.get_page(page)

    context = {
        'latest': latest,
        'queryset': paginated_blogs,
    }
    return render(request, 'blog.html', context)


def post(request):
    return render(request, 'post.html')


