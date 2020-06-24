from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import (
    Post,
    Category,
    Tag,
    Author,
    Site,
    PrivacyPolicy,
)


class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Post_list'] = Post.objects.all()
        context['Category_list'] = Category.objects.all()
        context['Tag_list'] = Tag.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['get_previous_by_pk'] = Post.objects.filter(pk__lt=self.kwargs['pk']).order_by('pk').last()
        context['get_next_by_pk'] = Post.objects.filter(pk__gt=self.kwargs['pk']).order_by('pk').first()
        context['Post_list'] = Post.objects.all()
        context['Category_list'] = Category.objects.all()
        context['Tag_list'] = Tag.objects.all()
        return context

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj.is_public and not self.request.user.is_authenticated:
            raise Http404
        return obj


class TagPostView(ListView):
    model = Post
    template_name = 'blog/tag_post.html'
    paginate_by = 10

    def get_queryset(self):
        tags_slug = self.kwargs['tags_slug']
        self.tags = get_object_or_404(Tag, slug=tags_slug)
        qs = super().get_queryset().filter(tags=self.tags)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = self.tags
        context['Category_list'] = Category.objects.all()
        context['Tag_list'] = Tag.objects.all()
        return context


class CategoryPostView(ListView):
    model = Post
    template_name = 'blog/category_post.html'
    paginate_by = 10

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        self.category = get_object_or_404(Category, slug=category_slug)
        qs = super().get_queryset().filter(category=self.category)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['Category_list'] = Category.objects.all()
        context['Tag_list'] = Tag.objects.all()
        return context


class SearchPostView(ListView):
    model = Post
    template_name = 'blog/search_post.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        lookups = (
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(category__name__icontains=query) |
                Q(tags__name__icontains=query)
        )
        if query is not None:
            qs = super().get_queryset().filter(lookups).distinct()
            return qs
        qs = super().get_queryset()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context


class AuthorListView(ListView):
    template_name = 'blog/author_list.html'
    model = Author
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Category_list'] = Category.objects.all()
        context['Tag_list'] = Tag.objects.all()
        return context


class ContactView(TemplateView):
    template_name = 'blog/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Category_list'] = Category.objects.all()
        context['Tag_list'] = Tag.objects.all()
        return context


class SiteDescriptionView(TemplateView):
    model = Site
    template_name = 'blog/this-site.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Category_list'] = Category.objects.all()
        context['Tag_list'] = Tag.objects.all()
        context['Site_description'] = Site.objects.all()
        return context


class PrivacyPolicyView(TemplateView):
    model = PrivacyPolicy
    template_name = 'blog/privacy-policy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Category_list'] = Category.objects.all()
        context['Tag_list'] = Tag.objects.all()
        context['PrivacyPolicy'] = PrivacyPolicy.objects.all()
        return context