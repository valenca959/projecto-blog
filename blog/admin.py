from django.contrib import admin
from blog.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "date_posted")
    list_filter = ("published", "date_posted")
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}
    ordering = ["-date_posted"]
    actions = ["make_published"]

    @admin.action(description="Publish/Unpublish selected posts")
    def make_published(self, request, queryset):
        for post in queryset:
            post.published = not post.published
            post.save()

admin.site.register(Post)
admin.site.register(Post, PostAdmin)