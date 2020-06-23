from django.contrib import admin
from django.utils.safestring import mark_safe
from markdownx.admin import MarkdownxModelAdmin
from django.forms import TextInput, Textarea
from django.db import models
from .models import (
    Category,
    Tag,
    Post,
    Author,
    Site,
    PrivacyPolicy,
)


class PostAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'thumbnail_preview', 'created_at', 'category', 'is_public')
    list_filter = ('is_public',)
    ordering = ('-created_at',)
    filter_horizontal = ('tags',)

    def thumbnail_preview(self, obj):
        return mark_safe('<img src="{}" style="width:100px; height:auto;">'.format(obj.thumbnail.url))

    thumbnail_preview.short_description = 'サムネ'


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('icon_preview', 'name')

    def icon_preview(self, obj):
        return mark_safe('<img src="{}" style="width:100px; height:auto;">'.format(obj.icon.url))


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Site)
admin.site.register(PrivacyPolicy)
