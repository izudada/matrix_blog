from django.urls import include, path

from .views import ArticleListView, ArticleDetailView, UserCreateView, ArticleCreateView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('create_article/', ArticleCreateView.as_view(), name="create_article"),
    path('<slug:slug>', ArticleDetailView.as_view(), name='article_detail'),
    path('', ArticleListView.as_view(), name='index'),
    path('register/', UserCreateView.as_view(), name='register'),
]