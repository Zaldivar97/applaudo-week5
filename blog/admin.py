from django.contrib import admin

from .models import Post, Tag, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'user', 'created_at')
    search_fields = ('title', 'user__username', 'created_at')

    fields = [
        'user',
        'title',
        'content',
        'tags',
        'likes',
        'active',
        'created_at'
    ]
    readonly_fields = ('created_at',)

class CommentAdmin(admin.ModelAdmin):
    
    list_display = ('__str__', 'post', 'created_at')
    search_fields = ('post__title', 'user__username', 'created_at')

    fields = [
        'post',
        'user',
        'content',
        'likes',
        'created_at',
    ]
    readonly_fields = ('created_at',)

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
