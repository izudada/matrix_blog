from django.db import models

from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import (PermissionsMixin, AbstractBaseUser, UserManager)
from django.utils import timezone

from django.utils.translation import gettext_lazy as _
from helpers.models import TrackingModel
from ckeditor.fields import RichTextField


class BlogUserManager(UserManager):
    
    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        # GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        # username = GlobalUserModel.normalize_username(username)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, TrackingModel):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """
    username_validator = UnicodeUsernameValidator()

    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=False, unique=True)
    username = models.CharField(
        _('username'),
        max_length=50,
        unique=True,
        help_text=_('Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    email_verified = models.BooleanField(
        _('email_verified'),
        default=False,
        help_text=_(
            'Designates whether this users email verified. '
        ),
    )
    objects = BlogUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def token(self):
        return ''

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('index')


class Article(TrackingModel, models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, related_name="articles", on_delete= models.CASCADE, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True)
    likes = models.ManyToManyField(User, related_name="likes")
    dislikes = models.ManyToManyField(User, related_name="dislikes")


    class Meta:
        ordering = ('-created_at',)


    def __str__(self):
        return self.title

    def get_absolute_url(self, **kwargs):
        return reverse('article_detail', kwargs={'slug': self.slug})

    @property
    def number_of_comments(self):
        return Comment.objects.filter(article=self).count()

    @property
    def number_of_likes(self):
        return self.likes.count()

    @property
    def number_of_dislikes(self):
        return self.dislikes.count()

    @property
    def all_liked(self):
        return self.likes.all()

    @property
    def all_disliked(self):
        return self.dislikes.all()


class Comment(TrackingModel, models.Model):
    author = models.ForeignKey(User, related_name="comments", on_delete= models.CASCADE, null=True)
    article = models.ForeignKey(Article, related_name="comments", on_delete= models.CASCADE, null=True)
    body = models.TextField()


    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.author) + ', ' + self.article.title[:40]

