'''
new.models.py
'''
from django.db import models
from django.urls import reverse

class MSource(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    feed_url = models.URLField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('news:source_detail', args=[str(self.id)])

class Article(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    content = models.TextField()
    published_at = models.DateTimeField()
    source = models.ForeignKey(MSource, on_delete=models.CASCADE, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('news:article_detail', args=[str(self.id)])


