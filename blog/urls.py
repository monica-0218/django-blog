from django.urls import path
from blog.views import (
    IndexView,
    PostDetailView,
    CategoryPostView,
    TagPostView,
    SearchPostView,
    AuthorListView,
    ContactView,
    SiteDescriptionView,
    PrivacyPolicyView,
)

app_name = 'blog'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('category/<str:category_slug>/', CategoryPostView.as_view(), name='category_post'),
    path('tag/<str:tags_slug>/', TagPostView.as_view(), name='tag_post'),
    path('search/', SearchPostView.as_view(), name='search_post'),
    path('author/', AuthorListView.as_view(), name='author_list'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('this-site/', SiteDescriptionView.as_view(), name='contact'),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name='privacy_policy'),
]
