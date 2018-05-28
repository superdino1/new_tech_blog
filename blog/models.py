# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model): # this line defines our model (it is an object). models.Model means that Post is a Django Model. So Django knows that it should be saved in the database
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) # The foreign key means a link to another model
    title = models.CharField(max_length = 200)  # this is how you define text with a limited number of characters
    text = models.TextField(default="some thoughts")   # this is for long text without a limit. Sounds ideal for blog post content, right?
    create_date = models.DateTimeField(default=timezone.now)  # this is a date and time
    publushed_date = models.DateField(blank = True, null=True) 
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def _str_(self):
        return self.title


"""
After we successfully initiate our model, we need to save it into our database.
"""


    



