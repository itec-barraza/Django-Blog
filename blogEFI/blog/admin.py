from django.contrib import admin
from .models import Categoria, Post


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('published', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    search_fields = ('title', 'content', 'author__username')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'category__name')

    def post_categories(self, obj):
        return ", ".join([
            c.name for c in obj.category.all().order_by("name")
        ])


admin.site.register(Post, PostAdmin)
admin.site.register(Categoria)

# Register your models here.
