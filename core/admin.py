from django.contrib import admin
from .models import UserProfile
from .models import Post

admin.site.register(UserProfile)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'project_description', 'created_at')
    search_fields = ('user__username', 'project_description', 'doubt_description')
    list_filter = ('created_at',)
