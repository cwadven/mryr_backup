from django.contrib import admin
from .models import Board, Comments, Likes


class BoardAdmin(admin.ModelAdmin):

    list_display = ('id', 'author', 'title', 'likes_count')


admin.site.register(Board, BoardAdmin)


class CommentsAdmin(admin.ModelAdmin):

    list_display = ('id', 'author', 'message', 'created_at', 'updated_at')


admin.site.register(Comments, CommentsAdmin)


class LikesAdmin(admin.ModelAdmin):

    list_display = ('id', 'author', 'post')


admin.site.register(Likes, LikesAdmin)
