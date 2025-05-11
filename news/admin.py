'''
news.admin.py
'''
from django.contrib import admin

from .models import MSource, Article

#from django_celery_beat.models import PeriodicTask, IntervalSchedule

# Register your models here.
admin.site.register(MSource)
admin.site.register(Article)

#celery_beat models
#admin.site.register(PeriodicTask)
#admin.site.register(IntervalSchedule)
