import json

from django.http import HttpResponse
from blog.models import Post


def blog_index(request):
    return HttpResponse(json.dumps(Post.get_i18n_list()), status=200)


def blog_detail(request, pk):
    try:
        return HttpResponse(json.dumps(Post.get_i18n_post(pk)), status=200)
    except:
        return HttpResponse(status=404)
    
