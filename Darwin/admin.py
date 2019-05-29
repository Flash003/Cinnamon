from django.contrib import admin
from Darwin import models

admin.site.register(models.Client)
admin.site.register(models.Disease)
admin.site.register(models.Symptom)
admin.site.register(models.Store)