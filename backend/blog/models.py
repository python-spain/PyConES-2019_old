from collections import defaultdict
from django.db import models


class Post(models.Model):

    I18N_KEYS = ['title', 'body']

    external_id = models.IntegerField()
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)  # Without add anytime the Post is modified the date updates
    lang = models.CharField(max_length=2) # ISO639-1

    @classmethod
    def get_i18n_list(cls):
        posts = list(cls.objects.all().values('external_id', 'title', 'created_on', 'last_modified', 'lang'))
        grouped_posts = defaultdict(list)
        for post in posts:
            grouped_posts[post.get('external_id')].append(post)
        return [cls.merge_posts(post) for post in grouped_posts.values()]

    @classmethod
    def get_i18n_post(cls, external_id):
        post_versions = list(cls.objects.filter(external_id=external_id).values())
        return cls.merge_posts(post_versions)


    @classmethod
    def merge_posts(cls, posts):
        final_post = {
           'id': posts[0].get('external_id'),
           'created_on': posts[0].get('created_on').strftime('%d-%m-%Y'),
           'last_modified': posts[0].get('last_modified').strftime('%d-%m-%Y'),
        }
        for post in posts:
            final_post = {
                **final_post,
                **{f"{k}_{post.get('lang')}":v for k, v in post.items() if k in cls.I18N_KEYS}
            }
        return final_post