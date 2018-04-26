# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Picture, Gallery, Photographer, Tag, Category

admin.site.register(Picture)
admin.site.register(Gallery)
admin.site.register(Photographer)
admin.site.register(Tag)
admin.site.register(Category)