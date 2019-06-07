# works/models
from django.db import models


class Work(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    
    owner = models.ForeignKey('auth.User', related_name='works', on_delete=models.CASCADE)
    
    fandom = models.CharField(max_length=100, blank=True, default='')
    tags = models.CharField(max_length=100, blank=True, default='')


    class Meta:
        ordering = ('created',)


class TextWork(Work):

    contents = models.CharField(max_length=100, blank=True, default='')

class CollectionWork(Work):

    contents = Work()

class MediaWork(Work):
# add upload/storage for files to be inherited
    contents = models.FileField()

class AudioWork(MediaWork):
    duration = models.DurationField()

class ImageWork(MediaWork):
    boo = models.CharField(max_length=100, blank=True, default='')

class VideoWork(MediaWork):
    duration = models.DurationField()
    media = models.FileField()