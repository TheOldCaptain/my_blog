from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now_add=True, blank=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{}--{}'.format(self.title, self.date_time)


class BlogUser(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class Message(models.Model):
    nickname = models.CharField(max_length=30)
    content = models.TextField(blank=True, null=True)
    date_time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return '{}--{}'.format(self.id,self.date_time)

    class Meta:
        ordering = ['date_time']
