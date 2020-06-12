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
    ordering = ['-created_at', '-id']


class CommentAdmin(admin.ModelAdmin):
    list_filter = ('approved',)
    actions = (mark_approved,)
    list_display = ('user_name', 'post', 'comment_content', 'created_at')
    search_fields = ('post__title', 'user__username', 'created_at')

    def test(self):
        return [self.get_object().commentreport_set.all()]

    def user_name(self, obj, *args, **kwargs):
        return obj.__str__()

    user_name.short_description = 'Created By'

    def comment_content(self, obj, *args, **kwargs):
        content = obj.content
        print(content)
        if len(content) > 9:
            content = content[0:20] + '...'
            print(content)
        return content

    fields = [
        'post',
        'user',
        'content',
        'approved',
        'created_at',
    ]
    readonly_fields = ('created_at', 'approved', 'content')
    ordering = ['-created_at', '-id']


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
