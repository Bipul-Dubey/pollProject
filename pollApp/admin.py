from django.contrib import admin
from .models import Question,Voter

# Register your models here.
admin.site.register(Question)
admin.site.register(Voter)