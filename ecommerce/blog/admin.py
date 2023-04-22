from django.contrib import admin
from .models.posts import Post, PostCategory
from .models.comments import Comment
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug')
    search_fields = ['category_name', 'category_description']
    prepopulated_fields = {'slug': ('category_name',)}

# admin.site.register(Comment, CommentAdmin)

# admin.site.register(Post, PostAdmin)
