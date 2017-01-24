# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    easiness = models.IntegerField(default=0)
    take_again = models.IntegerField(default=0)
    def __str__(self):   # 在python2版本中使用的是__unique__
        return self.question_text

    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):   # 在python2版本中使用的是__unique__
        return self.choice_text

class EasinessVote(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    easinessvote_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):   # 在python2版本中使用的是__unique__this is a testing for git
        return self.easinessvote_text
