from django.urls import include, path

from .views import ArticleListView, ArticleDetailView, UserCreateView, ArticleCreateView, UpdateArticle, DeleteArticleView, preference

urlpatterns = [
    path('<int:pk>/preference/', preference, name="preference"),
    path('<slug:slug>/delete/', DeleteArticleView.as_view(), name="delete_article"),
    path('<slug:slug>/edit/', UpdateArticle.as_view(), name="update_article"),
    path('create_article/', ArticleCreateView.as_view(), name="create_article"),
    path('<slug:slug>', ArticleDetailView.as_view(), name='article_detail'),
    path('', ArticleListView.as_view(), name='index'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('', include('django.contrib.auth.urls')),
]