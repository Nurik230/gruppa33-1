from django.contrib import admin
from . import models

admin.site.register(models.Mobile)
admin.site.register(models.Hashtag)
admin.site.register(models.Review)

