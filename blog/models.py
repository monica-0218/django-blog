import os
import random
from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from markdown import markdown
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = models.CharField('カテゴリー名', max_length=255)
    slug = models.SlugField('英語名', unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'カテゴリー'
        verbose_name_plural = 'カテゴリー'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('タグ名', max_length=255)
    slug = models.SlugField('英語名', unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'タグ'
        verbose_name_plural = 'タグ'

    def __str__(self):
        return self.name


class Author(models.Model):
    icon = models.ImageField('アイコン', help_text='正方形の画像にしてください', upload_to='author-icon/')
    name = models.CharField('ニックネーム', max_length=15)
    description = models.TextField('自己紹介', max_length=500)
    TwitterID = models.CharField(max_length=15, help_text='@はいりません')

    class Meta:
        verbose_name = '記者'
        verbose_name_plural = '記者'

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)
    thumbnail = models.ImageField('サムネ', upload_to='images/')
    title = models.CharField('タイトル', max_length=255)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, blank=False)
    description = models.CharField('headタグでの説明', max_length=255, blank=False)
    content = models.TextField('本文')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField('公開日', blank=False, null=True)
    is_public = models.BooleanField('公開する', default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = '記事'
        verbose_name_plural = '投稿記事'

    def save(self, *args, **kwargs):
        if self.is_public and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Site(models.Model):
    content = models.TextField('本文', help_text='サイトの説明を書いてください。また、このモデルは追加をしても意味がないのでご了承ください。')

    class Meta:
        verbose_name = 'サイトの説明'
        verbose_name_plural = 'サイトの説明'


class PrivacyPolicy(models.Model):
    content = models.TextField('本文', help_text='プライバシーポリシーを書いてください。また、このモデルは追加をしても意味がないのでご了承ください。')

    class Meta:
        verbose_name = 'プライバシーポリシー'
        verbose_name_plural = 'プライバシーポリシー'
