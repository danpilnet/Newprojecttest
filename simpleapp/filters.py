import django_filters
from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):


   class Meta:
       model = Post
       fields = {
           'text': ['icontains', ],
           'post_news': ['exact']}
