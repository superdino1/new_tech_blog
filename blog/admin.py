# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Post


# Register your models here.

admin.site.register(Post)
"""
In here, we want to make our model visible on the admin page, we need to 
register the model with above code
"""
