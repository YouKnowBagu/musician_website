from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['post_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

admin.site.register(Post, PostAdmin)