from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy, reverse
from .models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content', 'preview', 'created_at', 'publication_sign', 'views']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog_list')


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        """Возвращает список опубликованных статей."""
        queryset = super().get_queryset()
        return queryset.filter(publication_sign=True)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        """Считает просмотры статей."""
        counter = super().get_object()
        counter.views_count += 1
        counter.save()
        return counter


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'preview', 'created_at', 'publication_sign', 'views']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog_list')

    def get_success_url(self):
        """Перенаправление на страницу деталей только что отредактированного объекта"""
        return reverse('blog_detail', kwargs={'pk': self.object.pk})


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog_list')