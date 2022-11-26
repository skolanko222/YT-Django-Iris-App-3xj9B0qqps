from django.contrib import admin
from .models import PredResults


@admin.register(PredResults)
class PredResultAdmin(admin.ModelAdmin):
    pass 