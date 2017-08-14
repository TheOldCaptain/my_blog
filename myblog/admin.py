from django.contrib import admin

from myblog.models import Article, BlogUser, Message

admin.site.register(Article)
admin.site.register(BlogUser)
admin.site.register(Message)
