from django.contrib import admin
from .models import Post, Author, Tag

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author","tags")
    list_display = ("title","author","date")
    prepopulated_fields = {
        "slug" : ("title",)
    }
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post,PostAdmin)
