# import json
# 
# from django.http import HttpResponse
# from blog.models import Post
# 
# 
# def blog_index(request):
#     return HttpResponse(json.dumps(Post.get_i18n_list()), status=200)
# 
# 
# def blog_detail(request, pk):
#     try:
#         return HttpResponse(json.dumps(Post.get_i18n_post(pk)), status=200)
#     except:
#         return HttpResponse(status=404)
from rest_framework import serializers, viewsets, renderers

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    renderer_classes = [renderers.JSONRenderer]
