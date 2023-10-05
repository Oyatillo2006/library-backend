from django.contrib import admin

from .models import Student,Author,Book,Book_record

admin.site.register([Student,Author,Book,Book_record])
