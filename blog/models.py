# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BlogPost(models.model):
    title=models.CharField(max_length = 150)
    body=models.TextField()
    time=models.DateTimeField()
    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg
