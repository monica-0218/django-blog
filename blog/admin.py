from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import (
    Category,
    Tag,
    Post,
    Author,
    Site,
    PrivacyPolicy,
)
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'thumbnail_preview', 'created_at', 'category', 'is_public')
    list_filter = ('is_public',)
    ordering = ('-created_at',)
    filter_horizontal = ('tags',)

    def thumbnail_preview(self, obj):
        return mark_safe('<img src="{}" style="width:100px; height:auto;">'.format(obj.thumbnail.url))

    thumbnail_preview.short_description = 'サムネ'
    summernote_fields = '__all__'


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('icon_preview', 'name')

    def icon_preview(self, obj):
        return mark_safe('<img src="{}" style="width:100px; height:auto;">'.format(obj.icon.url))


class SiteAdmin(SummernoteModelAdmin):
    pass


class PrivacyPolicyAdmin(SummernoteModelAdmin):
    pass


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(PrivacyPolicy, PrivacyPolicyAdmin)
