from django.contrib import admin

from .models import Post,Category,Review

class PostAdmin(admin.ModelAdmin):
    list_display=['user','tile','draft']
    list_filter=['category']
    search_fields=['content','title']

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Review)
