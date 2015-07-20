"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from django import forms
from django.contrib import admin

from software.models import Software


class SoftwareAdminForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = ['name', 'img', 'description', 'platform', 'button', 'hero',]


class SoftwareAdmin(admin.ModelAdmin):
    form = SoftwareAdminForm


admin.site.register(Software, SoftwareAdmin)
