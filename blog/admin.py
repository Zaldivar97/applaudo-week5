from django.contrib import admin

from .models import Post, Tag, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    

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



admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
