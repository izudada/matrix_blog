from django.urls import  reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect, request

from django.template.defaultfilters import slugify


from .models import Article, Comment, Dislikes, Likes, User
from .forms import RegisterForm, NewCommentForm

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        article_comments = Comment.objects.filter(article=self.get_object()).order_by('-created_at')
        if article_comments:
            data['comments'] = article_comments
        if self.request.user.is_authenticated:
            data['comment_form'] = NewCommentForm(instance=self.request.user)

        return data
    
    def post(self, request, *args, **kwargs):
        new_comment = Comment(body=request.POST.get('body'), author=self.request.user, article=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)


class DeleteArticleView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    fields = []
    success_url = reverse_lazy('index')

    def test_func(self):
        if self.request.user.is_staff:
            return True
        else:
            return False


class UpdateArticle(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ['title', 'body']

    def test_func(self):
        if self.request.user.is_staff:
            return True
        else:
            return False


class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Article
    fields = ['title', 'body']
    success_url = reverse_lazy('index')
    template_name = 'create_article.html'

    def form_valid(self, form):
        # slug = form.instance.title
        # slug = ('-').join(slug)
        form.instance.slug = slugify(form.instance.title)
        form.instance.author = self.request.user
        return super(ArticleCreateView, self).form_valid(form)
    
    def test_func(self):
        if self.request.user.is_staff:
            return True
        else:
            return False


class UserCreateView(CreateView):
    model = User
    # fields = ['first_name', 'last_name', 'email', 'username', 'password']
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

    def form_valid(self, form):
        return super(UserCreateView, self).form_valid(form)