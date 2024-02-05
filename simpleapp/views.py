from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from datetime import datetime
from .filters import PostFilter
from django.urls import reverse_lazy
from .forms import PostForm



class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'post'
    ordering = ''
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context




class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'
    context_object_name = 'create'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.quantity = 13
        return super().form_valid(form)

class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    context_object_name = 'edit'


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    context_object_name = 'delete'


class PostSearch(ListView):
    model = Post
    template_name = 'post_search.html'
    context_object_name = 'search'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['time_now'] = datetime.now()
        return context
