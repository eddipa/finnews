'''
news URL Configuration
'''
from django.urls import path
from .views import index, source_detail

app_name = 'news'

urlpatterns = [
    path('', index, name='index'),
    path('source/<int:source_id>/', source_detail, name='source_detail')
]
