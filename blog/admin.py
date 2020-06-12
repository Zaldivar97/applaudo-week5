from django.contrib import admin

from .models import Post, Tag, Comment


# Register your models here.
def mark_approved(modeladmin, request, queryset):
    queryset.update(approved=True)


mark_approved.short_description = "Mark selected posts as approved."


class PostAdmin(admin.ModelAdmin):
    list_filter = ('approved',)
    actions = (mark_approved,)
    list_display = ('title', 'user', 'created_at')
    search_fields = ('title', 'user__username', 'created_at')
    filter_horizontal = ('tags',)
    fields = [
        'user',
        'title',
        'content',
        'tags',
        'active',
        'created_at'
    ]
    readonly_fields = ('created_at',)
    ordering = ['created_at', 'id']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'post', 'created_at')
    search_fields = ('post__title', 'user__username', 'created_at')

    fields = [
        'post',
        'user',
        'content',
        'created_at',
    ]
    readonly_fields = ('created_at',)


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
