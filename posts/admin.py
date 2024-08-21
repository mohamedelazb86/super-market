from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post,Category,Review

class PostAdmin(SummernoteModelAdmin):
    list_display=['user','title','draft']
    list_filter=['category']
    search_fields=['content','title']

    summernote_fields = ('content',)

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Review)
