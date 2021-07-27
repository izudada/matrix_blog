from django.urls import  reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect, request


from .models import Article, Comment, Dislikes, Likes, User
from .forms import RegisterForm, AddNewForm, NewCommentForm

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Article
    fields = ['title', 'body']
    success_url = reverse_lazy('index')
    template_name = 'create_article.html'

    def form_valid(self, form):
        slug = form.instance.title.split(' ')
        slug = ('-').join(slug)
        form.instance.slug = slug
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