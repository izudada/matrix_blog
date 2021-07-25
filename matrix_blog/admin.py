from django.contrib import admin

from .models import Article, Comment, User, Dislikes, Likes


class CommentInline(admin.TabularInline):
    model = Comment


class LikesInline(admin.TabularInline):
    model = Likes

class DislikeInline(admin.TabularInline):
    model = Dislikes


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [CommentInline, LikesInline, DislikeInline]


admin.site.register(Article, ArticleAdmin)
admin.site.register(User)