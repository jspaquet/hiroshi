from django.db import models
from taggit.managers import TaggableManager

from authentication.models import User


class Bookmark(models.Model):
    title = models.CharField(blank=True, null=True, max_length=500, verbose_name='Title')
    link = models.URLField(verbose_name='Link')
    archived_flag = models.BooleanField(default=False, verbose_name='Archived')
    deleted_flag = models.BooleanField(default=False, verbose_name='Deleted')
    new_flag = models.BooleanField(default=True, verbose_name='New')
    obsoleted_flag = models.BooleanField(default=False, verbose_name='Obsoleted')
    creation_at = models.DateTimeField(auto_now_add=True, verbose_name='Creation At')
    modification_at = models.DateTimeField(auto_now=True, verbose_name='Modification At')
    tags = TaggableManager()
    owner = models.ForeignKey(User, related_name='bookmarks', on_delete=models.CASCADE)
