from django.contrib import admin
from .models import Question, Choice, EasinessVote

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(EasinessVote)